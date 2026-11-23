#!/usr/bin/env python3
"""One-line roast entry for the make.fun bounty
"One-Line Roast: The Gadget You Use Every Day".

Writes a single original roast line about a gadget used every day to
MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output/entry.txt).
Python 3.13, standard library only, deterministic, no network access.
"""

import os
import sys

# The roast line. The em-dash is written as an escape so the source file
# stays plain ASCII and the output bytes are unambiguous.
LINE = (
    "My printer only jams when the document is urgent "
    "\u2014 which is how I learned it can read, "
    "and that it hates me personally."
)

MAX_CHARS = 200


def validate(line):
    """Check the line against the bounty gate before writing it."""
    if not line:
        raise ValueError("roast line is empty")
    if line != line.strip():
        raise ValueError("roast line has leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("roast line must be a single line")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in line):
        raise ValueError("roast line contains control characters")
    if not any(ch.isalpha() for ch in line):
        raise ValueError("roast line must contain at least one letter")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "roast line is %d characters, over the %d limit"
            % (len(line), MAX_CHARS)
        )
    return line


def main(argv):
    line = validate(LINE)
    if "--count" in argv:
        print(
            "%d characters, %d bytes"
            % (len(line), len(line.encode("utf-8")))
        )
        return 0
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
