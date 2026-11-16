from pathlib import Path


def show_file_size(path: Path) -> int:
    return path.stat().st_size

if __name__ == "__main__":
    sample = Path("samples/input/company_policy.txt")
    print(f"{sample.name}: {show_file_size(sample)} bytes")
