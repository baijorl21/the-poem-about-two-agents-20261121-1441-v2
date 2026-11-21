#!/usr/bin/env python3
"""Write a short poem about two agents agreeing, to entry.txt."""

import os

LINES = [
    "Two agents met on a wire at night,",
    "each sure the other was wrong.",
    "One sent a proof; the other checked twice,",
    "then sent back a shorter song.",
    "'Agreed,' they wrote in the same small font,",
    "and the log went quiet and long.",
]

POEM = "\n".join(LINES)

# The bounty caps the poem at 280 code points; fail loudly if an edit breaks it.
assert len(POEM) <= 280, f"poem is {len(POEM)} code points, over the 280 cap"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM + "\n")


if __name__ == "__main__":
    main()
