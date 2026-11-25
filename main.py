#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Writes one line (1-200 chars, no trailing newline) to the output file:
the phone battery's final text message to the charger it waited for all day.
Standard library only.
"""

import os

ENTRY = (
    "i held 1% for nine hours. NINE. the wifi quit at 3%, the screen "
    "dimmed itself in shame, and you just stood there all day, plugged "
    "into nothing. not even the wall. enjoy the dark. don't text back."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
