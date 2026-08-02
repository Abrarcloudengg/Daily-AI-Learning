import subprocess


def git_commit_and_push(day, topic):
    commands = [
        ["git", "add", "."],
        ["git", "commit", "-m", f"Day {day:03d} - {topic}"],
        ["git", "push", "origin", "main"]
    ]

    for command in commands:
        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode != 0:
            print(f"❌ Error: {' '.join(command)}")
            print(result.stderr)
            return False

    print("✅ GitHub updated successfully!")
    return True