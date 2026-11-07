"""Unframed images: one raw as captured, with no frame or copy (an in-app
purchase's App Store review screenshot), saved opaque and sRGB into
`out/unframed/<name>.png` by compose and held to the image rules by the
check."""

from __future__ import annotations

import io

import pytest
import yaml
from PIL import Image, ImageCms

from pngs import png
from test_check import NO_ACCOUNT, Store

PANEL = {"en": {"headline": "Every note you take, searchable."},
         "tr": {"headline": "Aldığın her not aranabilir."}}
OUT = "out/unframed/paywall.png"
RAW = "raw/iphone69/en/iphone69-paywall.png"


class Unframed(Store):
    """The example on the App Store (en: en-US, tr: tr), one iPhone target,
    panel p1 on the home scene, and the paywall scene in English as the
    unframed image `paywall`."""

    def __init__(self, example):
        super().__init__(example)
        self.configure(unframed={"paywall": {"scene": "paywall", "target": "iphone69",
                                             "lang": "en"}})
        for lang, panel in PANEL.items():
            self.example.write(f"texts/{lang}.yaml",
                               yaml.safe_dump({"panels": {"p1": panel}}, allow_unicode=True))


@pytest.fixture
def unframed(example) -> Unframed:
    return Unframed(example)


class TestCompose:
    def test_build_saves_the_raw_as_captured_opaque_and_srgb(self, unframed):
        run = unframed.example.run("build")

        assert run.code == 0, run.out + run.err
        assert run.lines[1].startswith("compose: ok, 3 images of 3")
        with Image.open(unframed.example.path(OUT)) as image, \
                Image.open(unframed.example.path(RAW)) as raw:
            assert (image.size, image.mode) == ((1320, 2868), "RGB")
            profile = ImageCms.ImageCmsProfile(io.BytesIO(image.info["icc_profile"]))
            assert "sRGB" in ImageCms.getProfileDescription(profile)
            assert "Copy" not in image.text
            assert image.tobytes() == raw.convert("RGB").tobytes()

    def test_its_scene_is_captured_in_its_language_only(self, unframed):
        assert unframed.example.run("build").code == 0

        assert unframed.example.path(RAW).is_file()
        assert not unframed.example.path("raw/iphone69/tr/iphone69-paywall.png").exists()

    def test_status_names_it_when_its_raw_changed(self, unframed):
        assert unframed.example.run("build").code == 0
        unframed.example.path(RAW).write_bytes(png(copy=None))

        assert f"  {OUT}: raw {RAW} changed" in unframed.example.run("status").lines

    def test_the_sheet_of_its_store_and_language_shows_it(self, unframed):
        assert unframed.example.run("build").code == 0

        for code, tiles in (("en-US", ["iphone69 p1", "unframed paywall"]), ("tr", ["iphone69 p1"])):
            with Image.open(unframed.example.path(f".store-shots/sheets/app_store/{code}.png")) as sheet:
                assert sheet.text["Tiles"].splitlines() == tiles


class TestConfig:
    @pytest.mark.parametrize("entry, problem", [
        ({"scene": "paywall", "target": "ipad13", "lang": "en"},
         "unframed.paywall.target must be one of iphone69"),
        ({"scene": "paywall", "target": "iphone69", "lang": "de"},
         "unframed.paywall.lang must be a language app_store lists: en, tr"),
        ({"target": "iphone69", "lang": "en"},
         "unframed.paywall needs a scene, a target and a lang"),
    ])
    def test_a_bad_entry_is_named(self, unframed, entry, problem):
        unframed.configure(unframed={"paywall": entry})

        assert unframed.example.run("status").lines[0] == f"status: FAILED, store-shots.yaml: {problem}"


class TestRules:
    @pytest.fixture(autouse=True)
    def with_shots(self, unframed):
        unframed.configure(banned_phrases=[NO_ACCOUNT])
        for code in ("en-US", "tr"):
            unframed.shot(f"app_store/{code}/iphone69-p1.png", png())

    def test_an_image_with_no_copy_passes(self, unframed):
        unframed.shot("unframed/paywall.png", png(copy=None))

        assert unframed.problems() == []

    def test_a_missing_one_is_named(self, unframed):
        assert unframed.problems() == [f"image: {OUT}: missing"]

    @pytest.mark.parametrize("data, problem", [
        (png(size=(1206, 2622), copy=None), "1206x2622, expected 1320x2868"),
        (png(color_type=6, copy=None), "has an alpha channel"),
        (png(profile=None, copy=None), "no colour profile, expected sRGB"),
    ])
    def test_one_breaking_an_image_rule_fails(self, unframed, data, problem):
        unframed.shot("unframed/paywall.png", data)

        assert unframed.problems() == [f"image: {OUT}: {problem}"]
