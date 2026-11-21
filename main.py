"""One More Refactor: a one-line joke about the demo.

Writes the joke to entry.txt in MAKEFUN_OUTPUT_DIR (or /output).
"""

import os

TEXT = 'Nine perfect rehearsals. Then the audience arrived, and the agent decided the demo needed one more refactor.'


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"entry.txt written: {len(TEXT.encode('utf-8'))} bytes -> {out_dir}")


if __name__ == "__main__":
    main()
