"""A project: its config file, storyboard, copy files, layout folder and the
paths the stages read and write. Paths in the config are relative to it."""

from __future__ import annotations

import os
import re
from dataclasses import dataclass
from functools import cached_property
from pathlib import Path

import yaml

from . import catalog
from .errors import StageError

CONFIG_NAME = "store-shots.yaml"

DEFAULT_PATHS = {
    "storyboard": "storyboard.yaml",
    "copy": "texts",
    "layout": "layout",
    "raw": "raw",
    "out": "out",
    "logs": ".store-shots/logs",
    "work": ".store-shots/work",
    "sheets": ".store-shots/sheets",
    "preview": ".store-shots/preview",
}


class ConfigError(StageError):
    pass


@dataclass(frozen=True)
class Target:
    id: str
    slot: catalog.Slot
    size: tuple[int, int]
    screen: tuple[int, int]

    @property
    def store(self) -> str:
        return self.slot.store

    @property
    def frame(self) -> str:
        return self.slot.frame

    @property
    def landscape(self) -> bool:
        """Wider than tall: its images and its raws."""
        return self.size[0] > self.size[1]

    @property
    def turned(self) -> bool:
        """A phone or tablet target at a landscape size (a Mac's is always
        landscape): its device lies on its side, its frame's `landscape`
        placement applies and its cluster members are landscape too."""
        return self.slot.turns and self.landscape


@dataclass(frozen=True)
class SceneRole:
    """How a raw is held to its target (see docs/adapter.md): `screen`,
    `card` or `member`; [frame] is a member's frame kind, else None."""
    kind: str
    frame: str | None = None


STRICTNESS = ("screen", "card", "member")

# The status bar a panel's mockup draws; the first is the default.
STATUSES = ("normal", "airplane", "none")


@dataclass(frozen=True)
class FeatureGraphic:
    size: tuple[int, int]


@dataclass(frozen=True)
class Unframed:
    """An image that is one raw as captured, with no frame or copy: [scene]
    on [target] in [lang], saved as `out/unframed/<name>.png`."""
    name: str
    scene: str
    target: Target
    lang: str


def member_landscape(target: Target, frame: str) -> bool:
    """Whether a [frame] cluster member on [target] is landscape."""
    return frame in catalog.LANDSCAPE_FRAMES or target.turned


def find_root(start: Path) -> Path:
    for folder in [start, *start.parents]:
        if (folder / CONFIG_NAME).is_file():
            return folder
    raise ConfigError(f"no {CONFIG_NAME} in {start} or above it; pass --project")


def _size(value, where: str) -> tuple[int, int]:
    if not (isinstance(value, list) and len(value) == 2 and all(isinstance(v, int) for v in value)):
        raise ConfigError(f"{where} must be [width, height]")
    return value[0], value[1]


def _yaml(path: Path, what: str):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except FileNotFoundError:
        raise ConfigError(f"no {what} at {path}") from None
    except yaml.YAMLError as e:
        raise ConfigError(f"{path}: not valid YAML ({str(e).splitlines()[0]})") from None


