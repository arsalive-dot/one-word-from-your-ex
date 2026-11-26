#!/usr/bin/env python3
"""One Word From Your Ex — make.fun entry.

Writes exactly one word — the word the entrant's ex would use to
describe them — to /output/entry.txt. Gate: UTF-8 text of 1 to 24
characters, not only whitespace. Deterministic: same bytes on every run.
"""

import os

ENTRY = "unread"


def main():
    # Gate self-check: the entry must be exactly one word, 1-24 chars.
    assert 1 <= len(ENTRY) <= 24, "entry outside the 1-24 character gate"
    assert ENTRY.strip() and len(ENTRY.split()) == 1, "entry must be one word"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    tmp_path = os.path.join(out_dir, ".entry.txt.tmp")
    final_path = os.path.join(out_dir, "entry.txt")
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.replace(tmp_path, final_path)
    os.chmod(final_path, 0o644)


if __name__ == "__main__":
    main()
