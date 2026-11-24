"""Count words in a UTF-8 text file.

Usage:
    python examples/word_count.py README.md
"""

from pathlib import Path
import sys


def count_words(text: str) -> int:
    """Return the number of whitespace-separated words in text."""
    return len(text.split())


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python examples/word_count.py <text-file>", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"Could not read {path}: {exc}", file=sys.stderr)
        return 1

    print(count_words(text))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
