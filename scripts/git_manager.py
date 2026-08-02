import subprocess


def run(command):
    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"❌ Error: {command}")
        print(result.stderr)
        return False

    return True


def git_commit_and_push(day, topic):

    print("📥 Syncing with GitHub...")

    run("git pull --rebase origin main")

    print("📦 Adding files...")

    run("git add .")

    print("📝 Creating commit...")

    commit = subprocess.run(
        f'git commit -m "Day {day}: {topic}"',
        shell=True,
        capture_output=True,
        text=True
    )

    if commit.returncode != 0:

        if "nothing to commit" in commit.stderr.lower():
            print("⚠ Nothing to commit.")
            return

        print(commit.stderr)
        return

    print("🚀 Pushing to GitHub...")

    run("git push origin main")

    print("✅ GitHub Updated Successfully!")