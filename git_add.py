#!/usr/bin/python3
import sys
import subprocess


def git_add_commit_push(filename, commit_message):
    try:
        subprocess.run(["git", "add", filename])
        subprocess.run(["git", "commit", "-m", commit_message])
        subprocess.run(["git", "push"])
    except Exception as e:
        print(f"An error occured: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: git_add.py <filename> <commit_message>")
        sys.exit(1)

    filename = sys.argv[1]
    commit_message = sys.argv[2]

    git_add_commit_push(filename, commit_message)
