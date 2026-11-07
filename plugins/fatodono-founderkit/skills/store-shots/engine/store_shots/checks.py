"""The automatic checks: one list of problems, each naming its source and
the file it is about. A new rule is a function in SOURCES; a new kind of
output is an entry in `expected_images`."""

from __future__ import annotations

import re
import struct
import zlib
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from . import catalog, compose
from .errors import StageError
from .project import CONFIG_NAME, Project
from .words import first_of, plural


@dataclass(frozen=True)
class Problem:
    source: str
    path: str
    message: str

    def __str__(self) -> str:
        return f"{self.source}: {self.path}: {self.message}"


@dataclass(frozen=True)
class ExpectedImage:
    """An image the project must hold: for a store to take its listing, or
    as an unframed image. [lang] is the copy language whose banned phrases
    its text must avoid; [store] is None for an image that shows no copy
    (an unframed image)."""
    path: Path
    size: tuple[int, int]
    store: str | None
    lang: str


def expected_images(project: Project) -> list[ExpectedImage]:
    """Every screenshot the targets take, each Play feature graphic, then
    each unframed image."""
    screenshots = [ExpectedImage(job.out, job.target.size, job.target.store, job.lang)
                   for job in compose.panel_jobs(project, list(project.targets.values()))]
    graphics = [ExpectedImage(job.out, job.size, "play", job.lang)
                for job in compose.feature_jobs(project)]
    unframed = [ExpectedImage(job.out, job.size, None, job.image.lang)
                for job in compose.unframed_jobs(project)]
    return screenshots + graphics + unframed


def check_catalog(project: Project) -> list[Problem]:
    """Targets at sizes their slot does not take, too many panels for a
    slot, and stores without a slot they require."""
    found = []
    panels = len(project.storyboard)
    for target in project.targets.values():
        where = f"targets.{target.id}"
        wrong = target.slot.size_problem(target.size)
        if wrong:
            found.append(Problem("catalog", CONFIG_NAME, f"{where} is {_size(target.size)}, {wrong}"))
        if panels > target.slot.most:
            found.append(Problem("catalog", CONFIG_NAME,
                                 f"{where} gets {panels} panels, {target.slot.id} takes at most "
                                 f"{target.slot.most}"))
    graphic = project.feature_graphic
    if graphic is not None and graphic.size != catalog.FEATURE_GRAPHIC_SIZE:
        found.append(Problem("catalog", CONFIG_NAME,
                             f"feature_graphic.size is {_size(graphic.size)}, play takes "
                             f"{_size(catalog.FEATURE_GRAPHIC_SIZE)}"))
    slots = {target.slot.id for target in project.targets.values()}
    for store in project.stores:
        for requirement in catalog.required(store, project.runs_on(store)):
            if not slots & set(requirement.slots):
                found.append(Problem("catalog", CONFIG_NAME,
                                     f"{store} requires a target for {requirement.device} "
                                     f"(slot {' or '.join(requirement.slots)})"))
    return found


def check_images(project: Project) -> list[Problem]:
    """Each expected image: exists, PNG, exact size, opaque, sRGB, and its
    recorded copy within the copy rules."""
    found = []
    for image in expected_images(project):
        found.extend(Problem("image", project.rel(image.path), message)
                     for message in _image_problems(project, image))
    return found


def check_feature_copy(project: Project) -> list[Problem]:
    """Every text the feature page shows, per Play language. (The words
    themselves are checked in the feature graphic's image.)"""
    if project.feature_graphic is None:
        return []
    return [Problem("copy", project.rel(project.copy_path(lang)), f"feature_graphic.{key} missing")
            for lang, _ in project.store_languages("play")
            for key in compose.feature_copy(project, lang)[1]]


def check_storyboard(project: Project) -> list[Problem]:
    """Each panel's evidence: present, and every file it names exists."""
    where = project.rel(project.path("storyboard"))
    found = []
    for panel in project.storyboard:
        evidence = panel.get("evidence") or []
        if not evidence:
            found.append(Problem("storyboard", where, f"panel {panel['id']} has no evidence"))
        for entry in evidence:
            path = str(entry).partition("#")[0]
            if not isinstance(entry, str) or not (project.root / path).is_file():
                found.append(Problem("storyboard", where,
                                     f"panel {panel['id']} evidence {entry}: no file {path}"))
    return found


SOURCES: list[Callable[[Project], list[Problem]]] = [check_catalog, check_storyboard, check_images,
                                                     check_feature_copy]


def check(project: Project) -> list[Problem]:
    return [problem for source in SOURCES for problem in source(project)]


def run(project: Project) -> str:
    """The check stage: the console text when every check passes; otherwise
    a StageError naming the first problem. The log holds them all."""
    problems = check(project)
    log = project.log_path("check")
    log.write_text("".join(f"{p}\n" for p in problems), encoding="utf-8")
    if problems:
        raise StageError(f"{first_of(problems)} (log: {project.rel(log)})")
    return f"{plural(len(expected_images(project)), 'image')} pass"


