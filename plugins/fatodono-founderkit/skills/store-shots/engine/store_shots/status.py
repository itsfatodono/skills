"""`status`: what each stage would redo and why, without running anything.
The console lists at most [SHOWN] outputs per stage; the log lists all."""

from __future__ import annotations

from .capture import stale_raws
from .compose import feature_jobs, panel_jobs, unframed_jobs
from .project import Project
from .words import plural

SHOWN = 20


def stages(project: Project) -> list[tuple[str, int, str, list[tuple[str, str]]]]:
    """Per stage: its name, its output count, the word for one output, and
    (output, reason) for each stale one."""
    targets = list(project.targets.values())
    raws = stale_raws(project, targets)
    all_raws = sum(len(project.scenes(target, lang))
                   for target in targets for lang in project.target_languages(target))
    images = [*panel_jobs(project, targets), *feature_jobs(project), *unframed_jobs(project)]
    captured = {r.path for r in raws}
    stale_images = [(job, reason) for job in images if (reason := job.why_stale(captured))]

    return [
        ("capture", all_raws, "raw",
         [(project.rel(r.path), r.reason) for r in raws]),
        ("compose", len(images), "image",
         [(project.rel(job.out), reason) for job, reason in stale_images]),
    ]


def status(project: Project) -> list[str]:
    """The console lines: per stage a summary, then each stale output with
    the input that made it stale."""
    log = project.log_path("status")
    console, full = [], []
    for name, total, word, stale in stages(project):
        head = f"{name}: {len(stale)} stale of {total}" if stale \
            else f"{name}: nothing stale ({plural(total, word)} current)"
        items = [f"  {path}: {reason}" for path, reason in stale]
        full += [head, *items]
        console += [head, *items[:SHOWN]]
        if len(items) > SHOWN:
            console.append(f"  (+{len(items) - SHOWN} more; all in {project.rel(log)})")
    log.write_text("".join(f"{line}\n" for line in full), encoding="utf-8")
    return console
