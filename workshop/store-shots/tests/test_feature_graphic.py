"""The Play feature graphic: rendered by compose per Play language into
`out/play/<code>/feature-graphic.png` when the config asks for one, and held
to the image rules by the check."""

from __future__ import annotations

import io

import pytest
import yaml
from PIL import Image, ImageCms

from pngs import png
from test_check import NO_ACCOUNT, Store

PANEL = {"en": {"headline": "Every note you take, searchable."},
         "tr": {"headline": "Aldığın her not aranabilir."}}
FEATURE = {"en": {"wordmark": "example.", "headline": "Every note you take, searchable."},
           "tr": {"wordmark": "example.", "headline": "Aldığın her not aranabilir."}}
GRAPHIC = {"en": "out/play/en-US/feature-graphic.png", "tr": "out/play/tr-TR/feature-graphic.png"}


class Graphic(Store):
    """The example on both stores (en: en-US / en-US, tr: tr / tr-TR), one
    iPhone target, no Play device required, and a feature graphic per Play
    language."""

    def __init__(self, example):
        super().__init__(example)
        self.config["languages"]["en"]["play"] = "en-US"
        self.config["languages"]["tr"]["play"] = "tr-TR"
        self.configure(runs_on={"app_store": ["iphone"], "play": []},
                       feature_graphic={"size": [1024, 500]})
        self.copy = {lang: {"panels": {"p1": PANEL[lang]}, "feature_graphic": dict(FEATURE[lang])}
                     for lang in PANEL}
        self.save_copy()

    def save_copy(self) -> None:
        for lang, copy in self.copy.items():
            self.example.write(f"texts/{lang}.yaml", yaml.safe_dump(copy, allow_unicode=True))

    def write_iphone_shots(self) -> None:
        for code in ("en-US", "tr"):
            self.shot(f"app_store/{code}/iphone69-p1.png", png())


@pytest.fixture
def graphic(example) -> Graphic:
    return Graphic(example)


class TestCompose:
    def test_build_renders_one_per_play_language_into_out(self, graphic):
        run = graphic.example.run("build")

        assert run.code == 0, run.out + run.err
        assert run.lines[1].startswith("compose: ok, 4 images of 4")
        for lang, out in GRAPHIC.items():
            with Image.open(graphic.example.path(out)) as image:
                assert image.size == (1024, 500)
                assert image.mode == "RGB"
                profile = ImageCms.ImageCmsProfile(io.BytesIO(image.info["icc_profile"]))
                assert "sRGB" in ImageCms.getProfileDescription(profile)
                assert image.text["Copy"].splitlines() == [FEATURE[lang]["wordmark"],
                                                           FEATURE[lang]["headline"]]
        assert not graphic.example.path("out/app_store/en-US/feature-graphic.png").exists()

    def test_a_second_build_renders_nothing_and_a_changed_headline_one(self, graphic):
        assert graphic.example.run("build").code == 0
        en = graphic.example.path(GRAPHIC["en"]).stat().st_mtime_ns

        assert graphic.example.run("build").lines[1] == "compose: ok, nothing stale (4 images current)"
        graphic.copy["tr"]["feature_graphic"]["headline"] = "Her not aranabilir."
        graphic.save_copy()
        status = graphic.example.run("status").lines
        assert "  out/play/tr-TR/feature-graphic.png: copy tr feature_graphic changed" in status
        assert not any("en-US/feature-graphic.png" in line for line in status)

        assert graphic.example.run("build").lines[1].startswith("compose: ok, 1 image of 4")
        assert graphic.example.path(GRAPHIC["en"]).stat().st_mtime_ns == en

    def test_without_the_config_entry_no_feature_graphic_is_made(self, graphic):
        del graphic.config["feature_graphic"]
        graphic.save()

        run = graphic.example.run("build")

        assert run.code == 0, run.out + run.err
        assert run.lines[1].startswith("compose: ok, 2 images of 2")
        assert not graphic.example.path("out/play").exists()

    def test_a_feature_page_text_missing_from_the_copy_fails(self, graphic):
        graphic.write_iphone_shots()
        del graphic.copy["tr"]["feature_graphic"]["headline"]
        graphic.save_copy()

        assert graphic.example.run("build").lines[1] == (
            "compose: FAILED, texts/tr.yaml: feature_graphic.headline missing")
        assert "copy: texts/tr.yaml: feature_graphic.headline missing" in graphic.problems()

    def test_a_feature_graphic_size_play_does_not_take_fails(self, graphic):
        graphic.configure(feature_graphic={"size": [1024, 512]})

        assert ("catalog: store-shots.yaml: feature_graphic.size is 1024x512, play takes 1024x500"
                in graphic.problems())

    def test_a_feature_graphic_needs_a_play_language(self, graphic):
        for codes in graphic.config["languages"].values():
            del codes["play"]
        graphic.save()

        assert graphic.example.run("check").lines[0] == (
            "check: FAILED, store-shots.yaml: feature_graphic is Play's; no language lists play")


def write_graphics(graphic: Graphic, en: bytes | None = None, tr: bytes | None = None) -> None:
    """Writes each feature graphic into `out/`; a language given None gets a good one."""
    for lang, data in (("en", en), ("tr", tr)):
        data = data or png(size=(1024, 500), copy="\n".join(FEATURE[lang].values()))
        path = graphic.example.path(GRAPHIC[lang])
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)


class TestRules:
    @pytest.fixture(autouse=True)
    def with_text(self, graphic):
        graphic.configure(banned_phrases=[NO_ACCOUNT])
        graphic.write_iphone_shots()

    def test_a_feature_graphic_per_play_language_passes(self, graphic):
        write_graphics(graphic)

        assert graphic.problems() == []

    def test_a_missing_feature_graphic_is_named(self, graphic):
        write_graphics(graphic)
        graphic.example.path(GRAPHIC["tr"]).unlink()

        assert graphic.problems() == ["image: out/play/tr-TR/feature-graphic.png: missing"]

    @pytest.mark.parametrize("data, problem", [
        (png(size=(1024, 512), copy="x"), "1024x512, expected 1024x500"),
        (png(size=(1024, 500), color_type=6, copy="x"), "has an alpha channel"),
        (png(size=(1024, 500), profile=None, copy="x"), "no colour profile, expected sRGB"),
        (png(size=(1024, 500), copy="example.\nNo account needed."), "its copy says there is no account"),
    ])
    def test_a_feature_graphic_breaking_an_image_rule_fails(self, graphic, data, problem):
        write_graphics(graphic, en=data)

        assert graphic.problems() == [f"image: out/play/en-US/feature-graphic.png: {problem}"]