# Platforms App Store images may not name (review guideline 2.3.10).
OTHER_PLATFORMS = ("Android", "Windows", "Linux", "Chromebook", "ChromeOS", "Chrome OS", "Galaxy",
                   "Samsung", "Google Play", "Play Store", "S Pen", "Huawei")


def other_platforms(text: str) -> list[str]:
    return [name for name in OTHER_PLATFORMS if re.search(rf"\b{re.escape(name)}\b", text)]


def text_problems(project: Project, lang: str, text: str, app_store: bool) -> list[str]:
    """[text]'s banned phrases in [lang], in config order, then, for text
    the App Store shows, the other platforms it names."""
    found = [f"says {claim}" for claim, patterns in project.banned_phrases(lang)
             if any(pattern.search(text) for pattern in patterns)]
    named = other_platforms(text) if app_store else []
    if named:
        found.append(f"names another platform ({', '.join(named)})")
    return found


PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
ALPHA_COLOUR_TYPES = (4, 6)


def _image_problems(project: Project, image: ExpectedImage) -> list[str]:
    if not image.path.is_file():
        return ["missing"]
    data = image.path.read_bytes()
    if not data.startswith(PNG_SIGNATURE):
        return ["not a PNG"]
    chunks = _chunks(data)
    if b"IHDR" not in chunks:
        return ["not a PNG"]
    width, height, _depth, colour_type = struct.unpack(">IIBB", chunks[b"IHDR"][:10])
    found = []
    if (width, height) != image.size:
        found.append(f"{width}x{height}, expected {_size(image.size)}")
    if colour_type in ALPHA_COLOUR_TYPES or b"tRNS" in chunks:
        found.append("has an alpha channel")
    profile = _profile_name(chunks)
    if profile is None:
        found.append("no colour profile, expected sRGB")
    elif "srgb" not in profile.lower():
        found.append(f"colour profile is {profile}, not sRGB")
    if image.store is not None:
        found.extend(_copy_problems(project, image, _recorded_copy(data)))
    return found


def _copy_problems(project: Project, image: ExpectedImage, copy: str | None) -> list[str]:
    app_store = image.store == "app_store"
    banned = project.banned_phrases(image.lang)
    if copy is None:
        return ["records no copy, so its text cannot be checked"] if app_store or banned else []
    return [f"its copy {problem}" for problem in text_problems(project, image.lang, copy, app_store)]


def _each_chunk(data: bytes):
    offset = len(PNG_SIGNATURE)
    while offset + 8 <= len(data):
        length, kind = struct.unpack(">I4s", data[offset:offset + 8])
        yield kind, data[offset + 8:offset + 8 + length]
        if kind == b"IEND":
            return
        offset += 12 + length


def _chunks(data: bytes) -> dict[bytes, bytes]:
    """The first chunk of each type, by type."""
    found: dict[bytes, bytes] = {}
    for kind, body in _each_chunk(data):
        found.setdefault(kind, body)
    return found


def _recorded_copy(data: bytes) -> str | None:
    """The iTXt "Copy" text the renderer records: every text the image shows."""
    for kind, body in _each_chunk(data):
        if kind != b"iTXt":
            continue
        keyword, _, rest = body.partition(b"\x00")
        if keyword != b"Copy" or len(rest) < 2:
            continue
        compressed = rest[0] == 1
        _language, _translated, text = rest[2:].split(b"\x00", 2)
        try:
            return (zlib.decompress(text) if compressed else text).decode("utf-8")
        except (zlib.error, UnicodeDecodeError):
            return None
    return None


def _profile_name(chunks: dict[bytes, bytes]) -> str | None:
    """"sRGB" for an sRGB chunk, an embedded ICC profile's description, or
    None for an untagged image."""
    if b"sRGB" in chunks:
        return "sRGB"
    if b"iCCP" not in chunks:
        return None
    iccp = chunks[b"iCCP"]
    try:
        return _icc_description(zlib.decompress(iccp[iccp.index(b"\x00") + 2:]))
    except (ValueError, zlib.error, struct.error):
        return "an unreadable ICC profile"


def _icc_description(icc: bytes) -> str:
    """The 'desc' tag of an ICC profile: v2 'desc' (ASCII) or v4 'mluc'
    (UTF-16BE, first record)."""
    (count,) = struct.unpack(">I", icc[128:132])
    for i in range(count):
        signature, offset, length = struct.unpack(">4sII", icc[132 + i * 12:144 + i * 12])
        if signature != b"desc":
            continue
        tag = icc[offset:offset + length]
        if tag[:4] == b"desc":
            (text_length,) = struct.unpack(">I", tag[8:12])
            return tag[12:12 + text_length].replace(b"\x00", b"").decode("latin-1")
        if tag[:4] == b"mluc":
            record_length, record_offset = struct.unpack(">II", tag[20:28])
            return tag[record_offset:record_offset + record_length].decode("utf-16-be")
    return "an unnamed ICC profile"


def _size(size: tuple[int, int]) -> str:
    return f"{size[0]}x{size[1]}"
