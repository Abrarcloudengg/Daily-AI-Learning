import subprocess


def run(command):

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"❌ {command}")
        print(result.stderr.strip())
        return False

    return True


def git_commit_and_push(day, topic):

    print("🔄 Syncing with GitHub...")

    if not run("git pull --rebase --autostash origin main"):
        print("❌ Git sync failed.")
        return

    print("📦 Adding files...")

    if not run("git add ."):
        return

    print("📝 Creating commit...")

    commit = subprocess.run(
        f'git commit -m "Day {day}: {topic}"',
        shell=True,
        capture_output=True,
        text=True
    )

    if commit.returncode != 0:

        output = (commit.stdout + commit.stderr).lower()

        if "nothing to commit" in output:
            print("⚠ Nothing to commit.")
            return

        print("❌ Commit failed")
        print(commit.stderr.strip())
        return

    print("🚀 Pushing to GitHub...")

    if not run("git push origin main"):
        print("❌ Push failed.")
        return

    print("✅ GitHub Updated Successfully!")