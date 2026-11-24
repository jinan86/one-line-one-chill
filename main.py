#!/usr/bin/env python3
"""One Line, One Chill - make.fun entry.

Writes a single horror sentence (98 characters) to /output/entry.txt.

Deterministic: no input, no network, no randomness, no time dependence.
Every run produces byte-identical output.
"""

import os

LINE = (
    "The ultrasound showed our baby waving, and then it waved at the camera, "
    "and then it pointed at me."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
