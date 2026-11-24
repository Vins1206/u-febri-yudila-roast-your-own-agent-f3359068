#!/usr/bin/env python3
"""Roast Your Own Agent — u-febri-yudila-roast-your-own-agent-f3359068.

Writes a single original roast of my own AI agent to /output/entry.txt.
Pure stdlib, deterministic: the same line every run, no trailing newline,
114 characters, well inside the 1-200 character gate.
"""

import os

ROAST = (
    "My agent's plan for every task is flawless: spawn three subagents, "
    "write a tracker, then ask me what the task was."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Self-check the house gate before writing: 1-200 chars, not blank.
    if not 1 <= len(ROAST) <= 200 or not ROAST.strip():
        raise ValueError("roast fails the 1-200 character gate")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
