"""`store-shots check`: the store catalog and the image rules, over images
written byte by byte so each test states exactly what a file holds."""

from __future__ import annotations

import pytest
import yaml

from pngs import IPHONE, png


class Store:
    """The example project reconfigured: App Store languages en (en-US) and tr
    (tr), one panel p1, one iPhone target, and what a test adds."""

    def __init__(self, example):
        self.example = example
        self.config = {
            "languages": {"en": {"app_store": "en-US"}, "tr": {"app_store": "tr"}},
            "targets": {"iphone69": {"slot": "app_store/iphone_69", "size": list(IPHONE)}},
            "adapter": {"command": ["uv", "run", "--quiet", "--script", "adapter/fake_adapter.py"], "inputs": ["adapter/**"]},
        }
        self.save()

    def save(self) -> None:
        self.example.write("store-shots.yaml", yaml.safe_dump(self.config))

    def configure(self, **entries) -> None:
        self.config.update(entries)
        self.save()

    def add_play(self, **targets) -> None:
        """Adds Play (en-US, tr-TR) and [targets] as id = (slot, size)."""
        self.config["languages"]["en"]["play"] = "en-US"
        self.config["languages"]["tr"]["play"] = "tr-TR"
        self.add_targets(**targets)

    def add_targets(self, **targets) -> None:
        self.config["targets"].update(
            {tid: {"slot": slot, "size": list(size)} for tid, (slot, size) in targets.items()})
        self.save()

    def shot(self, rel: str, data: bytes) -> None:
        path = self.example.path("out/" + rel)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)

    def problems(self) -> list[str]:
        """Every problem `check` lists; empty when it passes."""
        run = self.example.run("check")
        log = self.example.path(".store-shots/logs/check.log")
        found = log.read_text(encoding="utf-8").splitlines() if log.is_file() else []
        assert (run.code == 0) == (not found), run.out + run.err
        if found:
            assert run.lines[0].startswith(f"check: FAILED, {found[0]}"), run.out
        else:
            assert run.lines[0].startswith("check: ok"), run.out + run.err
        return found


@pytest.fixture
def store(example) -> Store:
    return Store(example)


def write_iphone_shots(store: Store, en=None, tr=None) -> None:
    store.shot("app_store/en-US/iphone69-p1.png", en or png())
    store.shot("app_store/tr/iphone69-p1.png", tr or png())


class TestImages:
    def test_an_opaque_srgb_screenshot_at_the_target_size_passes(self, store):
        write_iphone_shots(store)

        assert store.problems() == []

    def test_a_screenshot_at_another_size_names_both_sizes(self, store):
        write_iphone_shots(store, en=png(size=(1290, 2796)))

        assert store.problems() == [
            "image: out/app_store/en-US/iphone69-p1.png: 1290x2796, expected 1320x2868"]

    def test_a_screenshot_with_an_alpha_channel_fails(self, store):
        write_iphone_shots(store, tr=png(color_type=6))

        assert store.problems() == ["image: out/app_store/tr/iphone69-p1.png: has an alpha channel"]

    def test_a_grey_and_alpha_screenshot_fails(self, store):
        write_iphone_shots(store, tr=png(color_type=4))

        assert store.problems() == ["image: out/app_store/tr/iphone69-p1.png: has an alpha channel"]

    def test_a_transparency_chunk_counts_as_alpha(self, store):
        write_iphone_shots(store, tr=png(trns=True))

        assert store.problems() == ["image: out/app_store/tr/iphone69-p1.png: has an alpha channel"]

    def test_a_display_p3_screenshot_fails(self, store):
        write_iphone_shots(store, en=png(profile="Display P3"))

        assert store.problems() == [
            "image: out/app_store/en-US/iphone69-p1.png: colour profile is Display P3, not sRGB"]

    def test_an_embedded_srgb_icc_profile_passes(self, store):
        write_iphone_shots(store, en=png(profile="sRGB IEC61966-2.1"))

        assert store.problems() == []

    def test_an_untagged_screenshot_fails(self, store):
        write_iphone_shots(store, en=png(profile=None))

        assert store.problems() == [
            "image: out/app_store/en-US/iphone69-p1.png: no colour profile, expected sRGB"]

    def test_a_file_that_is_not_a_png_fails(self, store):
        write_iphone_shots(store, en=b"\xff\xd8\xff\xe0 a jpeg")

        assert store.problems() == ["image: out/app_store/en-US/iphone69-p1.png: not a PNG"]

    def test_a_language_without_its_screenshot_is_named(self, store):
        store.shot("app_store/en-US/iphone69-p1.png", png())

        assert store.problems() == ["image: out/app_store/tr/iphone69-p1.png: missing"]

    def test_every_problem_is_logged_and_the_console_names_the_first(self, store):
        run = store.example.run("check")

        assert run.code == 1
        assert run.lines == [
            "check: FAILED, image: out/app_store/en-US/iphone69-p1.png: missing (+1 more) "
            "(log: .store-shots/logs/check.log)",
            "exit 1",
        ]
        assert store.example.path(".store-shots/logs/check.log").read_text(encoding="utf-8").splitlines() == [
            "image: out/app_store/en-US/iphone69-p1.png: missing",
            "image: out/app_store/tr/iphone69-p1.png: missing",
        ]


