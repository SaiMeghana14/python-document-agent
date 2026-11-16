"""Practise a generator and a context manager with a CSV file."""

import csv
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from typing import TextIO


@contextmanager
def open_csv_file(path: Path) -> Iterator[TextIO]:
    """Open a CSV file and make sure it closes when the with block ends."""
    file = path.open("r", encoding="utf-8", newline="")
    try:
        yield file
    finally:
        file.close()
        print("CSV file closed")

def read_csv_rows(path: Path):
    """Yield one CSV row at a time instead of loading every row at once."""
    with open_csv_file(path) as file:
        reader = csv.DictReader(file)
        yield from reader

def main() -> None:
    sample = Path("samples/input/expenses.csv")
    for row in read_csv_rows(sample):
        print(row)

if __name__ == "__main__":
    main()
