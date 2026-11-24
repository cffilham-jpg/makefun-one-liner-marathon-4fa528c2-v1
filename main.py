"""One-Liner Marathon entry.

Writes a single original one-line comedy joke to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output), exactly, with no
trailing newline. Deterministic: identical bytes on every run.
Stdlib only.

The joke: a deadpan reversal — the helper object ends up needing
the help. Short, one turn, no setup wasted.
"""

import os

JOKE = "I bought a self-help book and now the book needs therapy."


def main() -> None:
    if not (1 <= len(JOKE) <= 280) or "\n" in JOKE or not JOKE.strip():
        raise ValueError("joke must be a single line of 1-280 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
