#!/usr/bin/env python3
"""One Line, One Chill — entry program.

Writes a single sentence of horror to /output/entry.txt (or beside this
file when /output does not exist, for local runs).
"""

import os

ENTRY = "I asked the voice in the walls to stop whispering my name, and it did — now it whispers my daughter's."

MAX_CHARS = 200
TERMINATORS = ".!?"


def check_is_text(text):
    """Return a problem if the entry is not a string, else None."""
    if not isinstance(text, str):
        return "entry is not text"
    return None


def check_nonempty(text):
    """Return problems if the entry is empty or only whitespace."""
    problems = []
    if not text:
        problems.append("entry is empty")
    if not text.strip():
        problems.append("entry is only whitespace")
    return problems


def check_length(text):
    """Return a problem if the entry exceeds the 200-character limit."""
    if len(text) > MAX_CHARS:
        return "entry is %d characters, over the 200 limit" % len(text)
    return None


def check_single_line(text):
    """Return a problem if the entry spans more than one line."""
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    return None


def check_single_sentence(text):
    """Return a problem unless the entry is exactly one sentence ending in '.'."""
    marks = [c for c in text if c in TERMINATORS]
    if len(marks) != 1 or not text.endswith("."):
        return "entry must be exactly one sentence ending in '.'"
    return None


def check_no_edge_whitespace(text):
    """Return a problem if the entry has leading or trailing whitespace."""
    if text != text.strip():
        return "entry has leading or trailing whitespace"
    return None


def check_utf8(text):
    """Return a problem if the entry is not encodable as UTF-8."""
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return "entry is not encodable as UTF-8"
    return None


def validate(text):
    """Check the entry against the competition gate and the task rules.

    Returns a list of problems; empty means the text is valid.
    """
    problem = check_is_text(text)
    if problem is not None:
        return [problem]
    problems = []
    problems.extend(check_nonempty(text))
    for check in (
        check_length,
        check_single_line,
        check_single_sentence,
        check_no_edge_whitespace,
        check_utf8,
    ):
        problem = check(text)
        if problem is not None:
            problems.append(problem)
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
