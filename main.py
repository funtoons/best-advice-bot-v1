"""Best advice entry generator.

Writes the chosen one-sentence entry to /output/entry.txt,
exactly as specified, with no trailing newline.
Deterministic, offline, stdlib-only: no randomness, no network,
no timestamps.
"""

import os

ENTRY = (
    "My grandmother, who raised seven kids on a seamstress's pay, "
    "said never lend money you need back, then lent me her last "
    "twenty dollars and told me to forget it."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if ENTRY.count(".") != 1 or not ENTRY.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
