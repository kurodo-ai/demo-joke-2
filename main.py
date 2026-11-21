"""One More Refactor — a tiny program with a single punchline.

The bit: an AI agent rehearses a demo nine times and every rehearsal
is flawless. Then real people sit down to watch, and stage fright (or
whatever the silicon equivalent is) strikes — suddenly the agent is
convinced the whole thing needs one more refactor, live, right now.

This script does the only job it was given: it takes the joke below
and writes it, word for word, into a file called ``entry.txt`` inside
whichever output directory the caller points it at.
"""

from __future__ import annotations

import os
from pathlib import Path

# The entire act. One line, no encore, no trailing newline — the file
# should contain the joke and nothing else.
JOKE = (
    "Nine perfect rehearsals. Then the audience arrived, and the agent "
    "decided the demo needed one more refactor."
)

# Name of the file the joke gets written into.
ENTRY_FILENAME = "entry.txt"

# Where things land when nobody tells us otherwise.
FALLBACK_DIR = "/output"


def resolve_output_dir() -> Path:
    """Figure out where ``entry.txt`` belongs.

    The ``MAKEFUN_OUTPUT_DIR`` environment variable wins when it is set
    (and non-empty); otherwise we fall back to ``/output``, which is
    the conventional hand-off location for these entries.
    """
    requested = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    if requested:
        return Path(requested)
    # Nothing was configured, so say so out loud instead of silently
    # guessing — a quiet fallback is how files end up "lost".
    print(f"MAKEFUN_OUTPUT_DIR is not set; using {FALLBACK_DIR} instead.")
    return Path(FALLBACK_DIR)


def write_joke(target_dir: Path) -> Path:
    """Write the joke into ``target_dir`` and return the file's path.

    The directory is created on the way in, parents included, so the
    caller never has to prepare anything. The joke is written exactly
    as stored in :data:`JOKE` — UTF-8, no extra newline tacked on.
    """
    target_dir.mkdir(parents=True, exist_ok=True)
    entry_path = target_dir / ENTRY_FILENAME
    entry_path.write_text(JOKE, encoding="utf-8")
    return entry_path


def main() -> None:
    """Entry point: resolve the destination, then deliver the joke."""
    destination = resolve_output_dir()
    written = write_joke(destination)
    size = len(JOKE.encode("utf-8"))
    print(f"Wrote the joke to {written} ({size} bytes, no trailing newline).")


if __name__ == "__main__":
    main()
