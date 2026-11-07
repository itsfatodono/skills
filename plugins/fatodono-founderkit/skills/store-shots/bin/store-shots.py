#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["pillow==13.0.0", "pyyaml==6.0.3"]
# ///
"""Run on every OS as `uv run --script bin/store-shots.py <command>`."""

import sys
from pathlib import Path

# The skill folder may be a versioned plugin cache or sit inside the user's repo.
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "engine"))

from store_shots.cli import main  # noqa: E402

sys.exit(main())
