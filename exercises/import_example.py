"""Practise importing a function and protecting code with a main guard."""

from pathlib import Path


def count_words(text: str) -> int:
    return len(text.split())


def main() -> None:
    sample_path = Path("samples/input/company_policy.txt")
    sample_text = sample_path.read_text(encoding="utf-8")
    print("Word count:", count_words(sample_text))


if __name__ == "__main__":
    main()
