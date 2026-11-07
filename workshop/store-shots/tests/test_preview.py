"""`preview`: the layout as it looks now, on placeholder screens and texts
where the raws and the copy are missing, without touching the build."""

from __future__ import annotations

from PIL import Image

PREVIEW = ".store-shots/preview/en"


def _tiles(example, lang: str = "en") -> list[str]:
    with Image.open(example.path(f".store-shots/preview/{lang}/sheet.png")) as sheet:
        return sheet.text["Tiles"].splitlines()


def test_preview_renders_every_panel_on_placeholders_before_any_capture(example):
    example.path("texts/en.yaml").unlink()

    run = example.run("preview")

    assert run.code == 0, run.out + run.err
    assert run.lines[0] == ("preview: ok, 1 image, sheet .store-shots/preview/en/sheet.png;"
                            " placeholders: 1 screen, 1 text")
    assert _tiles(example) == ["iphone69 p1"]
    with Image.open(example.path(f"{PREVIEW}/iphone69-p1.png")) as image:
        assert image.size == (1320, 2868)
    assert not example.path("out").exists()
    assert not example.path("raw").exists()


def test_preview_uses_the_raws_and_copy_once_they_exist_and_leaves_the_build_current(example):
    assert example.run("build").code == 0

    run = example.run("preview")

    assert run.code == 0, run.out + run.err
    assert "placeholders" not in run.lines[0]
    assert not example.path(f"{PREVIEW}/screens").exists()
    assert [line for line in example.run("status").lines if "stale" in line and "nothing" not in line] == []


def test_preview_shows_the_feature_graphic_and_every_target_of_the_full_example(full_example):
    run = full_example.run("preview", "--panel", "p2")

    assert run.code == 0, run.out + run.err
    assert _tiles(full_example) == ["iphone69 p2", "ipad13 p2", "mac p2", "android_phone p2",
                                    "android_tablet p2", "feature graphic"]


def test_preview_names_an_unknown_panel_or_language(example):
    assert example.run("preview", "--panel", "p9").lines[0] == "preview: FAILED, no panel p9; known: p1"
    assert example.run("preview", "--lang", "de").lines[0] == "preview: FAILED, no language de; known: en"


def test_preview_needs_a_storyboard_with_panels(example):
    example.write("storyboard.yaml", "panels: []\n")

    run = example.run("preview")

    assert run.code == 1
    assert run.lines[0] == "preview: FAILED, storyboard.yaml has no panels; the storyboard stage writes them first"
