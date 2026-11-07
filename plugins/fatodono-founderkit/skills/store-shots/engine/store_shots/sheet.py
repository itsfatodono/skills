"""Contact sheets: per store and language, every image the tool makes for
it downscaled onto one labelled image, for review in one look.

A sheet records a digest of its tiles (labels, order and image bytes) and is
rewritten only when that digest changes, so it is stale exactly when one of
its images changed."""

from __future__ import annotations

import hashlib
import math
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, PngImagePlugin

from . import compose
from .errors import StageError
from .project import Project

LONG_SIDE = 1600
GAP = 16
LABEL = 26
FONT_SIZES = range(18, 9, -1)
BACKGROUND = (232, 232, 232)
INK = (27, 27, 27)


@dataclass(frozen=True)
class Tile:
    label: str
    image: Path


@dataclass(frozen=True)
class Sheet:
    path: Path
    rows: list[list[Tile]]

    def digest(self) -> str:
        h = hashlib.sha256()
        for row in self.rows:
            h.update(b"row\0")
            for tile in row:
                h.update(tile.label.encode() + b"\0")
                h.update(hashlib.sha256(tile.image.read_bytes()).digest())
        return h.hexdigest()


def sheets(project: Project) -> list[Sheet]:
    """Every sheet the project's targets call for: one row per target in
    config order, its panels in storyboard order; then, on Play, a row for
    the feature graphic; then, on the sheet of each unframed image's store
    and language, a row of those images. So the sheets show every image the
    tool makes."""
    found = {}
    for target in project.targets.values():
        for _, code in project.store_languages(target.store):
            path = project.sheet_path(target.store, code)
            row = [Tile(f"{target.id} {panel['id']}",
                        project.screenshot_path(target.store, code, target.id, panel["id"]))
                   for panel in project.storyboard]
            found.setdefault(path, []).append(row)
    for job in compose.feature_jobs(project):
        found.setdefault(project.sheet_path("play", job.code), []).append(
            [Tile("feature graphic", job.out)])
    unframed: dict[Path, list[Tile]] = {}
    for job in compose.unframed_jobs(project):
        store = job.target.store
        code = dict(project.store_languages(store))[job.image.lang]
        unframed.setdefault(project.sheet_path(store, code), []).append(
            Tile(f"unframed {job.image.name}", job.out))
    for path, row in unframed.items():
        found.setdefault(path, []).append(row)
    return [Sheet(path, rows) for path, rows in found.items()]


def refresh(project: Project) -> tuple[int, int]:
    """Writes every stale sheet. Returns (written, up to date)."""
    written = fresh = 0
    for sheet in sheets(project):
        for tile in (t for row in sheet.rows for t in row):
            if not tile.image.is_file():
                raise StageError(f"{project.rel(tile.image)} missing; run build")
        digest = sheet.digest()
        if _recorded_digest(sheet.path) == digest:
            fresh += 1
            continue
        draw(sheet, digest)
        written += 1
    return written, fresh


def _recorded_digest(path: Path) -> str | None:
    try:
        with Image.open(path) as image:
            return image.text.get("Sources")
    except (FileNotFoundError, OSError):
        return None


def _layout(aspects: list[list[float]]) -> tuple[int, float]:
    """The column count and tile height that make the tiles largest while
    the sheet's long side stays within LONG_SIDE. [aspects] holds each row's
    tile width / height; a row longer than the column count wraps."""
    best = (1, 0.0)
    for columns in range(1, max(len(row) for row in aspects) + 1):
        lines = [row[i:i + columns] for row in aspects for i in range(0, len(row), columns)]
        widest = max(sum(line) for line in lines)
        by_width = (LONG_SIDE - GAP - columns * GAP) / widest
        by_height = (LONG_SIDE - GAP - len(lines) * (LABEL + GAP)) / len(lines)
        height = min(by_width, by_height)
        if height > best[1]:
            best = (columns, height)
    return best


def _font(text: str, width: int) -> ImageFont.FreeTypeFont:
    for size in FONT_SIZES:
        font = ImageFont.load_default(size=size)
        if font.getlength(text) <= width:
            return font
    return font


def draw(sheet: Sheet, digest: str) -> None:
    """Writes [sheet] even when fresh; [digest] is what `refresh` later compares against."""
    images = [[Image.open(tile.image) for tile in row] for row in sheet.rows]
    try:
        columns, height = _layout([[i.width / i.height for i in row] for row in images])
        height = math.floor(min(height, min(i.height for row in images for i in row)))
        lines = [list(zip(row_tiles[i:i + columns], row_images[i:i + columns]))
                 for row_tiles, row_images in zip(sheet.rows, images)
                 for i in range(0, len(row_tiles), columns)]
        widths = [[max(1, round(height * image.width / image.height)) for _, image in line]
                  for line in lines]
        canvas = Image.new("RGB", (
            GAP + max(sum(w) + GAP * len(w) for w in widths),
            GAP + len(lines) * (LABEL + height + GAP),
        ), BACKGROUND)
        draw = ImageDraw.Draw(canvas)
        y = GAP
        for line, line_widths in zip(lines, widths):
            x = GAP
            for (tile, image), width in zip(line, line_widths):
                draw.text((x, y + LABEL // 2), tile.label, fill=INK, anchor="lm",
                          font=_font(tile.label, width))
                thumb = image.convert("RGB").resize((width, height), Image.Resampling.LANCZOS)
                canvas.paste(thumb, (x, y + LABEL))
                x += width + GAP
            y += LABEL + height + GAP
    finally:
        for image in (i for row in images for i in row):
            image.close()
    info = PngImagePlugin.PngInfo()
    info.add_itxt("Tiles", "\n".join(tile.label for row in sheet.rows for tile in row))
    info.add_itxt("Sources", digest)
    sheet.path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(sheet.path, pnginfo=info)
