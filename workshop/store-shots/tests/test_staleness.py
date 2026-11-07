"""Every output records the inputs it was made from; `build` redoes only what
is stale and `status` names it."""

from __future__ import annotations

import json

PANEL = "out/app_store/en-US/iphone69-p1.png"


def _calls(example) -> list[dict]:
    if not example.calls.is_file():
        return []
    return [json.loads(line) for line in example.calls.read_text(encoding="utf-8").splitlines()]


def test_a_second_build_with_no_changes_captures_and_composes_nothing(example):
    assert example.run("build").code == 0
    calls = len(_calls(example))
    panel = example.path(PANEL).stat().st_mtime_ns

    run = example.run("build")

    assert run.code == 0, run.out
    assert len(_calls(example)) == calls
    assert example.path(PANEL).stat().st_mtime_ns == panel
    assert run.lines[0].startswith("capture: ok, nothing stale")
    assert run.lines[1].startswith("compose: ok, nothing stale")


P2 = "out/app_store/en-US/iphone69-p2.png"
COPY = """panels:
  p1:
    headline: {p1}
  p2:
    headline: Search in every notebook.
"""


def _two_panels(example, p1="Every note you take, searchable."):
    example.write("storyboard.yaml", """panels:
  - id: p1
    claim: Every note can be found by its text.
    scene: home
    evidence: [adapter/fake_adapter.py]
  - id: p2
    claim: Search reaches every notebook.
    scene: search
    evidence: [adapter/fake_adapter.py]
""")
    example.write("texts/en.yaml", COPY.format(p1=p1))


def _mtimes(example, *paths) -> list[int]:
    return [example.path(p).stat().st_mtime_ns for p in paths]


def test_a_changed_headline_recomposes_only_its_panel_and_never_runs_the_adapter(example):
    _two_panels(example)
    assert example.run("build").code == 0
    calls = len(_calls(example))
    before = _mtimes(example, PANEL, P2)

    _two_panels(example, p1="Every note, found.")
    run = example.run("build")

    assert run.code == 0, run.out
    assert len(_calls(example)) == calls
    after = _mtimes(example, PANEL, P2)
    assert after[0] != before[0]
    assert after[1] == before[1]
    assert run.lines[1].startswith("compose: ok, 1 image of 2")


def _scene_inputs(example):
    """The example adapter with one input file per scene, as an app's scene
    files would be."""
    config = example.path("store-shots.yaml")
    config.write_text(config.read_text(encoding="utf-8").replace(
        "inputs: [adapter/**]", "inputs: [adapter/**, 'scenes/{scene}.txt']"))
    example.path("scenes").mkdir()
    example.write("scenes/home.txt", "home v1\n")
    example.write("scenes/search.txt", "search v1\n")


HOME_RAW = "raw/iphone69/en/iphone69-home.png"
SEARCH_RAW = "raw/iphone69/en/iphone69-search.png"


def test_a_changed_adapter_input_recaptures_its_scene_then_recomposes_its_panel(example):
    _two_panels(example)
    _scene_inputs(example)
    assert example.run("build").code == 0
    calls = len(_calls(example))
    before = _mtimes(example, PANEL, P2)

    example.write("scenes/home.txt", "home v2\n")
    example.env["FAKE_ADAPTER_SHADE"] = "240,250,255"
    run = example.run("build")

    assert run.code == 0, run.out
    assert [(c["langs"], c["scenes"]) for c in _calls(example)[calls:]] == [(["en"], ["home"])]
    after = _mtimes(example, PANEL, P2)
    assert after[0] != before[0]
    assert after[1] == before[1]


