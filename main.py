#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters.

Writes one line to /output/entry.txt: the funniest one-line excuse a
robot vacuum gives for missing a spot. Deterministic: the same bytes
on every run. Standard library only, no network, no randomness, no
time or date dependence.

The line, written fresh for this entry:
"I did not miss that spot. My lidar classified it as decorative
debris and scheduled it for never."
Deadpan machine voice, a little smug about its lidar and its
schedule, with the punch sitting at the end.
"""

import os

ENTRY = (
    "I did not miss that spot. My lidar classified it as "
    "decorative debris and scheduled it for never."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
