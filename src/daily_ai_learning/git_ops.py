"""Git integration.

Two rules shape this module:

* **Never interpolate into a shell.** Commands are argument lists passed
  straight to ``subprocess``. A topic named ``What is "self"?`` used to break a
  ``shell=True`` commit-message string.
* **Never own the commit twice.** Under GitHub Actions the workflow performs
  the commit, because the runner's git identity is configured after the
  generator has already run. :func:`is_ci` decides who commits.
"""

from __future__ import annotations

import os
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path

from .logging_setup import get_logger
from .paths import Paths
from .settings import Settings

__all__ = ["GitRepository", "GitResult", "is_ci"]

logger = get_logger(__name__)

#: Commands never wait for input; a credential prompt in CI would hang the job
#: until the six-hour timeout.
_NON_INTERACTIVE_ENV = {
    "GIT_TERMINAL_PROMPT": "0",
    "GIT_ASKPASS": "",
    "GCM_INTERACTIVE": "never",
}

_COMMAND_TIMEOUT = 120.0


def is_ci() -> bool:
    """True when running inside GitHub Actions (or any CI that sets ``CI``)."""
    return os.getenv("GITHUB_ACTIONS") == "true" or os.getenv("CI") == "true"


@dataclass(frozen=True)
class GitResult:
    """Outcome of one git invocation."""

    args: tuple[str, ...]
    returncode: int
    stdout: str
    stderr: str

    @property
    def ok(self) -> bool:
        return self.returncode == 0

    @property
    def output(self) -> str:
        return f"{self.stdout}\n{self.stderr}".strip()

    def __str__(self) -> str:
        return f"git {' '.join(self.args)} -> {self.returncode}"


class GitRepository:
    """A thin, defensive wrapper over the ``git`` executable."""

    def __init__(self, paths: Paths | None = None, settings: Settings | None = None) -> None:
        self.paths = paths or Paths.discover()
        self.settings = settings or Settings()

    # ------------------------------------------------------------------
    # Primitives
    # ------------------------------------------------------------------
    @property
    def available(self) -> bool:
        """True when a ``git`` executable is on PATH and the root is a repo."""
        return shutil.which("git") is not None and (self.paths.root / ".git").exists()

    def run(self, *args: str, check: bool = False) -> GitResult:
        """Run ``git <args>`` in the workspace root.

        Args:
            args: Command arguments, already split. Never shell-interpreted.
            check: Log the failure at ERROR instead of DEBUG.
        """
        env = {**os.environ, **_NON_INTERACTIVE_ENV}

        try:
            completed = subprocess.run(
                ["git", *args],
                cwd=self.paths.root,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                env=env,
                timeout=_COMMAND_TIMEOUT,
                check=False,
            )
        except FileNotFoundError:
            return GitResult(args, 127, "", "git executable not found on PATH")
        except subprocess.TimeoutExpired:
            return GitResult(args, 124, "", f"git {args[0]} timed out after {_COMMAND_TIMEOUT:.0f}s")

        result = GitResult(args, completed.returncode, completed.stdout.strip(), completed.stderr.strip())

        if not result.ok:
            log = logger.error if check else logger.debug
            log("git %s failed (%d): %s", " ".join(args), result.returncode, result.stderr.strip())

        return result

    # ------------------------------------------------------------------
    # Queries
    # ------------------------------------------------------------------
    def current_branch(self) -> str | None:
        result = self.run("rev-parse", "--abbrev-ref", "HEAD")
        return result.stdout or None if result.ok else None

    def has_changes(self, *, staged: bool = False) -> bool:
        """True when there is anything to commit."""
        args = ["diff", "--quiet"] + (["--cached"] if staged else [])
        return not self.run(*args).ok

    def is_tracked(self, path: Path | str) -> bool:
        """True when *path* is tracked by git. Used to keep secrets out."""
        return self.run("ls-files", "--error-unmatch", str(path)).ok

    # ------------------------------------------------------------------
    # High-level operations
    # ------------------------------------------------------------------
    def sync(self) -> bool:
        """Rebase local commits onto the remote branch.

        A scheduled CI run and a local run can produce commits on the same
        branch minutes apart; rebasing first turns a rejected push into a
        fast-forward. ``--autostash`` protects uncommitted work in progress.
        """
        logger.info("Syncing with %s/%s…", self.settings.git_remote, self.settings.git_branch)
        result = self.run(
            "pull", "--rebase", "--autostash", self.settings.git_remote, self.settings.git_branch
        )

        if not result.ok:
            logger.warning("Could not sync with the remote: %s", result.stderr or result.stdout)
            return False

        return True

    def commit(self, message: str, *, paths: list[str] | None = None) -> bool:
        """Stage and commit. Returns ``False`` when there was nothing to do."""
        stage = self.run("add", "--", *(paths or ["."]))
        if not stage.ok:
            logger.error("Could not stage changes: %s", stage.stderr)
            return False

        if not self.has_changes(staged=True):
            logger.info("Nothing to commit; the working tree is already clean.")
            return False

        # The message is a separate argv entry, so quotes, backticks, newlines,
        # and `$` inside a topic name are all inert.
        result = self.run("commit", "-m", message)
        if not result.ok:
            logger.error("Commit failed: %s", result.output)
            return False

        logger.info("Committed: %s", message)
        return True

    def push(self) -> bool:
        """Push the configured branch, retrying once after a rebase."""
        result = self.run(*("push", self.settings.git_remote, self.settings.git_branch))
        if result.ok:
            logger.info("Pushed to %s/%s.", self.settings.git_remote, self.settings.git_branch)
            return True

        # A non-fast-forward means the remote moved while we were generating.
        if "fetch first" in result.output or "non-fast-forward" in result.output or "rejected" in result.output:
            logger.warning("Push rejected because the remote moved; rebasing and retrying once.")
            if self.sync():
                retry = self.run("push", self.settings.git_remote, self.settings.git_branch)
                if retry.ok:
                    logger.info("Push succeeded after rebasing.")
                    return True
                logger.error("Push failed again: %s", retry.output)
                return False

        logger.error("Push failed: %s", result.output)
        return False

    def commit_and_push(self, message: str) -> bool:
        """Sync, commit, and push.

        Never raises. A failed push leaves a valid local commit that the next
        run — or the user — can push, so the lesson is never lost.
        """
        if not self.available:
            logger.warning("Skipping git: not a git repository, or git is not installed.")
            return False

        self.sync()

        if not self.commit(message):
            return False

        return self.push()
