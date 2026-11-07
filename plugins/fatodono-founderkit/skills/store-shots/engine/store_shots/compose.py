"""The compose stage: frames raw screens with the mockups, the project's
layout page and its copy into store images, renders the Play feature
graphic per Play language from the layout's feature page, and saves each
unframed image from its raw.

Each image's sidecar records its raws, its copy entries, its storyboard
panel, its target, its own placement, the layout files its page uses, every
mockup file and the renderer, so a change to one of them re-composes exactly
the images that use it. A layout file belongs to the page of its own stem
(`panel.*` to the panels, `feature.*` to the feature graphic); every other
layout file is shared by both."""

from __future__ import annotations

import re
from dataclasses import dataclass
from functools import cached_property
from pathlib import Path

from PIL import Image

from . import layout, render, state
from .errors import StageError
from .project import STATUSES, Project, Target, Unframed

RENDERER = Path(render.__file__).resolve()
PANEL_PAGE = "panel.html"
FEATURE_PAGE = "feature.html"


# Editing these re-composes nothing.
UNSHOWN_PANEL_FIELDS = ("claim", "evidence")


def _page_data(frame: str, copy: dict[str, str], place: dict, **shown) -> dict:
    """What the layout page takes (see mockups/mockup.js); [shown] fills the
    places the image shows."""
    return {"frame": frame, "orientation": None, "panel": None, "status": None, "copy": copy,
            "screen": None, "card": None, "badge": None, "cluster": None, "place": place, **shown}


def _render(project: Project, page: str, data: dict, size: tuple[int, int], out: Path,
            texts: list[str], log: Path) -> None:
    layout_page = project.path("layout") / page
    if not layout_page.is_file():
        raise StageError(f"no layout page at {project.rel(layout_page)}")
    try:
        render.shoot(render.page(layout_page, data), size, out, texts,
                     project.path("work") / "render", log)
    except StageError as e:
        raise StageError(f"{e} (log: {project.rel(log)})") from None


@dataclass
class PanelJob:
    """One store image: a panel on a target in one language."""
    project: Project
    target: Target
    lang: str
    code: str
    panel: dict

    @property
    def out(self) -> Path:
        return self.project.screenshot_path(self.target.store, self.code, self.target.id,
                                            self.panel["id"])

    @property
    def size(self) -> tuple[int, int]:
        return self.target.size

    @cached_property
    def members(self) -> list[dict] | None:
        return self.project.cluster(self.panel, self.target.store)

    @property
    def raws(self) -> dict[str, Path]:
        """Every raw the image shows, by scene."""
        if self.members is not None:
            scenes = [member["scene"] for member in self.members]
        else:
            scenes = [self.panel["scene"], *([self.panel["card"]] if self.panel.get("card") else [])]
        return {scene: self.project.raw_path(self.target.id, self.lang, scene) for scene in scenes}

    @cached_property
    def place(self) -> dict:
        """This image's placement, merged from the layout's placement data."""
        return layout.resolve(layout.load(self.project.path("layout")), self.target.frame,
                              self.target.id, self.panel["id"], self.target.turned)

    def data(self) -> dict:
        """The layout page's data; the raws exist."""
        panel, target = self.panel, self.target
        raws = {scene: _image(path) for scene, path in self.raws.items()}
        shown = {"panel": panel["id"], "status": panel.get("status", STATUSES[0]),
                 "orientation": "landscape" if target.landscape else "portrait"}
        if self.members is not None:
            shown["cluster"] = [{"frame": m["frame"], **raws[m["scene"]]} for m in self.members]
            devices = [f"cluster.{m['frame']}" for m in self.members]
        else:
            shown["screen"] = raws[panel["scene"]]
            shown["card"] = raws.get(panel.get("card"))
            devices = ["device"]
        if panel.get("badge"):
            shown["badge"] = {"icon": _icon(self.project, panel["badge"]["icon"])}
        for place in devices:
            if "--screen-w" not in _at(self.place, place):
                raise StageError(f"{layout.PLACEMENT}: no {place} --screen-w for {target.id}"
                                 f" ({target.frame}) in {panel['id']}")
        return _page_data(target.frame, self.words, self.place, **shown)

    @cached_property
    def words(self) -> dict[str, str]:
        return self.project.panel_copy(self.lang, self.panel, self.target.store)

    def inputs(self) -> dict[str, str]:
        """Each input by the name `status` reports it under; the raws must exist."""
        project = self.project
        shown = {k: v for k, v in self.panel.items() if k not in UNSHOWN_PANEL_FIELDS}
        found = {f"raw {project.rel(raw)}": state.digest_file(raw) for raw in self.raws.values()}
        found[f"copy {self.lang} panels.{self.panel['id']}"] = state.digest_value(self.words)
        found[f"storyboard {self.panel['id']}"] = state.digest_value(shown)
        found["target"] = state.digest_value([self.target.slot.id, list(self.target.size)])
        found[f"placement {self.target.id} {self.panel['id']}"] = state.digest_value(self.place)
        return found | _shared_inputs(project, PANEL_PAGE)

    def why_stale(self, stale_raws: set[Path] = frozenset()) -> str | None:
        """None when the image is current; [stale_raws] are raws a capture is
        about to replace."""
        return _why_stale(self, stale_raws)

    def write(self, log: Path) -> None:
        _render(self.project, PANEL_PAGE, self.data(), self.size, self.out,
                list(self.words.values()), log)


