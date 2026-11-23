"""Roast Your Own Agent — one-line self-roast entry.

Writes the single roast line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt), exactly as-is, no trailing newline.
Standard library only; deterministic.
"""

import os

ROAST = "I asked my agent for one line. It spawned twelve subagents, wrote a run record, and burned a novel's worth of tokens to say 'done.'"


def main():
    # Gate self-check: entry must be 1-200 characters, not only whitespace.
    if not (1 <= len(ROAST) <= 200 and ROAST.strip()):
        raise ValueError("roast line is outside the 1-200 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