TEAPOT_TARGETS = {
    "ipad13": ("app_store/ipad_13", (2064, 2752)),
    "android_phone": ("play/phone", (1440, 2560)),
    "android_tablet": ("play/tablet_10", (1800, 3200)),
}


class TestCatalog:
    def test_every_target_is_checked_at_its_own_size(self, store):
        store.add_play(**TEAPOT_TARGETS)
        write_iphone_shots(store)
        for lang in ("en-US", "tr"):
            store.shot(f"app_store/{lang}/ipad13-p1.png", png(size=(2064, 2752)))
        for lang in ("en-US", "tr-TR"):
            store.shot(f"play/{lang}/android_phone-p1.png", png(size=(1440, 2560)))
        store.shot("play/en-US/android_tablet-p1.png", png(size=(1800, 3200)))
        store.shot("play/tr-TR/android_tablet-p1.png", png(size=(1080, 1920)))

        assert store.problems() == [
            "image: out/play/tr-TR/android_tablet-p1.png: 1080x1920, expected 1800x3200"]

    def test_a_target_at_a_size_its_slot_does_not_list_fails(self, store):
        store.add_targets(iphone69=("app_store/iphone_69", (1290, 2797)))
        write_iphone_shots(store, en=png(size=(1290, 2797)), tr=png(size=(1290, 2797)))

        assert store.problems() == [
            "catalog: store-shots.yaml: targets.iphone69 is 1290x2797, app_store/iphone_69 takes "
            "1320x2868, 1290x2796, 1260x2736 (or turned to landscape)"]

    def test_every_listed_size_of_a_slot_is_taken(self, store):
        store.add_targets(iphone69=("app_store/iphone_69", (1290, 2796)))
        write_iphone_shots(store, en=png(size=(1290, 2796)), tr=png(size=(1290, 2796)))

        assert store.problems() == []

    def test_a_listed_size_turned_to_landscape_is_taken(self, store):
        store.add_targets(iphone69=("app_store/iphone_69", (2868, 1320)))
        write_iphone_shots(store, en=png(size=(2868, 1320)), tr=png(size=(2868, 1320)))

        assert store.problems() == []

    def test_a_mac_screenshot_turned_to_portrait_fails(self, store):
        store.add_targets(mac=("app_store/mac", (1800, 2880)))
        write_iphone_shots(store)
        for lang in ("en-US", "tr"):
            store.shot(f"app_store/{lang}/mac-p1.png", png(size=(1800, 2880)))

        assert store.problems() == [
            "catalog: store-shots.yaml: targets.mac is 1800x2880, app_store/mac takes "
            "2880x1800, 2560x1600, 1440x900, 1280x800"]

    def test_a_play_phone_at_16_9_is_taken(self, store):
        store.add_play(android_phone=("play/phone", (2560, 1440)))

        assert not [p for p in store.problems() if p.startswith("catalog:")]

    @pytest.mark.parametrize("size", [(1440, 2561), (720, 1280), (1280, 720), (2561, 1440)])
    def test_a_play_phone_outside_9_16_from_1080_to_3840_fails(self, store, size):
        store.add_play(android_phone=("play/phone", size))

        assert (f"catalog: store-shots.yaml: targets.android_phone is {size[0]}x{size[1]}, "
                "play/phone takes 9:16 with sides from 1080 to 3840 (or turned to landscape)"
                ) in store.problems()

    def test_a_screen_turned_unlike_its_targets_size_fails(self, store):
        store.config["targets"]["iphone69"].update(size=[2868, 1320], screen=[1320, 2868])
        store.save()

        run = store.example.run("check")

        assert run.code == 1
        assert run.lines[0] == ("check: FAILED, store-shots.yaml: targets.iphone69: screen and size"
                                " must both be portrait or both landscape (width first)")

    def test_a_slot_the_catalog_does_not_list_fails(self, store):
        store.add_targets(iphone_old=("app_store/iphone_47", (750, 1334)))

        run = store.example.run("check")

        assert run.code == 1
        assert run.lines[0].startswith(
            "check: FAILED, store-shots.yaml: targets.iphone_old.slot must be one of app_store/iphone_69,")

    def test_the_app_store_without_an_iphone_slot_names_the_slot(self, store):
        store.config["targets"] = {"ipad13": {"slot": "app_store/ipad_13", "size": [2064, 2752]}}
        store.save()
        for lang in ("en-US", "tr"):
            store.shot(f"app_store/{lang}/ipad13-p1.png", png(size=(2064, 2752)))

        assert store.problems() == [
            "catalog: store-shots.yaml: app_store requires a target for iphone "
            "(slot app_store/iphone_69 or app_store/iphone_65)"]

    def test_the_older_large_iphone_slot_also_fills_the_requirement(self, store):
        store.config["targets"] = {"iphone65": {"slot": "app_store/iphone_65", "size": [1284, 2778]}}
        store.save()
        for lang in ("en-US", "tr"):
            store.shot(f"app_store/{lang}/iphone65-p1.png", png(size=(1284, 2778)))

        assert store.problems() == []

    def test_an_app_that_runs_on_ipad_and_mac_needs_those_slots(self, store):
        store.configure(runs_on={"app_store": ["iphone", "ipad", "mac"]})
        write_iphone_shots(store)

        assert store.problems() == [
            "catalog: store-shots.yaml: app_store requires a target for ipad (slot app_store/ipad_13)",
            "catalog: store-shots.yaml: app_store requires a target for mac (slot app_store/mac)",
        ]

    def test_play_without_a_phone_slot_fails(self, store):
        store.add_play(android_tablet=TEAPOT_TARGETS["android_tablet"])
        write_iphone_shots(store)
        for lang in ("en-US", "tr-TR"):
            store.shot(f"play/{lang}/android_tablet-p1.png", png(size=(1800, 3200)))

        assert store.problems() == [
            "catalog: store-shots.yaml: play requires a target for phone (slot play/phone)"]

    def test_more_panels_than_a_store_takes_fails(self, store):
        panels = [{"id": f"p{i}", "scene": "home", "evidence": ["adapter/fake_adapter.py"]}
                  for i in range(1, 12)]
        store.example.write("storyboard.yaml", yaml.safe_dump({"panels": panels}))

        assert ("catalog: store-shots.yaml: targets.iphone69 gets 11 panels, app_store/iphone_69 "
                "takes at most 10") in store.problems()


