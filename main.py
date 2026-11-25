#!/usr/bin/env python3
"""Funniest Honest Appliance Error — make.fun entry.

Writes one line (at most 200 characters) to /output/entry.txt:
the funniest honest error message a microwave could show.

The fault is real: a microwave heats unevenly and the plate soaks up
the energy, so the plate comes out too hot to touch while the food
stays cold. The laugh is the machine's deadpan excuse for it.
"""

import os
import sys

LINE = "ERROR: The plate is hot. The food is cold. I heated what I could reach."

MAX_CHARS = 200


def main() -> int:
    line = LINE
    if not line or not line.strip():
        print("entry is blank", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(f"entry is {len(line)} chars, over {MAX_CHARS}", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in line):
        print("entry contains a control character", file=sys.stderr)
        return 1
    # The entry line is 71 characters: one line, well inside the 200 cap.
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(line + "\n")
    print(f"wrote {len(line)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