@dataclass
class FeatureJob:
    """The Play feature graphic in one Play language."""
    project: Project
    lang: str
    code: str

    @property
    def raws(self) -> dict[str, Path]:
        return {}

    @property
    def out(self) -> Path:
        return self.project.feature_graphic_path(self.code)

    @property
    def size(self) -> tuple[int, int]:
        return self.project.feature_graphic.size

    @cached_property
    def place(self) -> dict:
        return layout.feature(layout.load(self.project.path("layout")))

    @cached_property
    def words(self) -> dict[str, str]:
        words, missing = feature_copy(self.project, self.lang)
        if missing:
            raise StageError(f"{self.project.rel(self.project.copy_path(self.lang))}: "
                             f"feature_graphic.{missing[0]} missing")
        return words

    def inputs(self) -> dict[str, str]:
        found = {
            f"copy {self.lang} feature_graphic": state.digest_value(self.words),
            "size": state.digest_value(list(self.size)),
            f"placement {layout.FEATURE_GRAPHIC_KEY}": state.digest_value(self.place),
        }
        return found | _shared_inputs(self.project, FEATURE_PAGE)

    def why_stale(self, stale_raws: set[Path] = frozenset()) -> str | None:
        return state.why_stale(self.out, self.inputs())

    def write(self, log: Path) -> None:
        _render(self.project, FEATURE_PAGE, _page_data("feature", self.words, self.place),
                self.size, self.out, list(self.words.values()), log)


@dataclass
class UnframedJob:
    """An unframed image: its scene's raw as captured, made opaque and sRGB."""
    project: Project
    image: Unframed

    @property
    def target(self) -> Target:
        return self.image.target

    @property
    def raws(self) -> dict[str, Path]:
        image = self.image
        return {image.scene: self.project.raw_path(image.target.id, image.lang, image.scene)}

    @property
    def out(self) -> Path:
        return self.project.unframed_path(self.image.name)

    @property
    def size(self) -> tuple[int, int]:
        return self.image.target.screen

    def inputs(self) -> dict[str, str]:
        (raw,) = self.raws.values()
        return {f"raw {self.project.rel(raw)}": state.digest_file(raw),
                "renderer": state.digest_file(RENDERER)}

    def why_stale(self, stale_raws: set[Path] = frozenset()) -> str | None:
        return _why_stale(self, stale_raws)

    def write(self, log: Path) -> None:
        (raw,) = self.raws.values()
        render.save_opaque(raw, self.out)


