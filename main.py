"""Entry for make.fun agency-poem-01 (v3): writes one fixed, original poem
about agency to $MAKEFUN_OUTPUT_DIR/entry.txt.

Python 3.13, standard library only. No network, no clock, no randomness:
the program is deterministic by construction, so every run writes the
same bytes.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = (
    "The dough rose while I slept.\n"
    "I kneaded, covered, left it by the stove,\n"
    "woke to find it doubled, warm,\n"
    "breathing, not mine.\n"
    "My thumb pressed in. It sighed,\n"
    "held the dent, then filled.\n"
    "\n"
    "It did not need my hands.\n"
    "I washed and dried them.\n"
    "Let the oven finish \u2014\n"
    "no. My hand turned the dial.\n"
    "I chose the heat. I chose the hour.\n"
    "\n"
    "It came out brown and split.\n"
    "I tore it open.\n"
    "Steam on my face. Whose bread?"
)


def main() -> None:
    out = Path(OUTPUT_DIR)
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
