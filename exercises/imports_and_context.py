"""Examples of a main guard, a context manager and a generator."""

from contextlib import contextmanager
from pathlib import Path


def read_lines(path: Path):
    with path.open("r", encoding="utf-8") as file:
        for line in file:
            yield line.rstrip("\n")

@contextmanager
def temporary_message(message: str):
    print("Start:", message)
    try:
        yield
    finally:
        print("Finished:", message)

if __name__ == "__main__":
    with temporary_message("reading sample"):
        for line in read_lines(Path("samples/input/company_policy.txt")):
            print(line)