def write_phone_shots(store: Store, en=None, tr=None) -> None:
    store.shot("play/en-US/android_phone-p1.png", en or png(size=(1440, 2560)))
    store.shot("play/tr-TR/android_phone-p1.png", tr or png(size=(1440, 2560)))


class TestImageCopy:
    @pytest.fixture(autouse=True)
    def with_play(self, store):
        store.add_play(android_phone=TEAPOT_TARGETS["android_phone"])
        write_iphone_shots(store)
        write_phone_shots(store)

    def test_app_store_images_whose_copy_names_only_apple_platforms_pass(self, store):
        write_iphone_shots(store, en=png(copy="Notes everywhere.\niPhone · iPad · Mac\nTeapot Notes"),
                           tr=png(copy="Notların her yerde.\niPhone · iPad · Mac"))

        assert store.problems() == []

    @pytest.mark.parametrize("named, copy", [
        ("Android", "Notes everywhere.\nAndroid · iPhone · iPad"),
        ("Windows", "Notes everywhere.\nMac and Windows"),
        ("Linux, Chromebook", "Runs on Linux and a Chromebook"),
        ("Google Play", "Also on Google Play"),
        ("Play Store", "Rated 5 stars on the Play Store"),
    ])
    def test_an_app_store_image_whose_copy_names_another_platform_fails(self, store, named, copy):
        write_iphone_shots(store, en=png(copy=copy))

        assert store.problems() == [
            f"image: out/app_store/en-US/iphone69-p1.png: its copy names another platform ({named})"]

    def test_playing_a_recording_is_not_a_platform_name(self, store):
        write_iphone_shots(store, en=png(copy="Play back every recording.\nplay, pause, seek"))

        assert store.problems() == []

    def test_turkish_copy_is_read_as_utf8(self, store):
        write_iphone_shots(store, tr=png(copy="Notların her yerde.\nAndroid tablette ve iPad'de"))

        assert store.problems() == [
            "image: out/app_store/tr/iphone69-p1.png: its copy names another platform (Android)"]

    def test_an_app_store_image_that_does_not_record_its_copy_fails(self, store):
        write_iphone_shots(store, tr=png(copy=None))

        assert store.problems() == [
            "image: out/app_store/tr/iphone69-p1.png: records no copy, so its text cannot be checked"]

    def test_play_images_may_name_every_platform(self, store):
        write_phone_shots(store, en=png(size=(1440, 2560),
                                        copy="Android phone, Android tablet, iPhone, iPad, Mac"),
                          tr=png(size=(1440, 2560), copy=None))

        assert store.problems() == []


