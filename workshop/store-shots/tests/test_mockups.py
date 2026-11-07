"""Every device frame, cards, badges, status bar states and clusters, placed
by the layout's placement data."""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest
from PIL import Image, ImageChops

from conftest import SKILL, copy_example

STORE_SIZES = {
    "app_store/en-US/iphone69": (1320, 2868),
    "app_store/en-US/ipad13": (2064, 2752),
    "app_store/en-US/mac": (2880, 1800),
    "play/en-US/android_phone": (1440, 2560),
    "play/en-US/android_tablet": (1800, 3200),
}
PANELS = ("p1", "p2", "p3")
IPHONE_P2 = "out/app_store/en-US/iphone69-p2.png"


@pytest.fixture(scope="module")
def built(tmp_path_factory):
    """One build of the whole example, for the tests that only read it."""
    example = copy_example(tmp_path_factory.mktemp("built") / "example")
    run = example.run("build")
    assert run.code == 0, run.out + run.err
    return example


def _calls(example) -> list[dict]:
    if not example.calls.is_file():
        return []
    return [json.loads(line) for line in example.calls.read_text(encoding="utf-8").splitlines()]


def _mtimes(example) -> dict[str, int]:
    return {p.relative_to(example.root).as_posix(): p.stat().st_mtime_ns
            for p in sorted(example.path("out").rglob("*.png"))}


def test_every_frame_kind_renders_each_panel_at_its_store_size(built):
    for prefix, size in STORE_SIZES.items():
        for panel in PANELS:
            with Image.open(built.path(f"out/{prefix}-{panel}.png")) as image:
                assert image.size == size, f"{prefix}-{panel}"
                assert image.mode == "RGB"


def test_the_badge_text_comes_from_copy_and_is_recorded_in_the_image(built):
    for prefix in STORE_SIZES:
        with Image.open(built.path(f"out/{prefix}-p2.png")) as image:
            assert image.text["Copy"].splitlines() == [
                "Your notes stay yours.",
                "Recognition runs on your device.",
                "Works in airplane mode",
            ]


def test_a_cluster_captures_each_stores_own_devices(built):
    scenes = {call["device"]: call["scenes"] for call in _calls(built)}

    assert [s for s in scenes["iphone69"] if s.startswith("everywhere")] == [
        "everywhere-mac", "everywhere-ipad", "everywhere-iphone"]
    assert [s for s in scenes["android_phone"] if s.startswith("everywhere")] == [
        "everywhere-mac", "everywhere-android_tablet", "everywhere-android_phone"]


def test_a_cluster_shows_the_copy_of_its_store(built):
    with Image.open(built.path("out/app_store/en-US/iphone69-p3.png")) as image:
        assert "iPhone, iPad and Mac" in image.text["Copy"]
    with Image.open(built.path("out/play/en-US/android_phone-p3.png")) as image:
        assert "phone, tablet and Mac" in image.text["Copy"]


def _move_iphone_p2_badge(example, left: str) -> None:
    placement = example.path("layout/placement.yaml")
    placement.write_text(placement.read_text(encoding="utf-8").replace(
        "  badge: {left: 41vw, top: calc(61vh - 6.8vw), font-size: 4vw}\n",
        "  badge: {left: 41vw, top: calc(61vh - 6.8vw), font-size: 4vw}\n"
        f"  panels:\n    p2:\n      badge: {{left: {left}}}\n", 1))


def test_moving_one_panels_badge_recomposes_only_that_panel_and_never_captures(full_example):
    assert full_example.run("build").code == 0
    calls = len(_calls(full_example))
    before = _mtimes(full_example)
    with Image.open(full_example.path(IPHONE_P2)) as image:
        old = image.copy()

    _move_iphone_p2_badge(full_example, "8vw")
    run = full_example.run("build")

    assert run.code == 0, run.out
    assert len(_calls(full_example)) == calls
    after = _mtimes(full_example)
    assert [p for p in before if after[p] != before[p]] == [IPHONE_P2]
    with Image.open(full_example.path(IPHONE_P2)) as image:
        moved = ImageChops.difference(old, image.convert("RGB")).getbbox()
    # The badge sat from 41vw (541 px); now it starts at 8vw (106 px).
    assert moved is not None and moved[0] < 541


def test_a_shared_placement_entry_recomposes_every_panel_of_its_frame(full_example):
    assert full_example.run("build").code == 0
    before = _mtimes(full_example)

    placement = full_example.path("layout/placement.yaml")
    placement.write_text(placement.read_text(encoding="utf-8").replace(
        "  card: {left: 27vw, width: 68vw, top: 61vh, border-radius: 4vw}",
        "  card: {left: 25vw, width: 68vw, top: 61vh, border-radius: 4vw}", 1))
    assert full_example.run("build").code == 0

    after = _mtimes(full_example)
    assert sorted(p for p in before if after[p] != before[p]) == [
        f"out/app_store/en-US/iphone69-{panel}.png" for panel in PANELS]


INK_SOFT = (111, 103, 89)
# The tracer's iPhone sits at 25vh (y = 717); copy must end 0.8vh (23 px) above.
DEVICE_TOP, GAP = 717, 23
# A one-line headline: 9.6vw type at 1.08 line height from 7vh.
HEADLINE_END = 340


