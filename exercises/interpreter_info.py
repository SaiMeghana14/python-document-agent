"""Show which Python interpreter is running this script."""

import sys


def main() -> None:
    print("Python version:", sys.version)
    print("Python executable:", sys.executable)
    print("Virtual environment:", sys.prefix != sys.base_prefix)


if __name__ == "__main__":
    main()
