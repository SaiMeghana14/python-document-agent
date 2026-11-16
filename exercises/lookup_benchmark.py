"""Compare membership lookup in a list, set and dictionary."""

from timeit import timeit

for size in (100, 1_000, 10_000):
    values = list(range(size))
    value_set = set(values)
    value_dict = {value: True for value in values}
    target = size - 1
    loops = 10_000

    print(f"\nCollection size: {size}")
    print("list:", timeit(lambda v=values, t=target: t in v, number=loops))
    print("set:", timeit(lambda v=value_set, t=target: t in v, number=loops))
    print("dict:", timeit(lambda v=value_dict, t=target: t in v, number=loops))