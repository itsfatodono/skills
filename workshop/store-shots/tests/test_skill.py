"""The skill is the agent skill `store-shots`, and what it names exists."""

import re
from pathlib import Path

import yaml

from conftest import SKILL
from store_shots.cli import COMMANDS

SKILL_FILES = sorted(SKILL.rglob("*.md"))


def test_the_skill_loads_as_store_shots():
    front = yaml.safe_load((SKILL / "SKILL.md").read_text(encoding="utf-8").split("---")[1])
    assert front["name"] == "store-shots"
    assert front["description"].startswith("Store screenshots")


def test_every_command_the_skill_names_exists():
    named = {(path.name, command) for path in SKILL_FILES
             for command in re.findall(r"[`/]store-shots (?:--project \S+ )?([a-z]+)", path.read_text(encoding="utf-8"))}

    assert named
    assert {(name, command) for name, command in named if command not in COMMANDS} == set()


def test_every_link_in_the_skill_resolves():
    links = [(path, target) for path in SKILL_FILES
             for target in re.findall(r"\]\(([^)#:]+)\)", path.read_text(encoding="utf-8"))]

    assert links
    assert [(path.name, target) for path, target in links
            if not (path.parent / target).is_file()] == []
