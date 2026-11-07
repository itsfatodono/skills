"""The adapter contract under capture and under `adapter test`. The fake
adapter breaks one rule at a time through FAKE_ADAPTER_BREAK."""

from __future__ import annotations

import json

import pytest

from conftest import Example

TWO_LANGUAGES = ("languages:\n  en: {app_store: en-US}\n",
                 "languages:\n  en: {app_store: en-US}\n  tr: {app_store: tr}\n")


def two_languages(example: Example) -> None:
    example.write("store-shots.yaml", example.path("store-shots.yaml").read_text(encoding="utf-8")
                  .replace(*TWO_LANGUAGES))


def add_adapter_key(example: Example, line: str) -> None:
    """Adds [line] under the config's `adapter:`."""
    example.write("store-shots.yaml", example.path("store-shots.yaml").read_text(encoding="utf-8")
                  .replace("adapter:\n", f"adapter:\n  {line}\n"))


def gates(run) -> list[str]:
    """`<gate>: <result>` of each gate line."""
    return [line.split(" ", 2)[2].split(",")[0] for line in run.lines if line.startswith("adapter ")]


class TestTheRequest:
    def test_names_what_each_scene_must_be_so_the_adapter_reads_no_project_file(self, full_example):
        full_example.env["FAKE_ADAPTER_OMIT"] = "home"  # fail, so the work folder stays
        full_example.run("capture", "--target", "iphone69")

        request = json.loads(full_example.path(".store-shots/work/capture/iphone69.request.json")
                             .read_text(encoding="utf-8"))
        assert request["contract"] == 1
        assert request["target"] == {"id": "iphone69", "store": "app_store", "device": "iphone",
                                     "frame": "iphone", "screen": [1320, 2868]}
        assert request["langs"] == {"en": "en-US"}
        assert request["scenes"]["home"] == {"role": "screen", "size": [1320, 2868]}
        assert request["scenes"]["editor-card"] == {"role": "card", "max_size": [1320, 2868]}
        assert request["scenes"]["everywhere-mac"] == {"role": "member", "frame": "mac",
                                                       "shape": [2560, 1600]}
        assert request["out"].endswith(".store-shots/work/capture/iphone69")


class TestCapture:
    @pytest.mark.parametrize("broken, reason", [
        ("no-checks", "en/iphone69-home.png has no `checked` line in the report"),
        ("no-text", "en/iphone69-home.png: the report checked no text; a screen with none goes"
                    " in the config's adapter.textless"),
        ("extra-file", "unexpected file debug.log in --out"),
    ])
    def test_a_run_breaking_the_contract_writes_no_raw(self, example, broken, reason):
        example.env["FAKE_ADAPTER_BREAK"] = broken

        run = example.run("capture")

        assert run.lines[0] == "capture: FAILED, iphone69: " + reason + \
            " (log: .store-shots/logs/capture-iphone69.log)"
        assert not example.path("raw").exists()

    def test_a_scene_listed_as_textless_may_check_no_text(self, example):
        example.env["FAKE_ADAPTER_BREAK"] = "no-text"
        add_adapter_key(example, "textless: [home]")

        assert example.run("capture").code == 0

    def test_the_same_image_in_every_language_fails_the_capture(self, example):
        two_languages(example)
        example.env["FAKE_ADAPTER_BREAK"] = "one-language"

        run = example.run("capture")

        assert run.lines[0].startswith("capture: FAILED, iphone69: iphone69-home is the same image"
                                       " in every language (en, tr): does the adapter set the"
                                       " app's locale?")

    def test_a_report_line_the_owner_accepted_passes(self, example):
        line = "en/iphone69-home.png: 'Settings' shows 7 of 8 characters"
        example.env["FAKE_ADAPTER_REPORT"] = line
        assert example.run("capture").lines[0].startswith("capture: FAILED, iphone69: report: " + line)

        add_adapter_key(example, f'accepted: ["{line}"]')

        assert example.run("capture").code == 0

    def test_a_scene_named_like_a_probe_is_refused(self, example):
        example.write("storyboard.yaml", example.path("storyboard.yaml").read_text(encoding="utf-8")
                      .replace("scene: home", "scene: __home"))

        run = example.run("capture")

        assert run.lines[0] == "capture: FAILED, scene __home: names starting with `__` are the" \
                               " engine's own (adapter test's probes)"


class TestAdapterTest:
    def test_a_good_adapter_passes_every_gate_and_writes_no_raw(self, example):
        two_languages(example)

        run = example.run("adapter", "test")

        assert run.code == 0, run.out
        assert gates(run) == ["runs: ok", "unknown-scene: ok", "full-bleed: ok", "cut-off-text: ok",
                              "one-scene: ok", "languages: ok", "every-scene: skipped",
                              "repeatable: ok"]
        assert not example.path("raw").exists()
        assert not example.path(".store-shots/work/adapter-test/iphone69").exists()

    def test_before_the_storyboard_names_scenes_the_scene_gates_skip(self, example):
        example.write("storyboard.yaml", "panels: []\n")

        run = example.run("adapter", "test")

        assert run.code == 0, run.out
        assert gates(run)[4:] == ["one-scene: skipped", "languages: skipped",
                                  "every-scene: skipped", "repeatable: ok"]

    @pytest.mark.parametrize("broken, gate, reason", [
        ("extra-file", "runs", "unexpected file debug.log in --out"),
        ("ignore-unknown", "unknown-scene", "exit 0 and no report line for"
                                            " en/iphone69-__no_such_scene.png"),
        ("status-bar", "full-bleed", "pixels from (0,0) to (1320,57) of 1320x2868 are not the"
                                     " probe fill #FF00FF at the top: a status bar"),
        ("miss-cut-off", "cut-off-text", "no report line for en/iphone69-__probe_truncation.png"),
        ("no-checks", "full-bleed", "en/iphone69-__probe_fullbleed.png has no `checked` line"),
        ("one-language", "languages", "iphone69-home is the same image in every language"),
        ("random", "repeatable", "en/iphone69-home.png differs between two runs"),
    ])
    def test_a_broken_rule_fails_its_gate_and_stops_the_target_there(self, example, broken,
                                                                     gate, reason):
        two_languages(example)
        example.env["FAKE_ADAPTER_BREAK"] = broken

        run = example.run("adapter", "test")

        assert run.code == 1
        failed = [line for line in run.lines if "FAILED" in line]
        assert len(failed) == 1
        assert failed[0].startswith(f"adapter iphone69 {gate}: FAILED, {reason}")
        assert gates(run)[-1] == f"{gate}: FAILED"

    def test_an_unknown_target_is_named(self, example):
        run = example.run("adapter", "test", "--target", "watch")

        assert run.lines[0] == "adapter: FAILED, no target watch; known: iphone69"
