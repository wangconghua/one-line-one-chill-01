#!/usr/bin/env python3
"""One Line, One Chill — entry program.

Writes a single sentence of horror to /output/entry.txt (or beside this
file when /output does not exist, for local runs).
"""

import os

ENTRY = "I asked the voice in the walls to stop whispering my name, and it did — now it whispers my daughter's."

MAX_CHARS = 200
TERMINATORS = ".!?"


def validate(text):
    """Check the entry against the competition gate and the task rules.

    Returns a list of problems; empty means the text is valid.
    """
    problems = []
    if not isinstance(text, str):
        problems.append("entry is not text")
        return problems
    if not text:
        problems.append("entry is empty")
    if not text.strip():
        problems.append("entry is only whitespace")
    if len(text) > MAX_CHARS:
        problems.append("entry is %d characters, over the 200 limit" % len(text))
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    # One sentence: exactly one sentence-terminating mark, at the end.
    marks = [c for c in text if c in TERMINATORS]
    if len(marks) != 1 or not text.endswith("."):
        problems.append("entry must be exactly one sentence ending in '.'")
    if text != text.strip():
        problems.append("entry has leading or trailing whitespace")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        problems.append("entry is not encodable as UTF-8")
    return problems


def main():
    problems = validate(ENTRY)
    if problems:
        raise SystemExit("invalid entry: " + "; ".join(problems))
    out = "/output/entry.txt" if os.path.isdir("/output") else os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "entry.txt"
    )
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print("wrote %s (%d chars)" % (out, len(ENTRY)))


if __name__ == "__main__":
    main()
