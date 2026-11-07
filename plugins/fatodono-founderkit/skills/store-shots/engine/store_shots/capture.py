"""The capture stage: runs the project's adapter and holds its output to the
adapter contract (contract.py, docs/adapter.md) before any raw reaches the project.

Each raw's sidecar records the adapter command, the files its `inputs` globs
match, the scene and the target, so a change to any of them makes exactly
those raws stale.
"""

from __future__ import annotations

import shutil
from dataclasses import dataclass
from pathlib import Path

from . import contract, state
from .errors import StageError
from .project import Project, Target
from .words import first_of


@dataclass(frozen=True)
class StaleRaw:
    target: Target
    lang: str
    scene: str
    path: Path
    reason: str


def raw_inputs(project: Project, target: Target, lang: str, scene: str) -> dict[str, str]:
    adapter = project.config["adapter"]
    patterns = [p.replace("{lang}", lang).replace("{scene}", scene)
                for p in adapter.get("inputs") or []]
    outputs = [project.path(name) for name in ("raw", "out", "logs", "work", "sheets")]
    return {
        "adapter command": state.digest_value(adapter["command"]),
        "adapter inputs": state.digest_globs(project.root, patterns, outputs),
        "scene": state.digest_value(scene),
        "target": state.digest_value([target.slot.id, list(target.size), list(target.screen)]),
    }


def stale_raws(project: Project, targets: list[Target], scenes: list[str] | None = None,
               force: bool = False) -> list[StaleRaw]:
    """Every raw of [targets] (of [scenes] only, when given) that needs a
    capture, with the reason; with [force], every one of them."""
    found = []
    for target in targets:
        for lang in project.target_languages(target):
            for scene in project.scenes(target, lang):
                if scenes is not None and scene not in scenes:
                    continue
                raw = project.raw_path(target.id, lang, scene)
                reason = "forced" if force else state.why_stale(
                    raw, raw_inputs(project, target, lang, scene))
                if reason:
                    found.append(StaleRaw(target, lang, scene, raw, reason))
    return found


def capture_stale(project: Project, stale: list[StaleRaw]) -> int:
    """Captures [stale] in as few adapter runs as it can: one per target and
    set of scenes stale in the same languages. Returns the run count."""
    targets = {raw.target.id: raw.target for raw in stale}
    by_lang: dict[tuple[str, str], list[str]] = {}
    for raw in stale:
        by_lang.setdefault((raw.target.id, raw.lang), []).append(raw.scene)
    runs: dict[tuple[str, tuple[str, ...]], list[str]] = {}
    for (target_id, lang), scenes in by_lang.items():
        runs.setdefault((target_id, tuple(scenes)), []).append(lang)
    for target_id in targets:
        project.log_path(f"capture-{target_id}").write_text("", encoding="utf-8")
    for (target_id, scenes), langs in runs.items():
        capture(project, targets[target_id], langs, list(scenes))
    return len(runs)


def capture(project: Project, target: Target, langs: list[str], scenes: list[str]) -> Path:
    """Captures [scenes] in [langs] on [target] and merges them over its raws,
    leaving every other raw as it was. Returns the log path (appended to);
    raises StageError, with no raw changed, when the output breaks the contract."""
    log = project.log_path(f"capture-{target.id}")
    inputs = {(lang, scene): raw_inputs(project, target, lang, scene)
              for lang in langs for scene in scenes}
    work = project.path("work") / "capture"
    out = work / target.id
    shutil.rmtree(out, ignore_errors=True)
    work.mkdir(parents=True, exist_ok=True)

    result = contract.run(project, target, langs, scenes, out, log)
    accepted = set(project.config["adapter"].get("accepted") or [])
    problems = contract.problems(project, result, accepted)
    if problems:
        with log.open("a", encoding="utf-8") as f:
            f.write("contract problems:\n" + "".join(f"  {p}\n" for p in problems))
        raise StageError(f"{target.id}: {first_of(problems)} (log: {project.rel(log)})")

    for lang in langs:
        folder = project.raw_dir(target.id, lang)
        folder.mkdir(parents=True, exist_ok=True)
        for scene in scenes:
            name = f"{target.id}-{scene}.png"
            shutil.copyfile(result.raw(lang, scene), folder / name)
            state.record(folder / name, inputs[lang, scene])
    shutil.rmtree(out)
    return log
