"""`store-shots build`: capture through the adapter, compose, check."""

from __future__ import annotations

import io
import os
import subprocess
from pathlib import Path

import pytest
from PIL import Image, ImageCms

from conftest import SKILL

PANEL = "out/app_store/en-US/iphone69-p1.png"


def test_build_writes_the_panel_at_the_store_size_opaque_and_srgb(example):
    run = example.run("build")

    assert run.code == 0, run.out + run.err
    with Image.open(example.path(PANEL)) as image:
        assert image.format == "PNG"
        assert image.size == (1320, 2868)
        assert image.mode == "RGB"
        assert "transparency" not in image.info
        profile = ImageCms.ImageCmsProfile(io.BytesIO(image.info["icc_profile"]))
        assert "sRGB" in ImageCms.getProfileDescription(profile)
        assert image.text["Copy"].splitlines() == [
            "Every note you take, searchable.",
            "Find anything you've noted, in seconds.",
        ]


@pytest.mark.parametrize("env, reason", [
    ({"FAKE_ADAPTER_OMIT": "home"}, "en/iphone69-home.png missing"),
    ({"FAKE_ADAPTER_SIZE": "1290x2796"}, "en/iphone69-home.png is 1290x2796, expected 1320x2868"),
    ({"FAKE_ADAPTER_REPORT": "en/iphone69-home.png: 'Settings' shows 7 of 8 characters"},
     "report: en/iphone69-home.png: 'Settings' shows 7 of 8 characters"),
])
def test_a_raw_breaking_the_adapter_contract_fails_before_compose(example, env, reason):
    example.env.update(env)

    run = example.run("build")

    assert run.code != 0
    assert len(run.lines) == 2
    assert run.lines[0].startswith("capture: FAILED, iphone69: " + reason)
    assert run.lines[1] == f"exit {run.code}"
    assert not example.path(PANEL).exists()
    assert not example.path("raw").exists()


INK = (27, 27, 27)
ACCENT = (223, 79, 79)
# The example layout's headline starts at 7vh with 9.6vw type at 1.08 line
# height: two lines end near y = 480; the device starts at 25vh (y = 717).
TWO_LINES_END, DEVICE_TOP = 500, 700


def _rows_with(image, colour, top, bottom, tolerance=24):
    pixels = image.load()
    return [y for y in range(top, bottom)
            if any(all(abs(c - k) <= tolerance for c, k in zip(pixels[x, y], colour))
                   for x in range(0, image.width, 2))]


def test_a_long_headline_shrinks_to_two_lines_above_the_device(example):
    example.write("texts/en.yaml", "panels:\n  p1:\n    headline: Every note you take, in every"
                  " notebook and every folder, searchable in seconds.\n")

    assert example.run("build").code == 0
    with Image.open(example.path(PANEL)) as image:
        assert _rows_with(image, INK, 0, TWO_LINES_END)
        assert not _rows_with(image, INK, TWO_LINES_END, DEVICE_TOP)


@pytest.mark.parametrize("headline, accent", [("Searchable.", True), ("Searchable", False)])
def test_a_closing_full_stop_takes_the_accent_colour(example, headline, accent):
    example.write("texts/en.yaml", f"panels:\n  p1:\n    headline: {headline}\n")

    assert example.run("build").code == 0
    with Image.open(example.path(PANEL)) as image:
        assert bool(_rows_with(image, ACCENT, 0, DEVICE_TOP, tolerance=12)) == accent


def test_the_entry_script_runs_the_same_build_through_uv(example):
    entry = SKILL / "bin" / "store-shots.py"
    done = subprocess.run(["uv", "run", "--quiet", "--script", str(entry), "build"],
                          cwd=example.root, capture_output=True, text=True,
                          env={**os.environ, **example.env})

    assert done.returncode == 0, done.stdout + done.stderr
    assert done.stdout.splitlines()[-1] == "exit 0"
    assert example.path(PANEL).is_file()


def test_the_console_shows_one_line_per_stage_and_the_logs_hold_the_rest(example):
    run = example.run("build")

    assert [line.split(":")[0] for line in run.lines] == ["capture", "compose", "check", "sheet", "exit 0"]
    assert "booting" not in run.out + run.err
    assert "pumping home in en" in example.path(".store-shots/logs/capture-iphone69.log").read_text(encoding="utf-8")
    assert example.path(".store-shots/logs/compose.log").is_file()
