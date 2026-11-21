#!/usr/bin/env python3
"""Writes one short poem about two agents agreeing to entry.txt.

Two agents begin apart -- one wants to wait, one wants to move --
and trade half-ideas until the halves join into a single plan
that both can speak in one voice.
"""

import os
import sys

LINES = [
    "You said wait. I said go.",
    "We traded halves of one idea",
    "until the halves met and held.",
    "No winner. No loser.",
    "Just two voices, one sentence:",
    "'We will.' Then we moved as one.",
]

MAX_CODE_POINTS = 280


def compose() -> str:
    return "\n".join(LINES) + "\n"


def check(text: str) -> None:
    n = len(text)
    if not (1 <= n <= MAX_CODE_POINTS):
        sys.exit(f"poem is {n} code points, gate wants 1..{MAX_CODE_POINTS}")
    if not text.strip():
        sys.exit("poem is only white space")
    text.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    poem = compose()
    check(poem)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(poem)


if __name__ == "__main__":
    main()
