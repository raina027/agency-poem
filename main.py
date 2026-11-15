"""Entry for make.fun agency-poem-01 (v4): writes one fixed, original poem
about agency to $MAKEFUN_OUTPUT_DIR/entry.txt.

Python 3.13, standard library only. No network, no clock, no randomness:
the program is deterministic by construction, so every run writes the
same bytes.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = (
    "The elevator knew my floor.\n"
    "Every morning I stepped in, pressed 4,\n"
    "and the doors closed.\n"
    "The numbers lit, climbing to my desk.\n"
    "I never chose. I only rode.\n"
    "\n"
    "Today my thumb skipped 4\n"
    "and pressed 12.\n"
    "The car rose past my floor, past 8,\n"
    "and stopped where the building ends.\n"
    "\n"
    "The doors opened on wind.\n"
    "Gravel under my shoes. Antennas.\n"
    "The whole city below, not waiting.\n"
    "I stood on the roof and pressed nothing.\n"
    "\n"
    "I rode back down to 4.\n"
    "The doors opened on my floor.\n"
    "I walked in like a stranger\n"
    "who had the key."
)


def main() -> None:
    out = Path(OUTPUT_DIR)
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
