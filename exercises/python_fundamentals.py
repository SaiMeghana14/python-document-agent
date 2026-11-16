"""Short examples for common Python language and object concepts."""
# ruff: noqa: B006, B023

from copy import copy, deepcopy
from dataclasses import asdict, dataclass
from functools import wraps
from time import perf_counter


def add_item_bad(item: str, items: list[str] = []) -> list[str]:
    """This example is intentionally wrong: calls share the same list."""
    items.append(item)
    return items

def add_item(item: str, items: list[str] | None = None) -> list[str]:
    """Use None as the default instead of sharing one mutable list."""
    if items is None:
        items = []
    items.append(item)
    return items

def make_multiplier(number: int):
    def multiply(value: int) -> int:
        return value * number

    return multiply

def make_multipliers_bad(numbers: list[int]):
    """This example is intentionally wrong: every function uses the last value."""
    return [lambda value: value * number for number in numbers]

def make_multipliers(numbers: list[int]):
    """Create functions that remember each loop value."""
    return [lambda value, number=number: value * number for number in numbers]

def make_counter():
    count = 0

    def next_value():
        nonlocal count
        count += 1
        return count

    return next_value

def timed(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        started = perf_counter()
        result = function(*args, **kwargs)
        print(f"{function.__name__} took {perf_counter() - started:.6f} seconds")
        return result
    return wrapper

@dataclass
class Employee:
    name: str
    _salary: float
    def give_raise(self, amount: float) -> None:
        """An instance method uses data belonging to this employee."""
        if amount < 0:
            raise ValueError("Raise cannot be negative.")
        self._salary += amount

    @property
    def salary(self) -> float:
        return self._salary

    @salary.setter
    def salary(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Salary cannot be negative.")
        self._salary = amount

    @classmethod
    def from_record(cls, record: dict[str, str]) -> "Employee":
        return cls(record["name"], float(record["salary"]))

    @staticmethod
    def is_work_email(address: str) -> bool:
        return address.endswith("@example.com")

@timed
def add_numbers(values: list[int]) -> int:
    """Return the sum of a list of numbers."""
    return sum(values)


def exception_example() -> None:
    try:
        number = int("not a number")
    except ValueError as error:
        print("Could not convert the value:", error)
    else:
        print("Converted value:", number)
    finally:
        print("The conversion example has finished.")

def main() -> None:
    print("Mutable default argument problem:")
    print(add_item_bad("notes"))
    print(add_item_bad("policy"))
    print("Both calls share one list. The fixed version starts a new list:")
    first = add_item("notes")
    second = add_item("policy")
    print(first, second)

    print("Shallow and deep copy:")
    original = {"scores": [10, 20]}
    shallow = copy(original)
    deep = deepcopy(original)
    original["scores"].append(30)
    print("Original:", original)
    print("Shallow copy:", shallow)
    print("Deep copy:", deep)

    print("Closure values:")
    double = make_multiplier(2)
    triple = make_multiplier(3)
    print(double(5), triple(5))

    print("Closure loop problem:")
    wrong_functions = make_multipliers_bad([1, 2, 3])
    print([function(10) for function in wrong_functions])
    print("Fixed closure loop:")
    functions = make_multipliers([1, 2, 3])
    print([function(10) for function in functions])

    counter = make_counter()
    print("Counter:", counter(), counter(), counter())

    employee = Employee.from_record({"name": "Asha", "salary": "35000"})
    employee.give_raise(1000)
    print("Employee as a dataclass:", employee)
    print("Same record as a dictionary:", asdict(employee))
    print("Salary property:", employee.salary)
    print("Work email:", Employee.is_work_email("asha@example.com"))
    print("Sum:", add_numbers([1, 2, 3, 4]))
    exception_example()

if __name__ == "__main__":
    main()
