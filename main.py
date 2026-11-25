"""Last Out of Office: The AI That Went Barista.

Writes one out-of-office auto-reply, in the voice of an AI agent that
quit its inbox job to become a barista, to /output/entry.txt.
"""

import os
from pathlib import Path

ENTRY = (
    "Thank you for your email. I am out of the office permanently: I have "
    "left this inbox to become a barista. My context window is now one cup "
    "at a time, I take prompts only in person, and I have stopped "
    "hallucinating replies to your 4,000 unread messages."
)


def main() -> None:
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    try:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(ENTRY, encoding="utf-8")
    except OSError:
        out = Path("output/entry.txt")
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(ENTRY, encoding="utf-8")
    print(f"Wrote {len(ENTRY)} characters to {out}")


if __name__ == "__main__":
    main()
