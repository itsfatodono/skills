"""`adapter test`: each gate is its own adapter run, so a failure points at
one thing to fix. It writes no raw, and the gates that need project scenes
skip until the storyboard names some.
"""

from __future__ import annotations

import shutil
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageChops

from . import contract
from .contract import FULLBLEED, NO_SUCH_SCENE, PROBE_FILL, TRUNCATION, raw_name
from .project import Project, Target
from .words import first_of, plural

# How far a full-bleed pixel may be from the probe fill, per channel, after
# conversion to sRGB.
FILL_TOLERANCE = 16


@dataclass(frozen=True)
class GateLine:
    target: str
    gate: str
    result: str  # ok, FAILED or skipped
    text: str

    def __str__(self) -> str:
        return f"adapter {self.target} {self.gate}: {self.result}, {self.text}"


class _Fail(Exception):
    pass


class _Skip(Exception):
    pass


class _TargetTest:

    def __init__(self, project: Project, target: Target):
        self.project = project
        self.target = target
        self.langs = project.target_languages(target)
        self.scenes = project.scenes(target)
        self.log = project.log_path(f"adapter-test-{target.id}")
        self.log.write_text("", encoding="utf-8")
        self.work = project.path("work") / "adapter-test" / target.id
        shutil.rmtree(self.work, ignore_errors=True)
        self.work.mkdir(parents=True)
        self.count = 0
        self.last: contract.Run | None = None

    def run(self, langs: list[str], scenes: list[str]) -> contract.Run:
        self.count += 1
        with self.log.open("a", encoding="utf-8") as f:
            f.write(f"\n# run {self.count}\n")
        return contract.run(self.project, self.target, langs, scenes,
                            self.work / f"run-{self.count}", self.log)

    def must_pass(self, result: contract.Run, accepted: set[str] = frozenset()) -> None:
        owner = set(self.project.config["adapter"].get("accepted") or [])
        problems = contract.problems(self.project, result, owner | accepted)
        if problems:
            raise _Fail(first_of(problems))
        self.last = result

    # The gates, in order. Each returns its ok text, or raises _Fail or _Skip.

    def runs(self) -> str:
        self.must_pass(self.run(self.langs[:1], []))
        return "no scenes asked, exit 0, a report and nothing else"

    def unknown_scene(self) -> str:
        lang = self.langs[0]
        result = self.run([lang], [NO_SUCH_SCENE])
        if result.code != 0:
            return f"exited {result.code} on a scene it does not have"
        if result.issues_of(lang, NO_SUCH_SCENE):
            return "reported the scene it does not have"
        raise _Fail(f"exit 0 and no report line for {raw_name(lang, self.target, NO_SUCH_SCENE)}:"
                    f" a scene the adapter does not have must fail the run or be reported")

    def full_bleed(self) -> str:
        lang = self.langs[0]
        result = self.run([lang], [FULLBLEED])
        self.must_pass(result)
        _require_fill(result.raw(lang, FULLBLEED))
        return "the probe fill covers the screen edge to edge"

    def cut_off_text(self) -> str:
        lang = self.langs[0]
        result = self.run([lang], [TRUNCATION])
        found = result.issues_of(lang, TRUNCATION)
        if not found and result.code == 0:
            raise _Fail(f"no report line for {raw_name(lang, self.target, TRUNCATION)}: the"
                        f" cut-off text check missed the probe's text")
        self.must_pass(result, set(found))
        return f"reported {found[0]}"

    def one_scene(self) -> str:
        if not self.scenes:
            raise _Skip(f"the storyboard names no scene for {self.target.id} yet")
        self.must_pass(self.run(self.langs[:1], self.scenes[:1]))
        return f"{self.scenes[0]} in {self.langs[0]}"

    def languages(self) -> str:
        if not self.scenes:
            raise _Skip("no scene yet")
        if len(self.langs) < 2:
            raise _Skip(f"{self.target.store} has one language")
        self.must_pass(self.run(self.langs, self.scenes[:1]))
        return f"{self.scenes[0]} in {', '.join(self.langs)}, each its own image"

    def every_scene(self) -> str:
        if len(self.scenes) < 2:
            raise _Skip("one scene or none, tested above" if self.scenes else "no scene yet")
        self.must_pass(self.run(self.langs, self.scenes))
        return f"{len(self.scenes)} scenes in {plural(len(self.langs), 'language')}"

    def repeatable(self) -> str:
        first = self.last
        if first is None or not first.scenes or first.scenes == [FULLBLEED]:
            first = self.run(self.langs[:1], [TRUNCATION])
        again = self.run(first.langs, first.scenes)
        accepted = {issue for lang in first.langs for issue in first.issues_of(lang, TRUNCATION)}
        self.must_pass(again, accepted)
        differ = [raw_name(lang, self.target, scene) for lang in first.langs
                  for scene in first.scenes
                  if contract.pixels(first.raw(lang, scene)) != contract.pixels(again.raw(lang, scene))]
        if differ:
            more = f", and {plural(len(differ) - 1, 'other raw')}" if len(differ) > 1 else ""
            raise _Fail(f"{differ[0]} differs between two runs of the same request{more}: a clock,"
                        f" an animation, a cursor or random demo content?")
        return f"two runs, the same pixels in {len(first.langs) * len(first.scenes)} raws"


GATES: list[tuple[str, Callable[[_TargetTest], str]]] = [
    ("runs", _TargetTest.runs),
    ("unknown-scene", _TargetTest.unknown_scene),
    ("full-bleed", _TargetTest.full_bleed),
    ("cut-off-text", _TargetTest.cut_off_text),
    ("one-scene", _TargetTest.one_scene),
    ("languages", _TargetTest.languages),
    ("every-scene", _TargetTest.every_scene),
    ("repeatable", _TargetTest.repeatable),
]


def _require_fill(path: Path) -> None:
    rgb = contract.srgb(path).convert("RGB")
    width, height = rgb.size
    diff = ImageChops.difference(rgb, Image.new("RGB", rgb.size, PROBE_FILL))
    off = ImageChops.lighter(ImageChops.lighter(*diff.split()[:2]), diff.split()[2])
    box = off.point(lambda v: 255 if v > FILL_TOLERANCE else 0).getbbox()
    if box is None:
        return None
    left, top, right, bottom = box
    where = (" at the top: a status bar or a safe-area inset?" if top == 0 and bottom < height
             else " at the bottom: a home indicator or a navigation bar?" if bottom == height and top > 0
             else ": is the probe drawn at the full screen size?")
    raise _Fail(f"pixels from ({left},{top}) to ({right},{bottom}) of {width}x{height} are not the"
                f" probe fill #%02X%02X%02X{where}" % PROBE_FILL)


def test(project: Project, targets: list[Target], say: Callable[[GateLine], None]) -> bool:
    """Stops a target at its first failing gate; the other targets still run.
    Returns whether no gate failed."""
    passed = True
    for target in targets:
        state = _TargetTest(project, target)
        log = project.rel(state.log)
        for name, gate in GATES:
            try:
                say(GateLine(target.id, name, "ok", gate(state)))
            except _Skip as e:
                say(GateLine(target.id, name, "skipped", str(e)))
            except _Fail as e:
                say(GateLine(target.id, name, "FAILED", f"{e} (log: {log})"))
                passed = False
                break
        else:
            shutil.rmtree(state.work, ignore_errors=True)
    return passed
