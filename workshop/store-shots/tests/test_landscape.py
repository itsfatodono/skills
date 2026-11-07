"""Targets turned to landscape: their slot sizes, raws, device frames,
placement and cluster members, and the status bar choices."""

from __future__ import annotations

import pytest
from PIL import Image, ImageChops

from store_shots import layout

from test_mockups import INK_SOFT, _text_bands

LANDSCAPE = (2868, 1320)
PANEL = "out/app_store/en-US/iphone69-p1.png"


@pytest.fixture
def landscape(example):
    """The tracer with its iPhone target turned to landscape."""
    config = example.path("store-shots.yaml")
    config.write_text(config.read_text(encoding="utf-8").replace(
        "size: [1320, 2868]", "size: [2868, 1320]"), encoding="utf-8")
    return example


def _set_status(example, status: str) -> None:
    storyboard = example.path("storyboard.yaml")
    storyboard.write_text(storyboard.read_text(encoding="utf-8").replace(
        "status: normal", f"status: {status}"), encoding="utf-8")


def _image(example, rel: str = PANEL) -> Image.Image:
    with Image.open(example.path(rel)) as image:
        return image.convert("RGB")


def _changed(before: Image.Image, after: Image.Image) -> tuple[int, int, int, int] | None:
    """Where the two differ by more than Chrome's run-to-run anti-aliasing,
    which reaches about 16 levels; a drawn or removed glyph differs by far more."""
    return ImageChops.difference(before, after).point(lambda v: 255 if v > 40 else 0).getbbox()


def test_a_landscape_target_captures_landscape_screens_and_composes_at_its_size(landscape):
    run = landscape.run("build")

    assert run.code == 0, run.out
    with Image.open(landscape.path("raw/iphone69/en/iphone69-home.png")) as raw:
        assert raw.size == LANDSCAPE
    assert _image(landscape).size == LANDSCAPE


def test_a_landscape_target_takes_its_frames_landscape_placement(landscape):
    assert landscape.run("build").code == 0
    image = _image(landscape)
    # The example's iphone `landscape` entry puts the device at 41vw (1176 px)
    # from 20vh (264 px), right of the copy, which ends at 38vw (1090 px).
    pixels = image.load()
    dark = [x for x in range(image.width) for y in (270, 276) if max(pixels[x, y]) < 70]
    assert dark and min(dark) > 1090


def test_text_beside_a_device_keeps_its_size(landscape):
    assert landscape.run("build").code == 0
    # The subline (1.9vw, 54 px type) would shrink to 8 px if the device
    # beside it counted as one it must end above.
    bands = _text_bands(_image(landscape), INK_SOFT, 0, LANDSCAPE[1])
    assert bands and max(bottom - top for top, bottom in bands) > 30


def test_a_landscape_iphone_shows_no_status_bar(landscape):
    assert landscape.run("build").code == 0
    normal = _image(landscape)

    _set_status(landscape, "airplane")
    assert landscape.run("build").code == 0

    assert _changed(normal, _image(landscape)) is None


def test_status_none_removes_only_the_status_bar(example):
    assert example.run("build").code == 0
    normal = _image(example)

    _set_status(example, "none")
    assert example.run("build").code == 0

    changed = _changed(normal, _image(example))
    # The tracer's iPhone sits at 25vh (y = 717); its status bar is the top
    # 6.5% of the screen, under the bezel.
    assert changed is not None
    assert 717 < changed[1] and changed[3] < 717 + 23 + 130


def test_an_unknown_status_names_the_choices(example):
    _set_status(example, "offline")

    run = example.run("build")

    assert run.code != 0
    assert "panel p1: status must be one of normal, airplane, none" in run.out


CLUSTER_PANEL = """panels:
  - id: p1
    claim: The same notes open on every device.
    cluster:
      app_store:
        - {frame: mac, scene: everywhere-mac}
        - {frame: ipad, scene: everywhere-ipad}
        - {frame: iphone, scene: everywhere-iphone}
    evidence: [adapter/fake_adapter.py]
"""


def test_cluster_members_on_a_landscape_target_are_landscape(landscape):
    landscape.write("storyboard.yaml", CLUSTER_PANEL)

    run = landscape.run("build")

    assert run.code == 0, run.out
    for scene in ("everywhere-ipad", "everywhere-iphone"):
        with Image.open(landscape.path(f"raw/iphone69/en/iphone69-{scene}.png")) as raw:
            assert raw.width > raw.height, scene


def test_a_portrait_member_on_a_landscape_target_fails_the_capture(landscape):
    landscape.write("storyboard.yaml", CLUSTER_PANEL)
    landscape.env["FAKE_ADAPTER_SIZE"] = "everywhere-ipad=2064x2752"

    run = landscape.run("build")

    assert run.code != 0
    assert run.lines[0].startswith(
        "capture: FAILED, iphone69: en/iphone69-everywhere-ipad.png is 2064x2752, not a"
        " landscape ipad screen")


PLACEMENT = {
    "iphone": {"device": {"left": "6vw", "top": "25vh"},
               "panels": {"p1": {"device": {"top": "30vh"}}},
               "landscape": {"device": {"left": "41vw"},
                             "panels": {"p1": {"device": {"top": "20vh"}}}}},
    "iphone69": {"device": {"--screen-w": "56vw"}},
}


def test_the_landscape_entry_applies_only_to_a_turned_target():
    assert layout.resolve(PLACEMENT, "iphone", "iphone69", "p1") == {
        "device": {"left": "6vw", "top": "30vh", "--screen-w": "56vw"}}
    assert layout.resolve(PLACEMENT, "iphone", "iphone69", "p1", turned=True) == {
        "device": {"left": "41vw", "top": "20vh", "--screen-w": "56vw"}}


def test_a_target_named_like_its_frame_keeps_the_landscape_entry():
    assert layout.resolve(PLACEMENT, "iphone", "iphone", "p2", turned=True) == {
        "device": {"left": "41vw", "top": "25vh"}}
