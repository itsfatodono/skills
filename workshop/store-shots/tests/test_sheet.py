"""Contact sheets: one downscaled image per store and language holding every
panel of every target, labelled, for review in one look."""

from __future__ import annotations

import pytest
from PIL import Image

SHEET = ".store-shots/sheets/app_store/{code}.png"


def _add_language(example) -> None:
    config = example.path("store-shots.yaml").read_text(encoding="utf-8")
    example.write("store-shots.yaml", config.replace(
        "  en: {app_store: en-US}\n", "  en: {app_store: en-US}\n  tr: {app_store: tr}\n"))
    example.write("texts/tr.yaml", "panels:\n  p1:\n    headline: Her not aranabilir.\n")


def _sheet(example, code: str = "en-US") -> Image.Image:
    with Image.open(example.path(SHEET.format(code=code))) as image:
        image.load()
        return image


def test_build_writes_a_sheet_per_store_and_language(example):
    _add_language(example)

    run = example.run("build")

    assert run.code == 0, run.out + run.err
    assert [line.split(":")[0] for line in run.lines] == ["capture", "compose", "check", "sheet", "exit 0"]
    for code in ("en-US", "tr"):
        sheet = _sheet(example, code)
        assert sheet.mode == "RGB"
        assert sheet.text["Tiles"].splitlines() == ["iphone69 p1"]


def _add_target_and_panel(example) -> None:
    config = example.path("store-shots.yaml").read_text(encoding="utf-8")
    example.write("store-shots.yaml", config.replace(
        "  iphone69: {slot: app_store/iphone_69, size: [1320, 2868]}\n",
        "  iphone69: {slot: app_store/iphone_69, size: [1320, 2868]}\n"
        "  iphone65: {slot: app_store/iphone_69, size: [1290, 2796]}\n"))
    storyboard = example.path("storyboard.yaml").read_text(encoding="utf-8")
    example.write("storyboard.yaml", storyboard + "  - id: p2\n    claim: Notes sync.\n    scene: sync\n"
                  "    evidence: [adapter/fake_adapter.py]\n")
    example.write("texts/en.yaml", "panels:\n  p1:\n    headline: Searchable.\n"
                  "  p2:\n    headline: Synced.\n")


def test_each_tile_is_labelled_with_device_and_panel_in_storyboard_order(example):
    _add_target_and_panel(example)

    assert example.run("build").code == 0
    sheet = _sheet(example)
    assert sheet.text["Tiles"].splitlines() == [
        "iphone69 p1", "iphone69 p2", "iphone65 p1", "iphone65 p2"]
    assert max(sheet.size) <= 1600


def _many_panels(example, count: int) -> None:
    """Grows the storyboard to [count] panels whose images copy p1's, so
    `sheet` has them without a compose per panel."""
    panel = example.path("out/app_store/en-US/iphone69-p1.png").read_bytes()
    lines = ["panels:"]
    for n in range(1, count + 1):
        lines += [f"  - id: p{n}", f"    claim: Claim {n}.", "    scene: home",
                  "    evidence: [adapter/fake_adapter.py]"]
        example.path(f"out/app_store/en-US/iphone69-p{n}.png").write_bytes(panel)
    example.write("storyboard.yaml", "\n".join(lines) + "\n")


@pytest.mark.parametrize("count", [1, 7, 40])
def test_the_sheet_stays_under_the_long_side_limit_whatever_the_panel_count(example, count):
    assert example.run("build").code == 0
    _many_panels(example, count)

    run = example.run("sheet")

    assert run.code == 0, run.out + run.err
    assert run.lines[0].startswith("sheet: ok, ")
    sheet = _sheet(example)
    assert len(sheet.text["Tiles"].splitlines()) == count
    assert max(sheet.size) <= 1600


def test_a_sheet_is_rewritten_only_when_one_of_its_images_changed(example):
    assert example.run("build").code == 0
    sheet = example.path(SHEET.format(code="en-US"))
    before = sheet.read_bytes()

    unchanged = example.run("sheet")
    assert unchanged.lines[0].startswith("sheet: ok, 0 sheets written, 1 up to date")
    assert sheet.read_bytes() == before

    panel = example.path("out/app_store/en-US/iphone69-p1.png")
    with Image.open(panel) as image:
        image.convert("RGB").transpose(Image.Transpose.FLIP_TOP_BOTTOM).save(panel)
    changed = example.run("sheet")
    assert changed.lines[0].startswith("sheet: ok, 1 sheet written, 0 up to date")
    assert sheet.read_bytes() != before


def test_the_play_sheet_also_shows_the_feature_graphic(full_example):
    assert full_example.run("build").code == 0

    with Image.open(full_example.path(".store-shots/sheets/play/en-US.png")) as play:
        assert play.text["Tiles"].splitlines()[-1] == "feature graphic"
    with Image.open(full_example.path(".store-shots/sheets/app_store/en-US.png")) as app_store:
        assert "feature graphic" not in app_store.text["Tiles"].splitlines()


def test_sheet_without_composed_images_names_the_missing_one(example):
    run = example.run("sheet")

    assert run.code == 1
    assert run.lines == ["sheet: FAILED, out/app_store/en-US/iphone69-p1.png missing; run build",
                         "exit 1"]
