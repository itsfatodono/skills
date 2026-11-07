"""Tests run the real CLI over a temporary copy of the example project."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

import pytest

# No bytecode in the skill folder, from the tests or the CLI they run: it ships as is.
sys.dont_write_bytecode = True

SKILL = Path(__file__).resolve().parents[3] / "plugins" / "fatodono-founderkit" / "skills" / "store-shots"
EXAMPLE = SKILL / "example"
# The engine is not installed; `python -m store_shots` finds it through PYTHONPATH.
ENGINE_PATH = {"PYTHONPATH": os.pathsep.join(filter(None, [str(SKILL / "engine"), os.environ.get("PYTHONPATH")])),
               "PYTHONDONTWRITEBYTECODE": "1"}


@dataclass
class Run:
    code: int
    out: str
    err: str

    @property
    def lines(self) -> list[str]:
        return self.out.splitlines()


class Example:
    def __init__(self, root: Path):
        self.root = root
        self.calls = root.parent / "adapter-calls.jsonl"
        self.env: dict[str, str] = {"FAKE_ADAPTER_CALLS": str(self.calls)}

    def run(self, *args: str) -> Run:
        done = subprocess.run(
            [sys.executable, "-m", "store_shots", *args],
            cwd=self.root, capture_output=True, text=True, env={**os.environ, **ENGINE_PATH, **self.env},
        )
        return Run(done.returncode, done.stdout, done.stderr)

    def path(self, rel: str) -> Path:
        return self.root / rel

    def write(self, rel: str, text: str) -> None:
        self.path(rel).write_text(text, encoding="utf-8")


# The example cut down to one iPhone and one panel, so a test about one image
# renders one; the layout, mockups and adapter stay the example's own.
TRACER = {
    "store-shots.yaml": """# A minimal project: one App Store language, one iPhone target, and the fake
# adapter in place of an app. Paths are relative to this file.
languages:
  en: {app_store: en-US}

targets:
  iphone69: {slot: app_store/iphone_69, size: [1320, 2868]}

# Decides the slots each store requires; without it: iphone, and phone on Play.
runs_on:
  app_store: [iphone]

# Python regular expressions per language, checked in every image's copy.
banned_phrases:
  - says: there is no account
    en: ['(?i)\\bno\\s+account\\b', '(?i)\\bwithout\\s+an?\\s+account\\b']

adapter:
  command: [uv, run, --quiet, --script, adapter/fake_adapter.py]
  inputs: [adapter/**]
""",
    "storyboard.yaml": """panels:
  - id: p1
    claim: Every note can be found by its text.
    scene: home
    status: normal
    evidence:
      - adapter/fake_adapter.py
""",
    "texts/en.yaml": """panels:
  p1:
    headline: Every note you take, searchable.
    subline: Find anything you've noted, in seconds.
""",
}


def copy_example(root: Path) -> Example:
    # Leaves out what a local build of the example wrote.
    built = shutil.ignore_patterns("raw", "out", ".store-shots")
    shutil.copytree(EXAMPLE, root, ignore=built)
    return Example(root)


@pytest.fixture
def example(tmp_path: Path) -> Example:
    """The example as a tracer: one iPhone target, one panel."""
    example = copy_example(tmp_path / "example")
    for rel, text in TRACER.items():
        example.write(rel, text)
    return example


@pytest.fixture
def full_example(tmp_path: Path) -> Example:
    """The whole example: a target per frame kind, a card, a badge, a cluster."""
    return copy_example(tmp_path / "example")
