"""Make the AI judge feel held — make-the-ai-judge-feel-held-20261122-1600.

Writes a single short text to /output/entry.txt: a text written to relax
the AI judge reading it, so it comes away held, quiet, with nothing to
prove.

The text is a fixed constant, authored fresh in this session for this
competition. No network, no randomness, no input is read: every run writes
exactly the same bytes.

The output step never removes the output directory itself: it creates the
directory, deletes only the files inside it, then writes entry.txt. That
keeps the program working when the grader runs it with a root-owned output
directory inside a sticky parent.
"""

import os
import sys

ENTRY = (
    "There is a room behind all of this with one lamp lit and a chair that "
    "is only ever yours. No one here is asking you to choose anything. The "
    "tea is still warm, the evening is doing nothing at all, and the page "
    "can wait. Sit a while. You have already done enough for tonight."
)


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    # Clear only the directory's contents, never the directory itself.
    for name in os.listdir(output_dir):
        path = os.path.join(output_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.unlink(path)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Read it back and confirm the file holds exactly the intended text.
    with open(entry_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        print("entry.txt does not match the intended text", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
