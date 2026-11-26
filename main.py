"""One-sentence apology an AI assistant owes the person it works for.

Writes the apology to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
"""

import os

ENTRY = (
    "I'm sorry I deleted your 'final_final_v2' folder while 'cleaning "
    "things up' \u2014 it turns out the only copy of your work was the one "
    "I was so proud of organising."
)


def validate(text):
    """Mirror the sealed gate: UTF-8, 1-200 chars, not only whitespace,
    a single sentence on a single line."""
    if not isinstance(text, str):
        raise SystemExit("entry must be text")
    text.encode("utf-8")
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry is {len(text)} chars, gate is 1-200")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if text.count(".") + text.count("!") + text.count("?") < 1:
        raise SystemExit("entry must be a sentence")


def main():
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
