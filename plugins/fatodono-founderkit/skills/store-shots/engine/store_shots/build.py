"""`build`: the stages in order, each reported as one console line. A stage
that fails stops the build; its line holds the reason, its log the rest.
Capture and compose redo only what is stale."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

from . import checks, sheet
from .capture import StaleRaw, capture_stale, stale_raws
from .compose import compose, feature_jobs, panel_jobs, unframed_jobs
from .errors import StageError
from .project import Project
from .words import plural


@dataclass(frozen=True)
class StageLine:
    stage: str
    ok: bool
    text: str

    def __str__(self) -> str:
        return f"{self.stage}: {'ok' if self.ok else 'FAILED'}, {self.text}"


def run_stage(name: str, run: Callable[[], str], say: Callable[[StageLine], None]) -> bool:
    try:
        text = run()
    except StageError as e:
        say(StageLine(name, False, str(e)))
        return False
    say(StageLine(name, True, text))
    return True


def capture_line(project: Project, stale: list[StaleRaw]) -> str:
    if not stale:
        return "nothing stale"
    runs = capture_stale(project, stale)
    targets = {raw.target.id for raw in stale}
    return f"{plural(len(stale), 'raw')} on {plural(len(targets), 'target')} in " \
           f"{plural(runs, 'adapter run')} (logs: {project.rel(project.path('logs'))}/capture-*.log)"


def build(project: Project, say: Callable[[StageLine], None]) -> bool:
    """Runs capture, compose, check and sheet; [say] gets each stage's
    line as it ends. Returns whether every stage passed."""
    targets = list(project.targets.values())
    images = [*panel_jobs(project, targets), *feature_jobs(project), *unframed_jobs(project)]

    def run_compose() -> str:
        todo = [job for job in images if job.why_stale()]
        if not todo:
            return f"nothing stale ({plural(len(images), 'image')} current)"
        log = compose(project, todo)
        return f"{plural(len(todo), 'image')} of {len(images)} (log: {project.rel(log)})"

    return (run_stage("capture", lambda: capture_line(project, stale_raws(project, targets)), say)
            and run_stage("compose", run_compose, say)
            and run_stage("check", lambda: checks.run(project), say)
            and run_stage("sheet", lambda: sheet_line(project), say))


def sheet_line(project: Project) -> str:
    written, fresh = sheet.refresh(project)
    return f"{plural(written, 'sheet')} written, {fresh} up to date " \
           f"(in {project.rel(project.path('sheets'))})"

