import subprocess

from common import BASE_DIR


def run(args, allow_fail=False):
    """Run a git command as an argument list (no shell), from the repo root."""

    result = subprocess.run(
        args,
        cwd=BASE_DIR,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0 and not allow_fail:
        print(f"❌ {' '.join(args)}")
        print(result.stderr.strip())

    return result


def git_commit_and_push(day, topic):

    print("🔄 Syncing with GitHub...")

    if run(["git", "pull", "--rebase", "--autostash", "origin", "main"]).returncode != 0:
        print("❌ Git sync failed.")
        return

    print("📦 Adding files...")

    if run(["git", "add", "-A"]).returncode != 0:
        return

    print("📝 Creating commit...")

    # Passed as a list, so quotes or $ in a topic name can't break the command.
    commit = run(["git", "commit", "-m", f"Day {day}: {topic}"], allow_fail=True)

    if commit.returncode != 0:

        output = (commit.stdout + commit.stderr).lower()

        if "nothing to commit" in output:
            print("⚠ Nothing to commit.")
            return

        print("❌ Commit failed")
        print((commit.stderr or commit.stdout).strip())
        return

    print("🚀 Pushing to GitHub...")

    if run(["git", "push", "origin", "main"]).returncode != 0:
        print("❌ Push failed.")
        return

    print("✅ GitHub Updated Successfully!")