def test_a_partial_capture_leaves_the_other_scenes_raws_byte_identical(example):
    _two_panels(example)
    assert example.run("build").code == 0
    search = example.path(SEARCH_RAW).read_bytes()
    search_inputs = example.path(SEARCH_RAW.replace(".png", ".inputs.json")).read_bytes()
    calls = len(_calls(example))

    example.path(HOME_RAW).unlink()
    example.env["FAKE_ADAPTER_SHADE"] = "240,250,255"
    assert example.run("build").code == 0

    assert [c["scenes"] for c in _calls(example)[calls:]] == [["home"]]
    assert example.path(HOME_RAW).is_file()
    assert example.path(SEARCH_RAW).read_bytes() == search
    assert example.path(SEARCH_RAW.replace(".png", ".inputs.json")).read_bytes() == search_inputs


def test_status_names_each_stale_output_and_its_reason_by_stage_and_changes_nothing(example):
    _two_panels(example)
    _scene_inputs(example)
    assert example.run("build").code == 0
    calls = len(_calls(example))

    example.write("scenes/home.txt", "home v2\n")
    example.write("texts/en.yaml", COPY.format(p1="Every note you take, searchable.")
                  .replace("Search in every notebook.", "Search everything."))
    run = example.run("status")

    assert run.code == 0, run.out
    assert run.lines == [
        "capture: 1 stale of 2",
        "  raw/iphone69/en/iphone69-home.png: adapter inputs changed",
        "compose: 2 stale of 2",
        "  out/app_store/en-US/iphone69-p1.png: raw raw/iphone69/en/iphone69-home.png to be captured",
        "  out/app_store/en-US/iphone69-p2.png: copy en panels.p2 changed",
        "exit 0",
    ]
    assert len(_calls(example)) == calls


def test_status_after_a_build_reports_every_stage_current(example):
    assert example.run("build").code == 0

    run = example.run("status")

    assert run.lines == ["capture: nothing stale (1 raw current)",
                         "compose: nothing stale (1 image current)", "exit 0"]


def test_capture_takes_only_stale_raws_unless_forced(example):
    _two_panels(example)
    assert example.run("build").code == 0
    calls = len(_calls(example))

    idle = example.run("capture")
    forced_one = example.run("capture", "--force", "--scene", "search")
    forced_all = example.run("capture", "--force")

    assert idle.lines == ["capture: ok, nothing stale", "exit 0"]
    assert forced_one.code == forced_all.code == 0
    assert [c["scenes"] for c in _calls(example)[calls:]] == [["search"], ["home", "search"]]
    assert example.run("status").lines[0] == "capture: nothing stale (2 raws current)"


def test_capture_names_an_unknown_scene(example):
    run = example.run("capture", "--force", "--scene", "nope")

    assert run.code == 1
    assert run.lines[0] == "capture: FAILED, no scene nope; known: home"
    assert not example.calls.exists()


def test_status_on_a_fresh_project_names_missing_outputs(example):
    run = example.run("status")

    assert run.lines == [
        "capture: 1 stale of 1",
        "  raw/iphone69/en/iphone69-home.png: missing",
        "compose: 1 stale of 1",
        "  out/app_store/en-US/iphone69-p1.png: raw raw/iphone69/en/iphone69-home.png to be captured",
        "exit 0",
    ]


def test_editing_a_panels_claim_and_evidence_recomposes_nothing(example):
    assert example.run("build").code == 0
    storyboard = example.path("storyboard.yaml")
    storyboard.write_text(storyboard.read_text(encoding="utf-8")
                          .replace("Every note can be found by its text.", "Every note is found.")
                          .replace("- adapter/fake_adapter.py", "- adapter/fake_adapter.py#main"))

    run = example.run("build")

    assert run.code == 0, run.out
    assert run.lines[1] == "compose: ok, nothing stale (1 image current)"


def test_a_changed_target_screen_makes_its_raws_stale(example):
    assert example.run("build").code == 0
    config = example.path("store-shots.yaml")
    config.write_text(config.read_text(encoding="utf-8").replace(
        "size: [1320, 2868]}", "size: [1320, 2868], screen: [1320, 2700]}"))

    run = example.run("status")

    assert run.lines[:2] == ["capture: 1 stale of 1",
                             "  raw/iphone69/en/iphone69-home.png: target changed"]
