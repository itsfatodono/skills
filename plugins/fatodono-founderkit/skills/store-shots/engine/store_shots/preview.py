"""`preview`: every target's panels in one language and Play's feature graphic, on placeholders
where raws or copy are missing. It writes nothing under `out/`, so it never makes a build stale."""

from __future__ import annotations

import shutil
from functools import cached_property
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from . import compose, contract, sheet
from .errors import StageError
from .project import ConfigError, Project, Target
from .words import plural

PLACEHOLDER_SUBLINE = "A placeholder subline, about as long as a real one."
SCREEN_FILL = (214, 214, 214)
SCREEN_INK = (120, 120, 120)
CARD_SHAPE = (1.0, 0.32)  # a card's width and height, as shares of the screen's width
MEMBER_SIZE = {"landscape": (1600, 1000), "portrait": (1000, 2000)}


class PreviewError(StageError):
    pass


def placeholder(project: Project, target: Target, scene: str, folder: Path) -> Path:
    """A flat screen labelled [scene], the size [target]'s adapter would capture."""
    entry = contract.scene_entry(project, target, scene, project.scene_roles(target)[scene])
    width, height = target.screen
    if entry["role"] == "screen":
        size = (width, height)
    elif entry["role"] == "card":
        size = (round(width * CARD_SHAPE[0]), round(width * CARD_SHAPE[1]))
    elif "shape" in entry:
        size = tuple(entry["shape"])
    else:
        size = MEMBER_SIZE[entry["orientation"]]
    path = folder / "screens" / f"{target.id}-{scene}.png"
    path.parent.mkdir(parents=True, exist_ok=True)
    image = Image.new("RGB", size, SCREEN_FILL)
    font = ImageFont.load_default(size=max(12, min(size) // 10))
    ImageDraw.Draw(image).text((size[0] / 2, size[1] / 2), scene, fill=SCREEN_INK,
                               anchor="mm", font=font)
    image.save(path)
    return path


class PreviewPanel(compose.PanelJob):
    """A panel's image as compose would make it, with placeholders for what
    is missing."""

    folder: Path
    placeholders: list[str]

    @property
    def out(self) -> Path:
        return self.folder / f"{self.target.id}-{self.panel['id']}.png"

    @cached_property
    def raws(self) -> dict[str, Path]:
        found = {}
        for scene, raw in super().raws.items():
            if not raw.is_file():
                raw = placeholder(self.project, self.target, scene, self.folder)
                self.placeholders.append(f"screen {self.target.id} {scene}")
            found[scene] = raw
        return found

    @cached_property
    def words(self) -> dict[str, str]:
        try:
            return self.project.panel_copy(self.lang, self.panel, self.target.store)
        except ConfigError:
            self.placeholders.append(f"copy {self.panel['id']}")
            words = {"headline": self.panel.get("claim") or self.panel["id"],
                     "subline": PLACEHOLDER_SUBLINE}
            if self.panel.get("badge"):
                words["badge"] = self.panel["badge"]["copy"]
            return words


class PreviewFeature(compose.FeatureJob):
    folder: Path
    placeholders: list[str]

    @property
    def out(self) -> Path:
        return self.folder / "feature-graphic.png"

    @cached_property
    def words(self) -> dict[str, str]:
        try:
            words, missing = compose.feature_copy(self.project, self.lang)
        except ConfigError:
            words, missing = {}, compose.feature_keys(self.project)
        for key in missing:
            self.placeholders.append(f"copy feature_graphic.{key}")
            words[key] = key.replace("_", " ").capitalize()
        return {key: words[key] for key in compose.feature_keys(self.project)}


def _language(project: Project, lang: str | None) -> str:
    known = list(project.languages)
    if lang is None:
        return known[0]
    if lang not in known:
        raise PreviewError(f"no language {lang}; known: {', '.join(known)}")
    return lang


def _panels(project: Project, wanted: list[str] | None) -> list[dict]:
    panels = project.storyboard
    if not panels:
        raise PreviewError(f"{project.rel(project.path('storyboard'))} has no panels;"
                           " the storyboard stage writes them first")
    if not wanted:
        return panels
    unknown = sorted(set(wanted) - {p["id"] for p in panels})
    if unknown:
        raise PreviewError(f"no panel {', '.join(unknown)}; known: {', '.join(p['id'] for p in panels)}")
    return [p for p in panels if p["id"] in wanted]


def preview(project: Project, lang: str | None = None, panels: list[str] | None = None) -> str:
    """Replaces [lang]'s preview folder with its images and sheet; returns the console line."""
    lang = _language(project, lang)
    chosen = _panels(project, panels)
    folder = project.path("preview") / lang
    shutil.rmtree(folder, ignore_errors=True)
    folder.mkdir(parents=True)
    placeholders: list[str] = []
    log = project.log_path("preview")
    log.parent.mkdir(parents=True, exist_ok=True)
    log.write_text("", encoding="utf-8")

    rows = []
    for target in project.targets.values():
        codes = dict(project.store_languages(target.store))
        if lang not in codes:
            continue
        row = []
        for panel in chosen:
            job = PreviewPanel(project, target, lang, codes[lang], panel)
            job.folder, job.placeholders = folder, placeholders
            job.write(log)
            row.append(sheet.Tile(f"{target.id} {panel['id']}", job.out))
        rows.append(row)
    play = dict(project.store_languages("play"))
    if project.feature_graphic is not None and lang in play:
        job = PreviewFeature(project, lang, play[lang])
        job.folder, job.placeholders = folder, placeholders
        job.write(log)
        rows.append([sheet.Tile("feature graphic", job.out)])
    if not rows:
        raise PreviewError(f"no target's store lists {lang}")

    path = folder / "sheet.png"
    sheet.draw(sheet.Sheet(path, rows), "preview")
    images = sum(len(row) for row in rows)
    line = f"{plural(images, 'image')}, sheet {project.rel(path)}"
    unique = set(placeholders)
    screens = sum(1 for p in unique if p.startswith("screen "))
    texts = len(unique) - screens
    counts = [plural(n, word) for n, word in [(screens, "screen"), (texts, "text")] if n]
    if counts:
        line += f"; placeholders: {', '.join(counts)}"
    return line

