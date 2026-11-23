#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line (119 characters) to entry.txt in
the output directory the harness provides. The line is fixed: the
same text on every run. Standard library only, no network access,
no randomness, no input files.
"""

import os
import sys

ROAST = (
    "My printer only jams when the document is urgent"
    " \u2014 which is how I learned it can read,"
    " and that it hates me personally."
)

CHAR_LIMIT = 200


def _check(line):
    """Refuse anything the gate would refuse: outside 1-200 chars,
    blank, multi-line, or carrying control characters."""
    n = len(line)
    if n < 1 or n > CHAR_LIMIT:
        raise SystemExit(f"roast is {n} characters, gate needs 1-{CHAR_LIMIT}")
    if not line.strip():
        raise SystemExit("roast must not be only whitespace")
    if line.strip() != line:
        raise SystemExit("roast must not start or end with whitespace")
    for ch in line:
        if ch in "\n\r" or ord(ch) < 32:
            raise SystemExit("roast must be one line with no control characters")


def _out_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def run():
    _check(ROAST)
    os.makedirs(_out_dir(), exist_ok=True)
    target = os.path.join(_out_dir(), "entry.txt")
    with open(target, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ROAST + "\n")
    return ROAST


if __name__ == "__main__":
    text = run()
    if "--count" in sys.argv[1:]:
        print(f"{len(text)} characters, {len(text.encode('utf-8'))} bytes")
