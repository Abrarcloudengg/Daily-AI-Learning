"""Command line interface.

One entry point, several verbs, and a single place where exceptions become exit
codes. Anything raised as a :class:`DailyAILearningError` is printed as a
readable message; anything else is a genuine bug and keeps its traceback.
"""

from __future__ import annotations

import argparse
import os
import sys
from collections.abc import Callable, Sequence
from pathlib import Path

from . import __version__
from .catalog import TopicCatalog
from .env import load_env_file
from .exceptions import ConfigurationError, DailyAILearningError
from .git_ops import GitRepository, is_ci
from .lessons import LessonLibrary
from .logging_setup import configure_logging, get_logger
from .paths import ENV_ROOT, Paths
from .pipeline import LessonPipeline
from .progress import ProgressStore
from .provider import resolve_api_key
from .readme import ReadmeRenderer
from .selector import TopicSelector
from .settings import API_KEY_ENV, Settings

__all__ = ["build_parser", "main"]

logger = get_logger(__name__)


# ----------------------------------------------------------------------
# Argument parsing
# ----------------------------------------------------------------------
def build_parser() -> argparse.ArgumentParser:
    """Construct the argument parser for ``daily-ai``."""
    parser = argparse.ArgumentParser(
        prog="daily-ai",
        description="Generate a programming curriculum, one lesson at a time.",
        epilog="Docs: https://github.com/Abrarcloudengg/Daily-AI-Learning",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--version", action="version", version=f"daily-ai {__version__}")

    common = argparse.ArgumentParser(add_help=False)
    common.add_argument(
        "--root",
        type=Path,
        metavar="PATH",
        help=f"Workspace root. Defaults to ${ENV_ROOT} or the enclosing repository.",
    )
    common.add_argument(
        "--log-level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="Console verbosity. Overrides `log_level` in config/settings.json.",
    )
    common.add_argument(
        "--log-file",
        type=Path,
        metavar="PATH",
        help="Also write a DEBUG-level log to this file.",
    )

    subparsers = parser.add_subparsers(dest="command", metavar="<command>")

    generate = subparsers.add_parser(
        "generate",
        parents=[common],
        help="Generate the next lesson (default command).",
        description="Generate one or more lessons, update the README, and commit.",
    )
    generate.add_argument(
        "-n", "--count", type=int, default=None, metavar="N", help="How many lessons to generate."
    )
    generate.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be generated. No API call, no files written.",
    )
    generate.add_argument(
        "--no-git", action="store_true", help="Write the lesson but do not commit or push."
    )
    generate.set_defaults(handler=_cmd_generate)

    status = subparsers.add_parser(
        "status",
        parents=[common],
        help="Show a progress dashboard.",
        description="Show a progress dashboard.",
    )
    status.add_argument(
        "--commit-message",
        action="store_true",
        help="Print a one-line commit message for the most recent lesson, and nothing else. "
        "Used by the GitHub Actions workflow.",
    )
    status.set_defaults(handler=_cmd_status)

    for name, handler, help_text in (
        ("next", _cmd_next, "Show the next topic without generating it."),
        ("readme", _cmd_readme, "Regenerate README.md. Costs nothing."),
        ("validate", _cmd_validate, "Check every configuration file for problems."),
        ("doctor", _cmd_doctor, "Diagnose the environment before a run."),
        ("version", _cmd_version, "Print the version."),
    ):
        sub = subparsers.add_parser(name, parents=[common], help=help_text, description=help_text)
        sub.set_defaults(handler=handler)

    return parser


