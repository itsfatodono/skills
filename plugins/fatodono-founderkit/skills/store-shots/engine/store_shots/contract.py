"""The adapter contract (docs/adapter.md). Capture and `adapter test` both
judge a run here, so passing means the same thing in both."""

from __future__ import annotations

import io
import json
import re
import shlex
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

from PIL import Image, ImageCms

from .project import Project, SceneRole, Target, member_landscape

CONTRACT = 1
REPORT = "report.txt"

# `adapter test` asks for its own scenes under this prefix; project scenes may not use it.
RESERVED_PREFIX = "__"
FULLBLEED = "__probe_fullbleed"
TRUNCATION = "__probe_truncation"
NO_SUCH_SCENE = "__no_such_scene"
PROBE_FILL = (255, 0, 255)
PROBE_TEXT = "store-shots truncation probe: this sentence is longer than its box"

# Devices of one frame kind differ slightly in shape (iPhone 6.9" and 6.5");
# within this share, a cluster device's screen counts as its frame's shape.
SHAPE_TOLERANCE = 0.01

CHECKED = re.compile(r"checked (?P<name>\S+/\S+) texts=(?P<texts>\d+)")


def raw_name(lang: str, target: Target, scene: str) -> str:
    """How the contract names a raw inside --out and in the report."""
    return f"{lang}/{target.id}-{scene}.png"


def scene_entry(project: Project, target: Target, scene: str, role: SceneRole) -> dict:
    """What a scene's raw must be, as the request states it."""
    width, height = target.screen
    if scene == FULLBLEED:
        return {"role": "screen", "size": [width, height], "probe": "fullbleed",
                "fill": "#%02X%02X%02X" % PROBE_FILL}
    if scene == TRUNCATION:
        return {"role": "screen", "size": [width, height], "probe": "truncation",
                "text": PROBE_TEXT}
    if role.kind == "screen":
        return {"role": "screen", "size": [width, height]}
    if role.kind == "card":
        return {"role": "card", "max_size": [width, height]}
    screens = project.member_screens(target, role.frame)
    entry = {"role": "member", "frame": role.frame}
    if screens:
        entry["shape"] = list(screens[0])
    else:
        entry["orientation"] = "landscape" if member_landscape(target, role.frame) else "portrait"
    return entry


def request(project: Project, target: Target, langs: list[str], scenes: list[str],
            out: Path) -> dict:
    """The request file's content: everything the adapter needs, so it never
    reads the project's own files."""
    roles = project.scene_roles(target)
    return {
        "contract": CONTRACT,
        "target": {"id": target.id, "store": target.store, "device": target.slot.device,
                   "frame": target.frame, "screen": list(target.screen)},
        "langs": {lang: project.languages[lang][target.store] for lang in langs},
        "scenes": {scene: scene_entry(project, target, scene, roles.get(scene, SceneRole("screen")))
                   for scene in scenes},
        "out": str(out),
        "report": str(out / REPORT),
    }


@dataclass
class Run:
    target: Target
    langs: list[str]
    scenes: list[str]
    out: Path
    code: int
    checked: dict[str, int] = field(default_factory=dict)
    issues: list[str] = field(default_factory=list)
    has_report: bool = False

    def raw(self, lang: str, scene: str) -> Path:
        return self.out / raw_name(lang, self.target, scene)

    def issues_of(self, lang: str, scene: str) -> list[str]:
        prefix = raw_name(lang, self.target, scene) + ":"
        return [issue for issue in self.issues if issue.startswith(prefix)]


def run(project: Project, target: Target, langs: list[str], scenes: list[str], out: Path,
        log: Path) -> Run:
    """[out] must not exist yet. The adapter's output is appended to [log]."""
    out.mkdir(parents=True)
    request_path = out.parent / f"{out.name}.request.json"
    content = request(project, target, langs, scenes, out)
    request_path.write_text(json.dumps(content, indent=1) + "\n", encoding="utf-8")
    command = project.config["adapter"]["command"]
    argv = shlex.split(command) if isinstance(command, str) else list(command)
    argv += ["--device", target.id, "--langs", ",".join(langs), "--scenes", ",".join(scenes),
             "--out", str(out), "--request", str(request_path)]
    with log.open("a", encoding="utf-8") as f:
        f.write(f"$ {shlex.join(argv)}\n")
        f.flush()
        done = subprocess.run(argv, cwd=project.root, stdout=f, stderr=subprocess.STDOUT)
    result = Run(target, langs, scenes, out, done.returncode)
    report = out / REPORT
    if report.is_file():
        result.has_report = True
        for line in report.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            checked = CHECKED.fullmatch(line)
            if checked:
                result.checked[checked["name"]] = int(checked["texts"])
            else:
                result.issues.append(line)
    return result


