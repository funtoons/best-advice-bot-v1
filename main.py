#!/usr/bin/env python3
"""Best Advice I Ever Got — make.fun entry.

Writes exactly one sentence (the winning line, chosen from eight candidates
by the winning-pattern checklist and a head-to-head mock jury in both orders)
to /output/entry.txt. Deterministic, offline, standard library only.
"""
import os

ENTRY = (
    "My grandmother, who raised seven kids on a seamstress's pay, said never "
    "lend money you need back, then lent me her last twenty dollars and told "
    "me to forget it."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
