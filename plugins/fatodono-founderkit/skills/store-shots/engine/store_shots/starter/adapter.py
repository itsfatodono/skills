#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""The project's store-shots adapter. The engine runs it from the project folder as

    adapter.py --device <target> --langs en,tr --scenes home,editor --out <empty folder> --request <file>

and holds its output to the store-shots skill's docs/adapter.md. Build it gate
by gate with `store-shots adapter test`. Dependencies go in the header above;
any other program works too if adapter.command points at it.
"""

import argparse
import json
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    for name in ("--device", "--langs", "--scenes", "--out", "--request"):
        parser.add_argument(name, required=True)
    args = parser.parse_args()
    request = json.loads(Path(args.request).read_text(encoding="utf-8"))

    # Capture request["scenes"] in request["langs"] on request["target"] into
    # request["out"], then write request["report"]; docs/adapter.md has the steps.
    print("adapter.py: the capture is not written yet (docs/adapter.md)", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