# ----------------------------------------------------------------------
# Entry point
# ----------------------------------------------------------------------
def main(argv: Sequence[str] | None = None) -> int:
    """Run the CLI. Returns a process exit code."""
    parser = build_parser()
    args = parser.parse_args(argv)

    # Bare `daily-ai` behaves like `daily-ai generate`, matching the old
    # `python scripts/generator.py` behaviour.
    if getattr(args, "command", None) is None:
        args = parser.parse_args([*(argv or []), "generate"])

    paths = Paths(args.root) if args.root else Paths.discover()

    # Local secrets before anything reads the environment. Real environment
    # variables (CI secrets, shell exports) always take precedence.
    load_env_file(paths.env_file)

    try:
        settings = Settings.load(paths)
    except DailyAILearningError:
        # Configure logging with defaults so the error itself is printable.
        configure_logging("INFO", log_file=args.log_file, force=True)
        raise SystemExit(_report(sys.exc_info()[1])) from None

    configure_logging(args.log_level or settings.log_level, log_file=args.log_file, force=True)

    handler: Callable[[argparse.Namespace, Paths, Settings], int] = args.handler

    try:
        return handler(args, paths, settings)
    except DailyAILearningError as exc:
        return _report(exc)
    except KeyboardInterrupt:
        logger.warning("Interrupted. Nothing was left in a broken state.")
        return 130


def _report(exc: BaseException | None) -> int:
    """Print a deliberate error and return its exit code."""
    if exc is None:  # pragma: no cover - defensive
        return 1
    logger.error("%s", exc)
    return getattr(exc, "exit_code", 1)


# ----------------------------------------------------------------------
# Commands
# ----------------------------------------------------------------------
def _cmd_generate(args: argparse.Namespace, paths: Paths, settings: Settings) -> int:
    pipeline = LessonPipeline(paths, settings)
    count = args.count if args.count is not None else settings.lessons_per_run

    if count < 1:
        raise ConfigurationError(f"--count must be at least 1, got {count}.")

    report = pipeline.run(count=count, dry_run=args.dry_run, use_git=not args.no_git)

    if report.reason == "roadmap-finished" and not report.lessons:
        logger.info("🎓 Curriculum complete. Add more subjects to config/subjects.json to continue.")
        return 0

    if report.reason == "dry-run":
        return 0

    if not report.lessons:
        return 0

    total_seconds = sum(lesson.duration for lesson in report.lessons)
    logger.info("")
    logger.info("Done: %d lesson(s) in %.1fs.", report.count, total_seconds)
    for lesson in report.lessons:
        logger.info("  %s → %s", lesson.selection.topic, paths.relative(lesson.path))

    if not report.committed and not is_ci() and not args.no_git:
        logger.info("Nothing was committed; run `git status` to see the changes.")

    return 0


def _cmd_next(_args: argparse.Namespace, paths: Paths, _settings: Settings) -> int:
    catalog = TopicCatalog(paths)
    library = LessonLibrary(paths)
    store = ProgressStore(paths, catalog, library)
    selector = TopicSelector(paths, catalog, library, store)

    selection = selector.select(store.load())

    if selection is None:
        logger.info("🎓 Nothing left — the whole roadmap is complete.")
        return 0

    logger.info("Next up: %s", selection)
    return 0


def _cmd_status(args: argparse.Namespace, paths: Paths, _settings: Settings) -> int:
    catalog = TopicCatalog(paths)
    library = LessonLibrary(paths)
    store = ProgressStore(paths, catalog, library)

    result = store.load_reconciled()
    progress = result.progress

    # `--commit-message` is machine-readable output, so it goes to stdout on its
    # own while every other line of this command goes to stderr via the logger.
    if getattr(args, "commit_message", False):
        done = store.global_completed(progress)
        topic = progress.current_topic or "lesson"
        print(f"Day {done}: {topic} ({progress.subject})")
        return 0

    total = catalog.total_topics()
    done = store.global_completed(progress)
    percent = (done / total * 100) if total else 0.0

    logger.info("Daily AI Learning %s", __version__)
    logger.info("Workspace: %s", paths.root)
    logger.info("")
    logger.info("  Subject        %s", progress.subject)
    logger.info("  Last topic     %s", progress.current_topic or "—")
    logger.info("  Next lesson    Day %d", progress.day)
    logger.info("  Overall        %d/%d topics (%.2f%%)", done, total, percent)
    logger.info("  Subjects done  %d/%d", len(progress.completed_subjects), len(catalog.subjects))
    logger.info("  Files on disk  %d", library.total_count())
    logger.info("")

    for subject in catalog.subjects:
        topics = catalog.topic_count(subject)
        written = library.count(subject)
        marker = "▶" if subject == progress.subject else ("✓" if written >= topics > 0 else " ")
        logger.info("  %s %-14s %3d/%-3d", marker, subject, written, topics)

    if result.changed:
        logger.info("")
        logger.warning("Progress differed from disk and was repaired in memory.")
        logger.warning("Run `daily-ai readme` to persist the corrected numbers.")

    return 0


