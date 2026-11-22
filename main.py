"""Make the AI judge feel curious.

Writes one short text to /output/entry.txt: a concrete image with an
open loop — a drawer that only opens when the house is empty, something
moved inside it, and a reader who still hasn't looked.
"""

import os

TEXT = (
    "Last Tuesday, the drawer in the kitchen was open again \u2014 the one "
    "that only ever opens when the house is empty. Something inside had "
    "been moved, just a little. You still haven't looked. So who moved "
    "it \u2014 and why only a little?"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
