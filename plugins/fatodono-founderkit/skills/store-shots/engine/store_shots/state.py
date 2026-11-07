"""Staleness of raws and composed images: each keeps a sidecar naming every
input it was made from with that input's digest, and is stale when it or its
sidecar is missing or an input's digest differs from the recorded one.
Contact sheets keep their digest inside the PNG instead.

Inputs are a flat {name: digest} map, so a stage adds an input by adding a
key; the name is what `status` shows as the reason."""

from __future__ import annotations

import glob
import hashlib
import json
import os
from functools import lru_cache
from pathlib import Path

SIDECAR_SUFFIX = ".inputs.json"


def digest_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def digest_file(path: Path) -> str:
    stat = path.stat()
    return _digest_file(path.resolve(), stat.st_mtime_ns, stat.st_size)


@lru_cache(maxsize=None)
def _digest_file(path: Path, mtime_ns: int, size: int) -> str:
    return digest_bytes(path.read_bytes())


def digest_value(value) -> str:
    """The digest of a JSON-shaped value; key order does not matter."""
    return digest_bytes(json.dumps(value, sort_keys=True, ensure_ascii=False).encode())


def digest_globs(root: Path, patterns: list[str], exclude: list[Path]) -> str:
    """One digest over every file the [patterns] match under [root] (`**`
    recursive, `..` allowed), by path and content; files under [exclude]
    never count, so an output can not be its own input."""
    excluded = [str(p.resolve()) + os.sep for p in exclude]
    files = {}
    for pattern in patterns:
        for match in glob.glob(pattern, root_dir=root, recursive=True, include_hidden=True):
            path = (root / match).resolve()
            if path.is_file() and not any(str(path).startswith(e) for e in excluded):
                files[os.path.normpath(match).replace(os.sep, "/")] = digest_file(path)
    return digest_value(files)


def sidecar(output: Path) -> Path:
    return output.with_name(output.stem + SIDECAR_SUFFIX)


def record(output: Path, inputs: dict[str, str]) -> None:
    sidecar(output).write_text(json.dumps(inputs, indent=1, sort_keys=True) + "\n", encoding="utf-8")


def why_stale(output: Path, inputs: dict[str, str]) -> str | None:
    """None when [output] was made from exactly [inputs]; otherwise the reason."""
    if not output.is_file():
        return "missing"
    try:
        recorded = json.loads(sidecar(output).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return "no recorded inputs"
    changed = sorted(k for k in inputs.keys() | recorded.keys() if inputs.get(k) != recorded.get(k))
    if not changed:
        return None
    return ", ".join(changed) + " changed"
