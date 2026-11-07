"""`store-shots init`: a new project from the example, which builds once the
storyboard, the copy and the adapter are written."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pytest
import yaml

from conftest import EXAMPLE, TRACER, Example
from store_shots import catalog
from store_shots.init import parse_runs_on, targets_for

BOTH_STORES = ["--runs-on", "app_store=iphone,mac", "--runs-on", "play=phone", "--lang", "en=en-US"]


@pytest.fixture
def folder(tmp_path: Path) -> Example:
    (tmp_path / "app").mkdir()
    return Example(tmp_path / "app")


def config(folder: Example) -> dict:
    return yaml.safe_load(folder.path("store-shots.yaml").read_text(encoding="utf-8"))


def test_init_gives_each_device_the_examples_target(folder):
    run = folder.run("init", *BOTH_STORES)

    assert run.code == 0, run.out
    assert run.lines[0] == "init: ok, 11 files written, 3 targets: iphone69, mac, android_phone"
    example = yaml.safe_load((EXAMPLE / "store-shots.yaml").read_text(encoding="utf-8"))["targets"]
    written = config(folder)
    assert written["targets"] == {t: example[t] for t in ("iphone69", "mac", "android_phone")}
    assert written["runs_on"] == {"app_store": ["iphone", "mac"], "play": ["phone"]}
    assert written["languages"] == {"en": {"app_store": "en-US", "play": "en-US"}}
    assert written["feature_graphic"] == {"size": list(catalog.FEATURE_GRAPHIC_SIZE)}
    assert "paths" not in written
    assert folder.path("texts/en.yaml").is_file()


def test_init_writes_the_copy_files_where_copy_names_and_records_it(folder):
    run = folder.run("init", *BOTH_STORES, "--copy", "../store-texts/")

    assert run.code == 0, run.out
    assert config(folder)["paths"] == {"copy": "../store-texts"}
    assert (folder.root.parent / "store-texts/en.yaml").is_file()
    assert not folder.path("copy").exists()


def test_init_writes_nothing_when_a_copy_file_beside_the_project_exists(folder):
    (folder.root.parent / "store-texts").mkdir(parents=True)
    (folder.root.parent / "store-texts/en.yaml").write_text("panels: {}\n", encoding="utf-8")

    run = folder.run("init", *BOTH_STORES, "--copy", "../store-texts")

    assert run.lines[0] == "init: FAILED, ../store-texts/en.yaml exists; init writes only into" \
                           " a folder without a project"
    assert list(folder.root.iterdir()) == []


def test_every_device_a_store_lists_has_a_target_in_the_example():
    runs_on = [f"{store}={','.join(catalog.devices(store))}" for store in catalog.STORES]

    targets = targets_for(parse_runs_on(runs_on))

    assert len(targets) == sum(len(catalog.devices(store)) for store in catalog.STORES)


def test_the_placement_holds_the_examples_entries_for_the_projects_frames(folder):
    folder.run("init", *BOTH_STORES)

    example = yaml.safe_load((EXAMPLE / "layout" / "placement.yaml").read_text(encoding="utf-8"))
    placement = yaml.safe_load(folder.path("layout/placement.yaml").read_text(encoding="utf-8"))
    assert placement == {frame: example[frame] for frame in ("iphone", "mac", "android_phone")}


def test_a_play_only_project_gets_only_the_placement_of_its_frames(folder):
    folder.run("init", "--runs-on", "play=phone,tablet", "--lang", "en=en-US")

    placement = yaml.safe_load(folder.path("layout/placement.yaml").read_text(encoding="utf-8"))
    assert sorted(placement) == ["android_phone", "android_tablet"]


def test_the_examples_phone_and_tablet_frames_have_landscape_placement():
    example = yaml.safe_load((EXAMPLE / "layout" / "placement.yaml").read_text(encoding="utf-8"))

    turning = {slot.frame for slot in catalog.SLOTS.values() if slot.turns}
    assert {frame for frame, entry in example.items() if "landscape" in entry} == turning


def test_an_app_store_only_project_gets_no_feature_graphic(folder):
    folder.run("init", "--runs-on", "app_store=iphone", "--lang", "en=en-US")

    assert "feature_graphic" not in config(folder)
    assert not folder.path("layout/feature.html").exists()
    assert folder.path("layout/panel.html").read_text(encoding="utf-8") == (EXAMPLE / "layout/panel.html").read_text(encoding="utf-8")


def test_init_writes_nothing_into_a_folder_with_a_project(folder):
    folder.write("storyboard.yaml", "panels: []\n")

    run = folder.run("init", *BOTH_STORES)

    assert run.code == 1
    assert run.lines[0] == "init: FAILED, storyboard.yaml exists; init writes only into a" \
                           " folder without a project"
    assert sorted(p.name for p in folder.root.iterdir()) == ["storyboard.yaml"]


@pytest.mark.parametrize("args, reason", [
    (["--runs-on", "play=watch", "--lang", "en=en-US"], "--runs-on play=watch: play devices are phone, tablet"),
    (["--runs-on", "steam=pc", "--lang", "en=en-US"], "--runs-on steam=pc: stores are app_store, play"),
    (["--lang", "en=en-US"], "--runs-on is required, once per store"),
    (["--runs-on", "play=phone", "--lang", "en"], "--lang en: write it as <copy language>=<store code>, en=en-US"),
])
def test_a_wrong_argument_names_what_init_takes(folder, args, reason):
    run = folder.run("init", *args)

    assert run.lines[0] == f"init: FAILED, {reason}"


def test_the_starter_adapter_fails_until_its_capture_is_written(folder):
    folder.run("init", "--runs-on", "app_store=iphone", "--lang", "en=en-US")
    folder.write("storyboard.yaml", TRACER["storyboard.yaml"])
    folder.write("texts/en.yaml", TRACER["texts/en.yaml"])

    run = folder.run("build")

    assert run.lines[0].startswith("capture: FAILED, iphone69: adapter exited 1")
    assert "the capture is not written yet" in folder.path(".store-shots/logs/capture-iphone69.log").read_text(encoding="utf-8")


@pytest.mark.parametrize("copy", ["texts", "../store-texts"])
def test_a_new_project_builds_once_its_storyboard_copy_and_adapter_are_written(folder, copy):
    folder.run("init", *BOTH_STORES, "--copy", copy)
    shutil.copy(EXAMPLE / "adapter" / "fake_adapter.py", folder.path("adapter/fake_adapter.py"))
    folder.write("store-shots.yaml", folder.path("store-shots.yaml").read_text(encoding="utf-8").replace(
        "adapter/adapter.py]", "adapter/fake_adapter.py]"))
    folder.write("storyboard.yaml", TRACER["storyboard.yaml"])
    folder.write(f"{copy}/en.yaml", TRACER["texts/en.yaml"]
                 + "feature_graphic:\n  wordmark: example.\n  headline: Every note, searchable.\n")

    run = folder.run("build")

    assert run.code == 0, run.out
    assert folder.path("out/app_store/en-US/mac-p1.png").is_file()
    assert folder.path("out/play/en-US/feature-graphic.png").is_file()


def test_git_ignores_the_work_and_log_folder_and_keeps_the_rest(folder):
    folder.run("init", *BOTH_STORES)
    subprocess.run(["git", "init", "-q"], cwd=folder.root, check=True)

    ignored = subprocess.run(["git", "check-ignore", ".store-shots/logs/capture.log", "raw/x.png",
                              "store-shots.yaml"], cwd=folder.root, capture_output=True, text=True)

    assert ignored.stdout.splitlines() == [".store-shots/logs/capture.log"]
