"""One-Sentence Absurd Invention Pitch.

Writes a single sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
"""

import os

ENTRY = (
    "The Blackmail Toothbrush hums your least favourite song on loop "
    "until you stop quitting after thirty seconds and brush for the "
    "full two minutes."
)


def main() -> None:
    # Self-check the gate before writing: 1-220 chars, one sentence.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 220, f"entry is {len(text)} chars, must be 1-220"
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
