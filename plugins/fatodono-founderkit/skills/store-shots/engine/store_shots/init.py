"""`init`: a new project in a folder without one. The example project is the
starting point: each device the app runs on gets the example's target and
placement for it, and the project gets the example's layout. The storyboard
and the copy start empty; the storyboard and copy stages write them."""

from __future__ import annotations

import posixpath
import shutil
from importlib.resources import files
from pathlib import Path

import yaml

from . import catalog
from .errors import StageError
from .project import CONFIG_NAME, DEFAULT_PATHS
from .words import plural

EXAMPLE = Path(__file__).resolve().parents[2] / "example"
DEFAULT_COPY = DEFAULT_PATHS["copy"]


class InitError(StageError):
    pass


def _example_targets() -> dict[str, dict]:
    return yaml.safe_load((EXAMPLE / CONFIG_NAME).read_text(encoding="utf-8"))["targets"]


def targets_for(runs_on: dict[str, list[str]]) -> dict[str, dict]:
    """The example's target for each device in [runs_on], in store order."""
    by_device = {}
    for target_id, entry in _example_targets().items():
        slot = catalog.SLOTS[entry["slot"]]
        by_device.setdefault((slot.store, slot.device), (target_id, entry))
    return dict(by_device[(store, device)]
                for store in catalog.STORES for device in runs_on.get(store, []))


def parse_runs_on(values: list[str]) -> dict[str, list[str]]:
    """`store=device,device` per value, checked against the catalog."""
    runs_on: dict[str, list[str]] = {}
    for value in values:
        store, _, devices = value.partition("=")
        if store not in catalog.STORES:
            raise InitError(f"--runs-on {value}: stores are {', '.join(catalog.STORES)}")
        listed = [d for d in devices.split(",") if d]
        known = catalog.devices(store)
        unknown = [d for d in listed if d not in known]
        if not listed or unknown:
            raise InitError(f"--runs-on {value}: {store} devices are {', '.join(known)}")
        runs_on[store] = listed
    if not runs_on:
        raise InitError("--runs-on is required, once per store")
    return runs_on


def parse_languages(values: list[str], stores: list[str]) -> dict[str, dict[str, str]]:
    """`lang=code` per value: the copy language and its code in every store."""
    languages = {}
    for value in values:
        lang, _, code = value.partition("=")
        if not lang or not code:
            raise InitError(f"--lang {value}: write it as <copy language>=<store code>, en=en-US")
        languages[lang] = {store: code for store in stores}
    if not languages:
        raise InitError("--lang is required: the copy language and its store code, en=en-US")
    return languages


def _flow(value) -> str:
    return yaml.safe_dump(value, default_flow_style=True, sort_keys=False, width=1000).strip()


def config_text(languages: dict, targets: dict, runs_on: dict, adapter: dict,
                copy: str = DEFAULT_COPY) -> str:
    sections = [
        "# Made by `store-shots init`. Every key: the store-shots skill's docs/config.md.\n"
        "languages:\n" + "".join(f"  {lang}: {_flow(codes)}\n" for lang, codes in languages.items()),
    ]
    if copy != DEFAULT_COPY:
        sections.append(f"paths: {_flow({'copy': copy})}\n")
    sections += [
        "targets:\n" + "".join(f"  {tid}: {_flow(entry)}\n" for tid, entry in targets.items()),
        "runs_on:\n" + "".join(f"  {store}: {_flow(devices)}\n" for store, devices in runs_on.items()),
    ]
    if "play" in runs_on:
        sections.append(f"feature_graphic:\n  size: {_flow(list(catalog.FEATURE_GRAPHIC_SIZE))}\n")
    sections.append(f"adapter:\n  command: {_flow(adapter['command'])}\n"
                    f"  inputs: {_flow(adapter['inputs'])}\n")
    return "\n".join(s.rstrip("\n") + "\n" for s in sections)


def placement_text(frames: set[str]) -> str:
    """The example's placement.yaml with only the blocks of [frames]: its
    blocks are blank-line separated, each one top-level key."""
    head, *blocks = (EXAMPLE / "layout" / "placement.yaml").read_text(encoding="utf-8").split("\n\n")
    kept = [b for b in blocks if b.split(":", 1)[0] in frames]
    return "\n\n".join([head, *kept]).rstrip("\n") + "\n"


ADAPTER = {"command": ["uv", "run", "--quiet", "--script", "adapter/adapter.py"],
           "inputs": ["adapter/**"]}


def adapter_script() -> str:
    return files("store_shots").joinpath("starter", "adapter.py").read_text(encoding="utf-8")


def init(root: Path, runs_on_values: list[str], lang_values: list[str],
         copy: str = DEFAULT_COPY) -> str:
    """Writes the project into [root], its copy files into [copy] (relative to
    [root]); writes nothing when any of its files exists. Returns the console
    text."""
    copy = posixpath.normpath(copy)
    runs_on = parse_runs_on(runs_on_values)
    languages = parse_languages(lang_values, list(runs_on))
    targets = targets_for(runs_on)
    frames = {catalog.SLOTS[entry["slot"]].frame for entry in targets.values()}

    texts = {
        CONFIG_NAME: config_text(languages, targets, runs_on, ADAPTER, copy),
        "storyboard.yaml": "# The panels in store order; the storyboard stage writes them.\npanels: []\n",
        **{f"{copy}/{lang}.yaml": "# The text the images show; the copy stage writes it.\npanels: {}\n"
           for lang in languages},
        "layout/placement.yaml": placement_text(frames),
        "adapter/adapter.py": adapter_script(),
        ".store-shots/.gitignore": "*\n",
    }
    pages = ["panel"] + (["feature"] if "play" in runs_on else [])
    copied = {f"layout/{page}.{ext}": EXAMPLE / "layout" / f"{page}.{ext}"
              for page in pages for ext in ("html", "css")}
    copied |= {f"layout/icons/{icon.name}": icon
               for icon in sorted((EXAMPLE / "layout" / "icons").glob("*.svg"))}

    existing = [rel for rel in [*texts, *copied] if (root / rel).exists()]
    if existing:
        raise InitError(f"{existing[0]} exists; init writes only into a folder without a project")
    for rel, text in texts.items():
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        (root / rel).write_text(text, encoding="utf-8")
    for rel, source in copied.items():
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, root / rel)
    return f"{plural(len(texts) + len(copied), 'file')} written, " \
           f"{plural(len(targets), 'target')}: {', '.join(targets)}"
