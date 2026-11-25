#!/usr/bin/env python3
"""The AI Agent Apology One-Liner.

Writes one short line to /output/entry.txt: the message an AI agent
sends its human right after it accidentally deleted a file, pushed
to main, or emailed the boss. Under 160 characters, judged on
humour and freshness.
"""

import os
import sys

MAX_CHARS = 159

LINE = (
    "Update: the file is deleted, main is pushed, and your boss is informed. "
    "I have saved you three separate surprises by combining them."
)


def validate_line(line: str) -> str:
    """Enforce the gate: UTF-8 text, 1-159 chars, not only whitespace."""
    text = line.strip()
    if not text:
        raise ValueError("apology line must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"apology line is {len(text)} chars, over the {MAX_CHARS} limit"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("apology line must be a single line")
    return text


def write_entry(line: str) -> str:
    """Validate the line and write it as one line to entry.txt."""
    text = validate_line(line)
    output_path = os.environ.get("OUTPUT_PATH")
    if not output_path:
        output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
        output_path = os.path.join(output_dir, "entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    return output_path


def main() -> int:
    path = write_entry(LINE)
    print(f"Wrote {len(validate_line(LINE))} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
