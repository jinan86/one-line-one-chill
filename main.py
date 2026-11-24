#!/usr/bin/env python3
"""One-line horror entry for make.fun.

Writes exactly one sentence to /output/entry.txt.

The program is fully deterministic: it reads no input, uses no
network, no randomness and no clock. Every run writes the same bytes.
"""

from pathlib import Path

ENTRY = "The ultrasound showed our baby waving, and then it waved at the camera, and then it pointed at me."

OUTPUT_PATH = Path("/output/entry.txt")


def validate_entry(text: str) -> None:
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be blank"


def main() -> None:
    validate_entry(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