def _text_bands(image, colour, top, bottom) -> list[tuple[int, int]]:
    """Runs of rows holding [colour]: one per line of text."""
    pixels = image.load()
    rows = [y for y in range(top, bottom)
            if any(all(abs(c - k) <= 16 for c, k in zip(pixels[x, y], colour))
                   for x in range(0, image.width, 2))]
    bands: list[tuple[int, int]] = []
    for y in rows:
        if bands and y - bands[-1][1] <= 4:
            bands[-1] = (bands[-1][0], y)
        else:
            bands.append((y, y))
    return bands


def test_a_long_subline_shrinks_to_two_lines_ending_above_the_device(example):
    example.write("texts/en.yaml", "panels:\n  p1:\n    headline: Searchable.\n    subline: Find"
                  " anything you have ever noted, in every notebook, every folder and every page,"
                  " in a few seconds, wherever you are.\n")

    assert example.run("build").code == 0
    with Image.open(example.path("out/app_store/en-US/iphone69-p1.png")) as image:
        bands = _text_bands(image, INK_SOFT, HEADLINE_END, DEVICE_TOP)
    assert 1 <= len(bands) <= 2
    assert bands[-1][1] < DEVICE_TOP - GAP


def test_airplane_mode_changes_only_the_status_bar(example):
    assert example.run("build").code == 0
    panel = example.path("out/app_store/en-US/iphone69-p1.png")
    with Image.open(panel) as image:
        normal = image.copy()

    storyboard = example.path("storyboard.yaml")
    storyboard.write_text(storyboard.read_text(encoding="utf-8").replace("status: normal", "status: airplane"))
    assert example.run("build").code == 0

    with Image.open(panel) as image:
        changed = ImageChops.difference(normal, image.convert("RGB")).getbbox()
    # The status bar is the top 6.5% of the 69vw-wide screen, under the bezel.
    assert changed is not None
    assert DEVICE_TOP < changed[1] and changed[3] < DEVICE_TOP + 23 + 130


CARD_PANEL = """panels:
  - id: p1
    claim: Every note can be found by its text.
    scene: home
    card: home-card
    evidence: [adapter/fake_adapter.py]
"""


def test_a_card_larger_than_the_screen_fails_the_capture(example):
    example.write("storyboard.yaml", CARD_PANEL)
    example.env["FAKE_ADAPTER_SIZE"] = "home-card=1400x400"

    run = example.run("build")

    assert run.code != 0
    assert run.lines[0].startswith(
        "capture: FAILED, iphone69: en/iphone69-home-card.png is 1400x400,"
        " larger than the 1320x2868 screen")


def test_a_card_within_the_screen_is_composed_over_the_device(example):
    example.write("storyboard.yaml", CARD_PANEL)

    assert example.run("build").code == 0
    # The fake card's top quarter is sky blue; the card sits at 27vw, 61vh.
    with Image.open(example.path("out/app_store/en-US/iphone69-p1.png")) as image:
        assert image.getpixel((700, 1800)) == (222, 239, 253)


CLUSTER_PANEL = """panels:
  - id: p1
    claim: The same notes open on every device.
    cluster:
      app_store:
        - {frame: mac, scene: everywhere-mac}
        - {frame: iphone, scene: everywhere-iphone}
    evidence: [adapter/fake_adapter.py]
"""


def test_a_cluster_device_shaped_unlike_its_frames_target_screen_fails_the_capture(example):
    example.write("storyboard.yaml", CLUSTER_PANEL)
    example.env["FAKE_ADAPTER_SIZE"] = "everywhere-iphone=1320x2000"

    run = example.run("build")

    assert run.code != 0
    assert run.lines[0].startswith(
        "capture: FAILED, iphone69: en/iphone69-everywhere-iphone.png is 1320x2000, not the"
        " shape of the 1320x2868 iphone screen")


def test_a_cluster_device_at_another_resolution_of_its_screens_shape_passes(example):
    example.write("storyboard.yaml", CLUSTER_PANEL)
    example.env["FAKE_ADAPTER_SIZE"] = "everywhere-iphone=660x1434"

    run = example.run("build")

    assert run.code == 0, run.out


def test_a_cluster_device_without_a_target_of_its_frame_keeps_the_frames_orientation(example):
    example.write("storyboard.yaml", CLUSTER_PANEL)
    example.env["FAKE_ADAPTER_SIZE"] = "everywhere-mac=1600x2560"

    run = example.run("build")

    assert run.code != 0
    assert run.lines[0].startswith(
        "capture: FAILED, iphone69: en/iphone69-everywhere-mac.png is 1600x2560, not a"
        " landscape mac screen")


MOCKUPS = SKILL / "engine" / "store_shots" / "mockups"


def test_the_mockups_hold_no_text_but_the_status_bar_clock():
    script = (MOCKUPS / "mockup.js").read_text(encoding="utf-8")
    markup = "".join(re.findall(r"'(<[^']*>)'", script))
    texts = [t for t in re.findall(r">([^<]+)<", markup) if t.strip()]
    assert texts and set(texts) == {"9:41"}
    for sheet in MOCKUPS.rglob("*.css"):
        values = re.findall(r"(?<![-\w])content:\s*([^;]+);", sheet.read_text(encoding="utf-8"))
        assert all(value == '""' for value in values), sheet.name


def test_a_device_without_a_placed_screen_width_fails_naming_it(example):
    placement = example.path("layout/placement.yaml")
    placement.write_text(placement.read_text(encoding="utf-8").replace(
        "  device: {--screen-w: 69vw, left: 6vw, top: 25vh}", "  device: {left: 6vw, top: 25vh}"))

    run = example.run("build")

    assert run.code != 0
    assert run.lines[1].startswith(
        "compose: FAILED, placement.yaml: no device --screen-w for iphone69 (iphone) in p1")
