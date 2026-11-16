"""A few short examples for the Python foundations as part of the assignment."""

from copy import copy, deepcopy
from dataclasses import dataclass
from functools import wraps
from time import perf_counter


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
        elapsed = perf_counter() - started
        print(f"{function.__name__} took {elapsed:.6f} seconds")
        return result

    return wrapper

@dataclass
class Employee:
    name: str
    _salary: float

    @property
    def salary(self) -> float:
        return self._salary

    @salary.setter
    def salary(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Salary cannot be negative.")
        self._salary = amount

    @classmethod
    def from_record(cls, record: dict) -> "Employee":
        return cls(name=record["name"], _salary=float(record["salary"]))

    @staticmethod
    def is_work_email(address: str) -> bool:
        return address.endswith("@example.com")

@timed
def add_numbers(values: list[int]) -> int:
    return sum(values)

if __name__ == "__main__":
    counter = make_counter()
    print("Closure:", counter(), counter(), counter())

    original = {"scores": [10, 20]}
    shallow = copy(original)
    deep = deepcopy(original)
    original["scores"].append(30)
    print("Original:", original)
    print("Shallow copy shares nested list:", shallow)
    print("Deep copy keeps its own nested list:", deep)

    employee = Employee.from_record({"name": "Asha", "salary": "35000"})
    employee.salary = 36000
    print("Employee:", employee)
    print("Work email:", Employee.is_work_email("asha@example.com"))
    print("Sum:", add_numbers([1, 2, 3, 4]))
