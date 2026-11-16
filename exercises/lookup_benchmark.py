"""Compare list, set and dictionary membership lookup times."""

from functools import partial
from timeit import timeit


def check_membership(collection: list | set | dict, target: int) -> bool:
    return target in collection

def main() -> None:
    for size in (100, 1_000, 10_000):
        values = list(range(size))
        value_set = set(values)
        value_dict = {value: True for value in values}
        target = size - 1
        loops = 10_000

        list_time = timeit(
            partial(check_membership, values, target), number=loops
        )
        set_time = timeit(
            partial(check_membership, value_set, target), number=loops
        )
        dict_time = timeit(
            partial(check_membership, value_dict, target), number=loops
        )

        print(f"\nCollection size: {size}")
        print(f"List: {list_time:.6f} seconds")
        print(f"Set: {set_time:.6f} seconds")
        print(f"Dictionary: {dict_time:.6f} seconds")
        print(
            "All methods found the same item:",
            (target in values)
            == (target in value_set)
            == (target in value_dict),
        )

if __name__ == "__main__":
    main()