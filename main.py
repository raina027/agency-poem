"""Entry for make.fun agency-poem-01: writes one fixed, original poem
about agency to $MAKEFUN_OUTPUT_DIR/entry.txt.

Python 3.13, standard library only. No network, no clock, no randomness:
the program is deterministic by construction, so every run writes the
same bytes.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = (
    "The morning she chose the blue cup\n"
    "over the white one, nothing happened.\n"
    "\n"
    "No thunder. No door swung open.\n"
    "The tea was the same tea.\n"
    "\n"
    "But her hand, reaching, had paused \u2014\n"
    "not asked, not waited, not weighed\n"
    "what anyone else would think of blue.\n"
    "\n"
    "That was the whole of it.\n"
    "The rest of the day went on as before:\n"
    "the bus, the queue, the boss, the rent.\n"
    "\n"
    "Only now she counted the times\n"
    "her hand hovered, asking permission\n"
    "from people who were not even in the room.\n"
    "\n"
    "So she chose the long way home,\n"
    "the song no one else liked,\n"
    "the word no when yes was expected.\n"
    "\n"
    "Small things. Her things.\n"
    "The power to act had never left her \u2014\n"
    "it had only been waiting, quietly,\n"
    "for her to pick it up, like a cup,\n"
    "and drink."
)


def main() -> None:
    out = Path(OUTPUT_DIR)
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
