"""The one command-line entry: `store-shots <command>`. Each command prints
one line per stage and ends with the exit code; full output goes to logs."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Callable
from pathlib import Path
from typing import NamedTuple

from . import adapter_test, checks, init, preview
from .build import build, capture_line, run_stage, sheet_line
from .capture import stale_raws
from .errors import StageError
from .project import ConfigError, Project, find_root
from .status import status


def _build(project: Project, args: argparse.Namespace) -> int:
    return 0 if build(project, print) else 1


def _check(project: Project, args: argparse.Namespace) -> int:
    return 0 if run_stage("check", lambda: checks.run(project), print) else 1


def _sheet(project: Project, args: argparse.Namespace) -> int:
    return 0 if run_stage("sheet", lambda: sheet_line(project), print) else 1


def _status(project: Project, args: argparse.Namespace) -> int:
    for line in status(project):
        print(line)
    return 0


def _preview_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--lang", metavar="LANG",
                        help="the copy language to preview (default: the config's first)")
    parser.add_argument("--panel", action="append", metavar="ID",
                        help="only this panel (repeatable; default: every panel)")


def _preview(project: Project, args: argparse.Namespace) -> int:
    run = lambda: preview.preview(project, args.lang, args.panel)
    return 0 if run_stage("preview", run, print) else 1


def _capture_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--force", action="store_true",
                        help="re-capture even the raws whose inputs have not changed")
    parser.add_argument("--target", action="append", metavar="ID",
                        help="only this target (repeatable)")
    parser.add_argument("--scene", action="append", metavar="NAME",
                        help="only this scene (repeatable)")


def _capture(project: Project, args: argparse.Namespace) -> int:
    targets = list(project.targets.values())
    for wanted, known, what in [(args.target, [t.id for t in targets], "target"),
                                (args.scene, {s for t in targets for s in project.scenes(t)}, "scene")]:
        unknown = sorted(set(wanted or []) - set(known))
        if unknown:
            raise ConfigError(f"no {what} {', '.join(unknown)}; known: {', '.join(sorted(known))}")
    if args.target:
        targets = [t for t in targets if t.id in args.target]
    stale = stale_raws(project, targets, scenes=args.scene, force=args.force)
    return 0 if run_stage("capture", lambda: capture_line(project, stale), print) else 1


def _adapter_arguments(parser: argparse.ArgumentParser) -> None:
    actions = parser.add_subparsers(dest="action", required=True)
    test = actions.add_parser(
        "test", help="hold the adapter to its contract in gates: runs, unknown-scene, full-bleed,"
                     " cut-off-text, one-scene, languages, every-scene, repeatable; a target"
                     " stops at its first failing gate, and no raw is written",
        description="hold the adapter to its contract in gates (docs/adapter.md)")
    test.add_argument("--target", action="append", metavar="ID", help="only this target (repeatable)")


def _adapter(project: Project, args: argparse.Namespace) -> int:
    targets = list(project.targets.values())
    unknown = sorted(set(args.target or []) - {t.id for t in targets})
    if unknown:
        raise ConfigError(f"no target {', '.join(unknown)}; known: {', '.join(t.id for t in targets)}")
    if args.target:
        targets = [t for t in targets if t.id in args.target]
    return 0 if adapter_test.test(project, targets, print) else 1


def _init_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--runs-on", action="append", default=[], metavar="STORE=DEVICES",
                        help="a store and the devices the app runs on in it, e.g."
                             " app_store=iphone,ipad,mac or play=phone,tablet (once per store)")
    parser.add_argument("--lang", action="append", default=[], metavar="LANG=CODE",
                        help="a copy language and its code in every store, e.g. en=en-US"
                             " (repeatable)")
    parser.add_argument("--copy", default=init.DEFAULT_COPY, metavar="DIR",
                        help="the copy files' folder, relative to the project, e.g. beside the"
                             " app's other store texts; the config's paths records it"
                             " (default: texts)")


def _init(root: Path, args: argparse.Namespace) -> int:
    write = lambda: init.init(root, args.runs_on, args.lang, args.copy)
    return 0 if run_stage("init", write, print) else 1


class Command(NamedTuple):
    help: str
    run: Callable[[Path, argparse.Namespace], int]
    arguments: Callable[[argparse.ArgumentParser], None] | None


def _on_project(run: Callable[[Project, argparse.Namespace], int]
                ) -> Callable[[Path, argparse.Namespace], int]:
    return lambda root, args: run(Project(root), args)


COMMANDS = {
    "init": Command("write a new project into the project folder (default: the current folder):"
                    " config, layout and an adapter skeleton, with an empty storyboard and copy",
                    _init, _init_arguments),
    "build": Command("run the stages capture, compose, check and sheet; capture and compose"
                     " redo only what is stale", _on_project(_build), None),
    "status": Command("list each stale output and the input that made it stale, by stage",
                      _on_project(_status), None),
    "capture": Command("capture the stale raws only, or with --force every chosen one",
                       _on_project(_capture), _capture_arguments),
    "adapter": Command("test the project's adapter against the contract, gate by gate, before"
                       " or after its scenes exist (`adapter test`)",
                       _on_project(_adapter), _adapter_arguments),
    "check": Command("check the catalog, the images and their copy without building",
                     _on_project(_check), None),
    "preview": Command("render the layout as it looks now in one language, every panel on every"
                       " target and the feature graphic, on the raws and copy so far and"
                       " placeholder screens and texts for the rest, into one sheet"
                       " (.store-shots/preview/<lang>/sheet.png); records nothing, so no output"
                       " goes stale", _on_project(_preview), _preview_arguments),
    "sheet": Command("refresh the contact sheets from the composed images",
                     _on_project(_sheet), None),
}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="store-shots", description=" ".join(__doc__.split()))
    parser.add_argument("--project", type=Path,
                        help="folder holding store-shots.yaml, or the one init writes it into"
                             " (default: the current folder or above; for init the current folder)")
    commands = parser.add_subparsers(dest="command", required=True)
    for name, command in COMMANDS.items():
        sub = commands.add_parser(name, help=command.help, description=command.help)
        if command.arguments:
            command.arguments(sub)
    args = parser.parse_args(argv)

    try:
        # A new project has no config to find yet.
        root = args.project or (Path.cwd() if args.command == "init" else find_root(Path.cwd()))
        code = COMMANDS[args.command].run(root.resolve(), args)
    except StageError as e:
        print(f"{args.command}: FAILED, {e}")
        code = 1
    print(f"exit {code}")
    sys.stdout.flush()
    return code


if __name__ == "__main__":
    sys.exit(main())