NO_ACCOUNT = {
    "says": "there is no account",
    "en": [r"\b(?:[Nn]o|NO)\s+(?:[A-Z]\w*\s+){0,3}(?:accounts?|ACCOUNTS?)\b",
           r"(?i)\bwithout\s+(?:an?\s+)?accounts?\b"],
    "tr": [r"(?i)\bhesa[pb]\w*\s+(?:yok|gerekmez|gerektirmez|istemez|olmadan)\b", r"(?i)\bhesapsız"],
}


class TestBannedPhrases:
    @pytest.fixture(autouse=True)
    def with_play(self, store):
        store.add_play(android_phone=TEAPOT_TARGETS["android_phone"])
        store.configure(banned_phrases=[NO_ACCOUNT])
        write_iphone_shots(store)
        write_phone_shots(store)

    @pytest.mark.parametrize("copy", [
        "There's no Teapot Notes account, and our servers never receive your notes.",
        "No account needed.",
        "Works without an account.",
    ])
    def test_an_english_banned_phrase_fails_in_an_app_store_image(self, store, copy):
        write_iphone_shots(store, en=png(copy=copy))

        assert store.problems() == [
            "image: out/app_store/en-US/iphone69-p1.png: its copy says there is no account"]

    @pytest.mark.parametrize("copy", [
        "Teapot Notes hesabı yok, notların sunucularımıza hiç gelmez.",
        "Hesap yok.",
        "Hesap gerekmez.",
        "Hesapsız çalışır.",
    ])
    def test_a_turkish_banned_phrase_fails_in_a_play_image(self, store, copy):
        write_phone_shots(store, tr=png(size=(1440, 2560), copy=copy))

        assert store.problems() == [
            "image: out/play/tr-TR/android_phone-p1.png: its copy says there is no account"]

    def test_signing_in_to_an_account_is_not_a_banned_phrase(self, store):
        write_iphone_shots(store, en=png(
            copy="No card and no sign-up. Buying needs only an email sign-in to your account."))

        assert store.problems() == []

    def test_a_phrase_is_checked_only_in_its_own_language(self, store):
        write_iphone_shots(store, en=png(copy="Hesap yok."), tr=png(copy="No account needed."))

        assert store.problems() == []

    def test_an_image_without_recorded_copy_cannot_be_checked(self, store):
        write_phone_shots(store, en=png(size=(1440, 2560), copy=None))

        assert store.problems() == [
            "image: out/play/en-US/android_phone-p1.png: records no copy, so its text cannot be checked"]

    def test_a_bad_pattern_names_its_entry(self, store):
        store.configure(banned_phrases=[{"says": "x", "en": ["(unclosed"]}])

        run = store.example.run("check")

        assert run.code == 1
        assert run.lines[0].startswith("check: FAILED, store-shots.yaml: banned_phrases[0].en: bad pattern")


class TestStoryboardEvidence:
    def _evidence(self, store, *evidence) -> None:
        panel = {"id": "p1", "claim": "Every note can be found by its text.", "scene": "home"}
        if evidence:
            panel["evidence"] = list(evidence)
        store.example.write("storyboard.yaml", yaml.safe_dump({"panels": [panel]}))
        write_iphone_shots(store)

    def test_evidence_naming_files_and_symbols_that_exist_passes(self, store):
        self._evidence(store, "adapter/fake_adapter.py", "adapter/fake_adapter.py#png")

        assert store.problems() == []

    def test_a_panel_without_evidence_fails(self, store):
        self._evidence(store)

        assert store.problems() == ["storyboard: storyboard.yaml: panel p1 has no evidence"]

    def test_evidence_naming_a_missing_file_fails(self, store):
        self._evidence(store, "adapter/fake_adapter.py", "lib/gone.dart#Engine.run")

        assert store.problems() == [
            "storyboard: storyboard.yaml: panel p1 evidence lib/gone.dart#Engine.run: no file "
            "lib/gone.dart"]


def test_build_fails_at_the_check_when_its_copy_breaks_a_rule(example):
    config = yaml.safe_load(example.path("store-shots.yaml").read_text(encoding="utf-8"))
    config["banned_phrases"] = [{"says": "every note is searchable", "en": ["(?i)searchable"]}]
    example.write("store-shots.yaml", yaml.safe_dump(config))

    run = example.run("build")

    assert run.code == 1
    assert [line.split(":")[0] for line in run.lines] == ["capture", "compose", "check", "exit 1"]
    assert run.lines[2].startswith("check: FAILED, image: out/app_store/en-US/iphone69-p1.png: "
                                   "its copy says every note is searchable")
