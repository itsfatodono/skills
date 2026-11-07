"""Placement: where each element of a layout page sits, as data in the
project's layout folder (`placement.yaml`), so moving a device, card or
badge never touches the page or its stylesheet.

    <frame kind or target id>:
      <place>: {<css property>: <value>, ...}    every panel
      cluster: {<frame kind>: {...}, ...}        a cluster's devices
      panels:
        <panel id>: {<place>: {...}, ...}        one panel
      landscape: {<the keys above>}              a target turned to landscape

A place is a `data-place` name on the page (`device`, `card`, `badge` and
`cluster.<frame>` are the engine's own). The key `feature_graphic` places
the feature graphic's page. A device's screen width is its
`--screen-w`. For one target and panel the entries merge per property:
frame kind, then that frame's panel, then on a target turned to landscape
(a phone or tablet one at a landscape size) the frame's `landscape` entry and
its panel, then target id and its panel.
"""

from __future__ import annotations

from pathlib import Path

import yaml

from .errors import StageError

PLACEMENT = "placement.yaml"
# Holds the feature page's places and no panels.
FEATURE_GRAPHIC_KEY = "feature_graphic"
# A frame's places on a target turned to landscape, over its own.
LANDSCAPE = "landscape"


class PlacementError(StageError):
    pass


def load(layout: Path) -> dict:
    path = layout / PLACEMENT
    if not path.is_file():
        return {}
    try:
        found = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as e:
        raise PlacementError(f"{PLACEMENT}: not valid YAML ({str(e).splitlines()[0]})") from None
    if not isinstance(found, dict):
        raise PlacementError(f"{PLACEMENT} must map frame kinds or target ids to places")
    return found


def resolve(placement: dict, frame: str, target: str, panel: str, turned: bool = False) -> dict:
    """The places of [panel] on [target] (a [frame] device, [turned] to
    landscape), merged."""
    frame_entry = placement.get(frame) or {}
    entries = [frame_entry]
    if turned:
        entries.append(frame_entry.get(LANDSCAPE) or {})
    if target != frame:
        entries.append(placement.get(target) or {})
    merged: dict = {}
    for entry in entries:
        _merge(merged, {k: v for k, v in entry.items() if k not in ("panels", LANDSCAPE)})
        _merge(merged, (entry.get("panels") or {}).get(panel) or {})
    return merged


def feature(placement: dict) -> dict:
    """The places of the feature graphic's page."""
    merged: dict = {}
    _merge(merged, placement.get(FEATURE_GRAPHIC_KEY) or {})
    return merged


def _merge(into: dict, entry: dict) -> None:
    for key, value in entry.items():
        if isinstance(value, dict) and isinstance(into.get(key), dict):
            _merge(into[key], value)
        elif isinstance(value, dict):
            into[key] = {}
            _merge(into[key], value)
        else:
            into[key] = str(value)