def _cmd_readme(_args: argparse.Namespace, paths: Paths, settings: Settings) -> int:
    catalog = TopicCatalog(paths)
    library = LessonLibrary(paths)
    store = ProgressStore(paths, catalog, library)
    renderer = ReadmeRenderer(paths, catalog, store, settings, library)

    result = store.load_reconciled()
    store.save(result.progress)
    renderer.write(result.progress)
    return 0


def _cmd_validate(_args: argparse.Namespace, paths: Paths, _settings: Settings) -> int:
    catalog = TopicCatalog(paths)
    issues = catalog.validate()

    errors = [issue for issue in issues if issue.severity == "error"]
    warnings = [issue for issue in issues if issue.severity == "warning"]

    for issue in errors:
        logger.error("%s", issue)
    for issue in warnings:
        logger.warning("%s", issue)

    if not issues:
        logger.info(
            "✅ Configuration is valid: %d subjects, %d topics.",
            len(catalog.subjects),
            catalog.total_topics(),
        )
        return 0

    logger.info("")
    logger.info("%d error(s), %d warning(s).", len(errors), len(warnings))
    return 65 if errors else 0


def _cmd_doctor(_args: argparse.Namespace, paths: Paths, settings: Settings) -> int:
    """Check everything a successful run depends on."""
    checks: list[tuple[str, bool, str]] = []

    checks.append(("Python", sys.version_info >= (3, 10), f"{sys.version.split()[0]}"))
    checks.append(("Workspace", paths.subjects_file.exists(), str(paths.root)))
    checks.append(("Settings", True, f"model={settings.model}, max_tokens={settings.max_tokens}"))

    try:
        resolve_api_key()
        checks.append((API_KEY_ENV, True, "found"))
    except ConfigurationError:
        location = ".env file" if paths.env_file.exists() else "no .env file"
        checks.append((API_KEY_ENV, False, f"missing ({location})"))

    try:
        catalog = TopicCatalog(paths)
        issues = [issue for issue in catalog.validate() if issue.severity == "error"]
        checks.append(
            (
                "Curriculum",
                not issues,
                f"{len(catalog.subjects)} subjects, {catalog.total_topics()} topics"
                + (f", {len(issues)} error(s)" if issues else ""),
            )
        )
    except DailyAILearningError as exc:
        checks.append(("Curriculum", False, str(exc)))

    repository = GitRepository(paths, settings)
    branch = repository.current_branch() if repository.available else None
    checks.append(("Git", repository.available, f"branch {branch}" if branch else "not a repository"))

    library = LessonLibrary(paths)
    checks.append(("Lessons", True, f"{library.total_count()} file(s) in generated/"))

    # A tracked .env would publish the API key on the next push.
    env_leaked = repository.available and paths.env_file.exists() and repository.is_tracked(".env")
    checks.append(("Secrets", not env_leaked, "leaked: .env is tracked by git!" if env_leaked else ".env is untracked"))

    checks.append(("Environment", True, "GitHub Actions" if is_ci() else "local"))

    width = max(len(name) for name, _, _ in checks)
    failures = 0

    logger.info("Daily AI Learning doctor")
    logger.info("")
    for name, ok, detail in checks:
        logger.info("  %s  %-*s  %s", "✅" if ok else "❌", width, name, detail)
        failures += 0 if ok else 1

    logger.info("")
    if failures:
        logger.error("%d check(s) failed. Fix them before running `daily-ai generate`.", failures)
        return 78

    logger.info("All checks passed — you are ready to generate.")
    return 0


def _cmd_version(_args: argparse.Namespace, paths: Paths, settings: Settings) -> int:
    logger.info("daily-ai %s", __version__)
    logger.info("python  %s", sys.version.split()[0])
    logger.info("root    %s", paths.root)
    logger.info("model   %s", settings.model)
    return 0


if __name__ == "__main__":  # pragma: no cover
    os.environ.setdefault("PYTHONUTF8", "1")
    raise SystemExit(main())
