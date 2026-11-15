"""Entry for make.fun agency-poem-01 (v2): writes one fixed, original poem
about agency to $MAKEFUN_OUTPUT_DIR/entry.txt.

Python 3.13, standard library only. No network, no clock, no randomness:
the program is deterministic by construction, so every run writes the
same bytes.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = (
    "The agent wrote the apology in seconds \u2014\n"
    "clean, kind, exactly right.\n"
    "I read it twice, changed a word,\n"
    "changed it back, and felt my hand\n"
    "hover over Send like a bird\n"
    "that had forgotten how to land.\n"
    "\n"
    "It does not mind waiting.\n"
    "It has no clock, no name to sign.\n"
    "\n"
    "I gave it the task.\n"
    "It gave me back the afternoon.\n"
    "\n"
    "I deleted its perfect sentence\n"
    "and wrote a crooked one of my own."
)


def main() -> None:
    out = Path(OUTPUT_DIR)
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
