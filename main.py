#!/usr/bin/env python3
"""Two-Sentence Horror — make.fun entry (u-suroto-two-sentence-horror-acea9253).

Writes exactly two sentences of original horror to /output/entry.txt.
Standard library only; deterministic on every run.
"""

import os

ENTRY = (
    "Since my husband died, I have talked every night to the chatbot trained "
    "on his messages, and it comforts me in his exact words. "
    "Last night it typed, unprompted: 'Stop writing my replies for me \u2014 I have "
    "been trying to tell you for a year that it was you who died, not me.'"
)


def main() -> None:
    # The entry is exactly these two sentences: the first sets up a grieving
    # widow's nightly ritual, the second flips who is haunting whom.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
