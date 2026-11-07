"""`--help` is where an agent learns the commands, so it must say what each does."""

import os
import subprocess
import sys

from conftest import ENGINE_PATH


def help_text(*args: str) -> str:
    done = subprocess.run([sys.executable, "-m", "store_shots", *args, "--help"],
                          capture_output=True, text=True, check=True,
                          env={**os.environ, **ENGINE_PATH})
    return " ".join(done.stdout.split())


def test_the_top_level_help_says_how_every_command_reports():
    assert "Each command prints one line per stage and ends with the exit code" in help_text()


def test_a_commands_help_says_what_it_does():
    assert "list each stale output and the input that made it stale" in help_text("status")


def test_builds_help_names_every_stage_it_runs():
    text = help_text("build")

    for stage in ("capture", "compose", "check", "sheet"):
        assert stage in text.split("options:")[0]
