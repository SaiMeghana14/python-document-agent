"""Run with: uv run python exercises/import_example.py"""

from pathlib import Path


def count_words(text: str) -> int:
    return len(text.split())

if __name__ == "__main__":
    sample = Path("samples/input/company_policy.txt").read_text(encoding="utf-8")
    print("Word count:", count_words(sample))
