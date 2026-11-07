#!/usr/bin/env -S uv run --quiet --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Stands in for an app adapter, keeping docs/adapter.md as a real one must.

    fake_adapter.py --device ID --langs en,tr --scenes home,... --out DIR --request FILE

It has every scene a project can name; of the engine's `__` names, only the probes.

Tests break one rule at a time through the environment:
  FAKE_ADAPTER_OMIT     a scene to leave out
  FAKE_ADAPTER_SIZE     WxH for every scene, or scene=WxH for one
  FAKE_ADAPTER_REPORT   extra report lines, one issue each
  FAKE_ADAPTER_SHADE    R,G,B for the page band, as a changed app would draw
  FAKE_ADAPTER_CALLS    a file each call appends its arguments to, as JSON
  FAKE_ADAPTER_BREAK    no-checks, no-text, ignore-unknown, status-bar,
                        miss-cut-off, one-language, random or extra-file
"""

import argparse
import json
import os
import random
import struct
import zlib
from pathlib import Path

# App-like bands, top to bottom: (share of the height, RGB).
BANDS = [(0.07, (248, 243, 234)), (0.06, (233, 225, 208)), (0.87, (255, 253, 247))]
CARD_BANDS = [(0.25, (222, 239, 253)), (0.75, (255, 253, 247))]
STATUS_BAR = (0.02, (0, 0, 0))


def png(width: int, height: int, bands: list) -> bytes:
    rows = []
    top = 0.0
    for share, colour in bands:
        bottom = top + share
        count = round(bottom * height) - round(top * height)
        rows.append((b"\x00" + bytes(colour) * width) * count)
        top = bottom
    raw = b"".join(rows)

    def chunk(kind: bytes, data: bytes) -> bytes:
        body = kind + data
        return struct.pack(">I", len(data)) + body + struct.pack(">I", zlib.crc32(body))

    header = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", header)
            + chunk(b"IDAT", zlib.compress(raw, 6)) + chunk(b"IEND", b""))


def size_of(entry: dict) -> tuple[int, int]:
    """Cards and shapeless cluster members get made-up sizes within what the
    request allows."""
    if "size" in entry:
        return tuple(entry["size"])
    if "max_size" in entry:
        width, height = entry["max_size"]
        return width * 9 // 10, height * 3 // 10
    if "shape" in entry:
        return tuple(entry["shape"])
    return (2560, 1600) if entry["orientation"] == "landscape" else (1320, 2868)


def is_project_scene(scene: str) -> bool:
    return not scene.startswith("__")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", required=True)
    parser.add_argument("--langs", required=True)
    parser.add_argument("--scenes", required=True)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--request", required=True, type=Path)
    args = parser.parse_args()
    request = json.loads(args.request.read_text(encoding="utf-8"))
    langs = list(request["langs"])
    scenes = list(request["scenes"])
    broken = os.environ.get("FAKE_ADAPTER_BREAK", "")

    calls = os.environ.get("FAKE_ADAPTER_CALLS")
    if calls:
        with open(calls, "a") as f:
            f.write(json.dumps({"device": args.device, "langs": langs, "scenes": scenes}) + "\n")

    forced = os.environ.get("FAKE_ADAPTER_SIZE", "")
    forced_scene, _, forced_size = forced.rpartition("=")
    omit = os.environ.get("FAKE_ADAPTER_OMIT")
    shade = os.environ.get("FAKE_ADAPTER_SHADE")
    report = []

    for scene in scenes:
        if not is_project_scene(scene) and not request["scenes"][scene].get("probe") and broken != "ignore-unknown":
            for lang in langs:
                report.append(f"{lang}/{args.device}-{scene}.png: no such scene")

    for lang in langs:
        folder = args.out / lang
        folder.mkdir(parents=True, exist_ok=True)
        for scene in scenes:
            entry = request["scenes"][scene]
            name = f"{lang}/{args.device}-{scene}.png"
            if scene == omit or not (is_project_scene(scene) or entry.get("probe")):
                continue
            print(f"booting {args.device}, pumping {scene} in {lang}")
            width, height = size_of(entry)
            if forced_size and forced_scene in ("", scene):
                width, height = map(int, forced_size.split("x"))
            texts = 3
            if entry.get("probe") == "fullbleed":
                fill = tuple(int(entry["fill"][i:i + 2], 16) for i in (1, 3, 5))
                bands = [(1.0, fill)]
                if broken == "status-bar":
                    bands = [STATUS_BAR, (1 - STATUS_BAR[0], fill)]
                texts = 0
            elif entry.get("probe") == "truncation":
                bands, texts = list(CARD_BANDS), 1
                if broken != "miss-cut-off":
                    report.append(f"{name}: text '{entry['text']}' shows 1 of 2 lines")
            else:
                bands = list(CARD_BANDS if entry["role"] == "card" else BANDS)
                if shade:
                    bands[-1] = (bands[-1][0], tuple(map(int, shade.split(","))))
                # The app's locale shows in its pixels; the fake tints its header.
                if lang != "en" and broken != "one-language":
                    tint = 1 + sum(map(ord, lang)) % 4
                    share, (r, g, b) = bands[0]
                    bands[0] = (share, (r - tint, g, b))
                if broken == "random":
                    share, (r, g, b) = bands[-1]
                    bands[-1] = (share, (r, g, random.randrange(200, 256)))
            if broken == "no-text":
                texts = 0
            (args.out / name).write_bytes(png(width, height, bands))
            if broken != "no-checks":
                report.append(f"checked {name} texts={texts}")

    extra = os.environ.get("FAKE_ADAPTER_REPORT", "")
    report += [line for line in extra.splitlines() if line.strip()]
    if broken == "extra-file":
        (args.out / "debug.log").write_text("left behind\n", encoding="utf-8")
    (args.out / "report.txt").write_text("".join(f"{line}\n" for line in report), encoding="utf-8")


if __name__ == "__main__":
    main()