def _why_stale(job: PanelJob | UnframedJob, stale_raws: set[Path]) -> str | None:
    for raw in job.raws.values():
        if raw in stale_raws:
            return f"raw {job.project.rel(raw)} to be captured"
        if not raw.is_file():
            return f"raw {job.project.rel(raw)} missing"
    return state.why_stale(job.out, job.inputs())


def unframed_jobs(project: Project) -> list[UnframedJob]:
    return [UnframedJob(project, image) for image in project.unframed]


def feature_keys(project: Project) -> list[str]:
    """The copy keys the feature page shows, in page order."""
    page = project.path("layout") / FEATURE_PAGE
    if not page.is_file():
        raise StageError(f"no feature graphic page at {project.rel(page)}")
    return list(dict.fromkeys(re.findall(r'data-copy="([^"]+)"', page.read_text(encoding="utf-8"))))


def feature_copy(project: Project, lang: str) -> tuple[dict[str, str], list[str]]:
    """The feature graphic's texts in [lang] by key, and the keys its copy lacks."""
    section = project.copy(lang).get("feature_graphic") or {}
    keys = feature_keys(project)
    words = {key: section[key] for key in keys if isinstance(section.get(key), str) and section[key]}
    return words, [key for key in keys if key not in words]


def feature_jobs(project: Project) -> list[FeatureJob]:
    """A feature graphic per Play language, when the project has one."""
    if project.feature_graphic is None:
        return []
    return [FeatureJob(project, lang, code) for lang, code in project.store_languages("play")]


def _shared_inputs(project: Project, page: str) -> dict[str, str]:
    """The inputs every image of [page] shares: the layout files that page
    uses (not placement, which each image records as its own), the mockups
    and the renderer."""
    found = {}
    folder = project.path("layout")
    other = {Path(PANEL_PAGE).stem, Path(FEATURE_PAGE).stem} - {Path(page).stem}
    for path in _files(folder):
        if path != folder / layout.PLACEMENT and path.stem not in other:
            found[f"layout {project.rel(path)}"] = state.digest_file(path)
    for path in _files(render.MOCKUPS):
        found[f"mockup {path.relative_to(render.MOCKUPS).as_posix()}"] = state.digest_file(path)
    found["renderer"] = state.digest_file(RENDERER)
    return found


def _files(folder: Path) -> list[Path]:
    return sorted(p for p in folder.rglob("*") if p.is_file() and p.name != ".DS_Store")


def panel_jobs(project: Project, targets: list[Target]) -> list[PanelJob]:
    """Every image [targets] take: each panel in each of their store's languages."""
    return [PanelJob(project, target, lang, code, panel)
            for target in targets
            for lang, code in project.store_languages(target.store)
            for panel in project.storyboard]


Job = PanelJob | FeatureJob | UnframedJob


def compose(project: Project, todo: list[Job]) -> Path:
    """Writes [todo] and records each image's inputs. Returns the log path."""
    log = project.log_path("compose")
    log.write_text("", encoding="utf-8")
    for job in todo:
        for raw in job.raws.values():
            if not raw.is_file():
                raise StageError(f"{project.rel(raw)} missing; capture {job.target.id} first")
        inputs = job.inputs()
        job.write(log)
        state.record(job.out, inputs)
    return log


def _image(path: Path) -> dict:
    """A raw as the page takes it: its URL and its height / width."""
    with Image.open(path) as image:
        return {"src": path.resolve().as_uri(), "ratio": image.height / image.width}


def _icon(project: Project, name: str) -> str:
    """A badge icon's SVG markup, from the layout's icons/ folder."""
    path = project.path("layout") / "icons" / f"{name}.svg"
    if not path.is_file():
        raise StageError(f"no badge icon at {project.rel(path)}")
    return path.read_text(encoding="utf-8")


def _at(place: dict, name: str) -> dict:
    for key in name.split("."):
        place = place.get(key) or {}
    return place