class Project:
    def __init__(self, root: Path):
        self.root = root.resolve()
        self.config = _yaml(self.root / CONFIG_NAME, CONFIG_NAME)
        for key in ("languages", "targets", "adapter"):
            if key not in self.config:
                raise ConfigError(f"{CONFIG_NAME}: `{key}` missing")
        adapter = self.config["adapter"]
        if not isinstance(adapter, dict) or not adapter.get("command"):
            raise ConfigError(f"{CONFIG_NAME}: adapter.command missing")
        for key in ("inputs", "textless", "accepted"):
            listed = adapter.get(key)
            if listed is not None and not (isinstance(listed, list)
                                           and all(isinstance(v, str) for v in listed)):
                raise ConfigError(f"{CONFIG_NAME}: adapter.{key} must be a list of strings")

    def path(self, name: str) -> Path:
        return self.root / self.config.get("paths", {}).get(name, DEFAULT_PATHS[name])

    def rel(self, path: Path) -> str:
        """[path] as the console shows it: relative to the project (with `..`
        for a path beside it)."""
        return Path(os.path.relpath(path.resolve(), self.root)).as_posix()

    @cached_property
    def languages(self) -> dict[str, dict[str, str]]:
        """Copy language => {store: that store's language code}."""
        return {lang: dict(codes or {}) for lang, codes in self.config["languages"].items()}

    @cached_property
    def stores(self) -> list[str]:
        """The stores the project makes images for: those a language lists."""
        listed = {store for codes in self.languages.values() for store in codes}
        unknown = sorted(listed - set(catalog.STORES))
        if unknown:
            raise ConfigError(f"{CONFIG_NAME}: languages name unknown store {', '.join(unknown)}; "
                              f"stores are {', '.join(catalog.STORES)}")
        return [store for store in catalog.STORES if store in listed]

    def runs_on(self, store: str) -> list[str]:
        """The devices the app runs on in [store] (`runs_on.<store>`), which
        decide the slots the store requires."""
        listed = (self.config.get("runs_on") or {}).get(store)
        if listed is None:
            return list(catalog.DEFAULT_RUNS_ON[store])
        known = catalog.devices(store)
        if not isinstance(listed, list) or not set(listed) <= set(known):
            raise ConfigError(f"{CONFIG_NAME}: runs_on.{store} must list some of {', '.join(known)}")
        return listed

    def banned_phrases(self, lang: str) -> list[tuple[str, list[re.Pattern]]]:
        """[(what the phrase says, its patterns in [lang])] for every banned
        phrase with patterns in [lang]."""
        return [(claim, by_lang[lang]) for claim, by_lang in self._banned if by_lang.get(lang)]

    @cached_property
    def _banned(self) -> list[tuple[str, dict[str, list[re.Pattern]]]]:
        found = []
        for i, entry in enumerate(self.config.get("banned_phrases") or []):
            where = f"{CONFIG_NAME}: banned_phrases[{i}]"
            if not isinstance(entry, dict) or not isinstance(entry.get("says"), str):
                raise ConfigError(f"{where} needs `says:` and a pattern list per language")
            by_lang = {}
            for lang, patterns in entry.items():
                if lang == "says":
                    continue
                if lang not in self.languages:
                    raise ConfigError(f"{where}.{lang} is not a language of the project")
                if not isinstance(patterns, list) or not all(isinstance(p, str) for p in patterns):
                    raise ConfigError(f"{where}.{lang} must be a list of patterns")
                try:
                    by_lang[lang] = [re.compile(p) for p in patterns]
                except re.error as e:
                    raise ConfigError(f"{where}.{lang}: bad pattern ({e})") from None
            found.append((entry["says"], by_lang))
        return found

    def store_languages(self, store: str) -> list[tuple[str, str]]:
        """[(copy language, store code)] of every language the store lists."""
        return [(lang, codes[store]) for lang, codes in self.languages.items() if store in codes]

    @cached_property
    def targets(self) -> dict[str, Target]:
        found = {}
        for target_id, entry in self.config["targets"].items():
            where = f"{CONFIG_NAME}: targets.{target_id}"
            slot = catalog.SLOTS.get(entry.get("slot", ""))
            if slot is None:
                raise ConfigError(f"{where}.slot must be one of {', '.join(catalog.SLOTS)}")
            size = _size(entry.get("size"), f"{where}.size")
            screen = _size(entry["screen"], f"{where}.screen") if "screen" in entry else size
            if (screen[0] > screen[1]) != (size[0] > size[1]):
                raise ConfigError(f"{where}: screen and size must both be portrait or both"
                                  f" landscape (width first)")
            found[target_id] = Target(target_id, slot, size, screen)
        return found

    def target_languages(self, target: Target) -> list[str]:
        return [lang for lang, _ in self.store_languages(target.store)]

    @cached_property
    def storyboard(self) -> list[dict]:
        path = self.path("storyboard")
        panels = _yaml(path, "storyboard").get("panels") or []
        ids = [p.get("id") for p in panels]
        if len(set(ids)) != len(ids) or not all(ids):
            raise ConfigError(f"{self.rel(path)}: every panel needs a unique id")
        for panel in panels:
            where = f"{self.rel(path)}: panel {panel['id']}"
            cluster = panel.get("cluster")
            if cluster is None and not panel.get("scene"):
                raise ConfigError(f"{where} needs a scene or a cluster")
            for store, members in (cluster or {}).items():
                if store not in catalog.STORES or not isinstance(members, list) or not members:
                    raise ConfigError(f"{where}: cluster.{store} must be a store's list of devices")
                frames = [member.get("frame") for member in members if isinstance(member, dict)]
                if len(frames) != len(members) or not all(m.get("scene") for m in members) \
                        or not set(frames) <= set(catalog.FRAMES):
                    raise ConfigError(f"{where}: each cluster.{store} device needs a scene and a"
                                      f" frame ({', '.join(catalog.FRAMES)})")
                if len(set(frames)) != len(frames):
                    raise ConfigError(f"{where}: cluster.{store} shows a frame twice")
            if panel.get("status", STATUSES[0]) not in STATUSES:
                raise ConfigError(f"{where}: status must be one of {', '.join(STATUSES)}")
            badge = panel.get("badge")
            if badge is not None and not (isinstance(badge, dict) and badge.get("icon")
                                          and badge.get("copy")):
                raise ConfigError(f"{where}: badge needs an icon and a copy key")
        return panels

    def cluster(self, panel: dict, store: str) -> list[dict] | None:
        """The panel's devices on [store], back to front; None when it shows one device."""
        if "cluster" not in panel:
            return None
        members = panel["cluster"].get(store)
        if not members:
            raise ConfigError(f"{self.rel(self.path('storyboard'))}: panel {panel['id']}"
                              f" has no cluster for {store}")
        return members

    def scene_roles(self, target: Target, lang: str | None = None) -> dict[str, SceneRole]:
        """Every scene [target] needs captured (in [lang] only, when given),
        in storyboard order, unframed images' scenes last. A scene used two
        ways takes the strictest role."""
        roles: dict[str, SceneRole] = {}

        def add(scene: str, role: SceneRole) -> None:
            if scene.startswith("__"):
                raise ConfigError(f"scene {scene}: names starting with `__` are the engine's"
                                  f" own (adapter test's probes)")
            if scene not in roles or STRICTNESS.index(role.kind) < STRICTNESS.index(roles[scene].kind):
                roles[scene] = role

        for panel in self.storyboard:
            members = self.cluster(panel, target.store)
            if members is not None:
                for member in members:
                    add(member["scene"], SceneRole("member", member["frame"]))
                continue
            add(panel["scene"], SceneRole("screen"))
            if panel.get("card"):
                add(panel["card"], SceneRole("card"))
        for image in self.unframed:
            if image.target == target and lang in (None, image.lang):
                add(image.scene, SceneRole("screen"))
        return roles

    def scenes(self, target: Target, lang: str | None = None) -> list[str]:
        return list(self.scene_roles(target, lang))

    def member_screens(self, target: Target, frame: str) -> list[tuple[int, int]]:
        """The screen of each target shown in [frame], in config order, turned
        to the orientation a [frame] cluster member takes on [target]: its
        target's, or landscape for a landscape frame."""
        landscape = member_landscape(target, frame)
        return list(dict.fromkeys(
            t.screen if (t.screen[0] > t.screen[1]) == landscape else t.screen[::-1]
            for t in self.targets.values() if t.frame == frame))

    def copy_path(self, lang: str) -> Path:
        return self.path("copy") / f"{lang}.yaml"

    def copy(self, lang: str) -> dict:
        return _yaml(self.copy_path(lang), f"copy file for {lang}")

    @cached_property
    def feature_graphic(self) -> FeatureGraphic | None:
        """The Play feature graphic's settings; None when the project has none."""
        entry = self.config.get("feature_graphic")
        if entry is None:
            return None
        where = f"{CONFIG_NAME}: feature_graphic"
        if not isinstance(entry, dict):
            raise ConfigError(f"{where} must hold its size")
        if "play" not in self.stores:
            raise ConfigError(f"{where} is Play's; no language lists play")
        size = _size(entry.get("size", list(catalog.FEATURE_GRAPHIC_SIZE)), f"{where}.size")
        return FeatureGraphic(size)

    def feature_graphic_path(self, code: str) -> Path:
        return self.path("out") / "play" / code / "feature-graphic.png"

    @cached_property
    def unframed(self) -> list[Unframed]:
        """The unframed images, in config order."""
        entries = self.config.get("unframed") or {}
        where = f"{CONFIG_NAME}: unframed"
        if not isinstance(entries, dict):
            raise ConfigError(f"{where} must map image names to a scene, a target and a lang")
        found = []
        for name, entry in entries.items():
            at = f"{where}.{name}"
            if not re.fullmatch(r"[A-Za-z0-9_.-]+", str(name)):
                raise ConfigError(f"{at}: a name takes letters, digits, `_`, `.` and `-` only")
            if not isinstance(entry, dict) or not isinstance(entry.get("scene"), str) \
                    or not entry["scene"]:
                raise ConfigError(f"{at} needs a scene, a target and a lang")
            target = self.targets.get(entry.get("target"))
            if target is None:
                raise ConfigError(f"{at}.target must be one of {', '.join(self.targets)}")
            langs = self.target_languages(target)
            if entry.get("lang") not in langs:
                raise ConfigError(f"{at}.lang must be a language {target.store} lists:"
                                  f" {', '.join(langs)}")
            found.append(Unframed(name, entry["scene"], target, entry["lang"]))
        return found

    def unframed_path(self, name: str) -> Path:
        return self.path("out") / "unframed" / f"{name}.png"

    def panel_copy(self, lang: str, panel: dict, store: str) -> dict[str, str]:
        """The texts a panel shows on [store], by copy key: headline, subline
        and badge. A panel's per-store variant (`app_store:` / `play:`) wins
        over its plain texts; the badge text is `badges.<its copy key>`."""
        copy = self.copy(lang)
        entry = (copy.get("panels") or {}).get(panel["id"])
        if not entry:
            raise ConfigError(f"{self.rel(self.copy_path(lang))}: no panels.{panel['id']}")
        entry = entry.get(store, entry)
        words = {key: entry[key] for key in ("headline", "subline") if entry.get(key)}
        if panel.get("badge"):
            key = panel["badge"]["copy"]
            text = (copy.get("badges") or {}).get(key)
            if not text:
                raise ConfigError(f"{self.rel(self.copy_path(lang))}: no badges.{key}")
            words["badge"] = text
        return words

    def raw_dir(self, target: str, lang: str) -> Path:
        return self.path("raw") / target / lang

    def raw_path(self, target: str, lang: str, scene: str) -> Path:
        return self.raw_dir(target, lang) / f"{target}-{scene}.png"

    def screenshot_path(self, store: str, code: str, target: str, panel: str) -> Path:
        return self.path("out") / store / code / f"{target}-{panel}.png"

    def sheet_path(self, store: str, code: str) -> Path:
        return self.path("sheets") / store / f"{code}.png"

    def log_path(self, name: str) -> Path:
        path = self.path("logs") / f"{name}.log"
        path.parent.mkdir(parents=True, exist_ok=True)
        return path