def problems(project: Project, result: Run, accepted: set[str] = frozenset()) -> list[str]:
    """Every way [result] breaks the contract; [accepted] report lines (the
    owner's, or a probe's expected one) are not problems."""
    found = []
    if result.code != 0:
        found.append(f"adapter exited {result.code}")
    if not result.has_report:
        found.append(f"adapter wrote no {REPORT}")
    found += [f"report: {issue}" for issue in result.issues if issue not in accepted]

    roles = project.scene_roles(result.target)
    textless = set(project.config["adapter"].get("textless") or [])
    expected = {result.out / REPORT}
    for lang in result.langs:
        for scene in result.scenes:
            path = result.raw(lang, scene)
            name = raw_name(lang, result.target, scene)
            expected.add(path)
            if not path.is_file():
                found.append(f"{name} missing")
                continue
            image_problem = _image_problem(project, result.target, scene,
                                           roles.get(scene, SceneRole("screen")), path)
            if image_problem:
                found.append(f"{name} {image_problem}")
            if name not in result.checked:
                found.append(f"{name} has no `checked` line in the report")
            elif result.checked[name] == 0 and scene not in textless and scene != FULLBLEED:
                found.append(f"{name}: the report checked no text; a screen with none goes"
                             f" in the config's adapter.textless")
    extra = sorted(p.relative_to(result.out).as_posix() for p in result.out.rglob("*")
                   if p.is_file() and p not in expected)
    if extra:
        found.append(f"unexpected file {extra[0]} in --out"
                     + (f" (+{len(extra) - 1} more)" if len(extra) > 1 else ""))
    if not found:
        found += _same_in_every_language(result, textless)
    return found


def _image_problem(project: Project, target: Target, scene: str, role: SceneRole,
                   path: Path) -> str | None:
    try:
        with Image.open(path) as image:
            size, kind = image.size, image.format
    except OSError:
        return "is not an image"
    if kind != "PNG":
        return f"is {kind}, not PNG"
    wrong = _size_problem(project, target, role, size)
    return f"is {size[0]}x{size[1]}, {wrong}" if wrong else None


def _size_problem(project: Project, target: Target, role: SceneRole,
                  size: tuple[int, int]) -> str | None:
    width, height = target.screen
    if role.kind == "screen":
        return None if size == target.screen else f"expected {width}x{height}"
    if role.kind == "card":
        if size[0] > width or size[1] > height:
            return f"larger than the {width}x{height} screen"
        return None
    screens = project.member_screens(target, role.frame)
    if not screens:
        landscape = member_landscape(target, role.frame)
        if (size[0] > size[1]) == landscape:
            return None
        return f"not a {'landscape' if landscape else 'portrait'} {role.frame} screen"
    ratio = size[1] / size[0]
    if any(abs(ratio - h / w) <= SHAPE_TOLERANCE * h / w for w, h in screens):
        return None
    return f"not the shape of the {screens[0][0]}x{screens[0][1]} {role.frame} screen"


def srgb(path: Path) -> Image.Image:
    """[path] as RGBA in sRGB, converted through its embedded colour profile
    (a simulator's Display P3, say) when it has one."""
    with Image.open(path) as image:
        profile = image.info.get("icc_profile")
        converted = image.convert("RGBA")
    if profile:
        try:
            source = ImageCms.ImageCmsProfile(io.BytesIO(profile))
            converted = ImageCms.profileToProfile(converted, source, ImageCms.createProfile("sRGB"),
                                                  outputMode="RGBA")
        except (OSError, ImageCms.PyCMSError):
            pass
    return converted


def pixels(path: Path) -> bytes:
    """[path]'s size and sRGB pixels, so images differing only in their
    encoding or colour profile compare equal."""
    image = srgb(path)
    return repr(image.size).encode() + image.tobytes()


def _same_in_every_language(result: Run, textless: set[str]) -> list[str]:
    if len(result.langs) < 2:
        return []
    found = []
    for scene in result.scenes:
        if scene in textless or scene.startswith(RESERVED_PREFIX):
            continue
        shots = {pixels(result.raw(lang, scene)) for lang in result.langs}
        if len(shots) == 1:
            found.append(f"{result.target.id}-{scene} is the same image in every language"
                         f" ({', '.join(result.langs)}): does the adapter set the app's locale?")
    return found
