"""CSV, Decimal, pandas and NumPy practice using the sample expenses file."""

import csv
from decimal import Decimal
from pathlib import Path

import numpy as np
import pandas as pd

DATA_FILE = Path("samples/input/expenses.csv")

def plain_python_totals(path: Path) -> dict[str, Decimal]:
    totals: dict[str, Decimal] = {}
    with path.open("r", encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            department = row["department"]
            totals[department] = totals.get(department, Decimal(0)) + Decimal(row["amount"])
    return totals

def pandas_totals(path: Path) -> pd.Series:
    frame = pd.read_csv(path, dtype={"employee_id": "string"})
    frame["amount"] = pd.to_numeric(frame["amount"], errors="coerce")
    frame["amount"] = frame["amount"].fillna(0)
    return frame.groupby("department")["amount"].sum()

def join_example() -> None:
    orders = pd.DataFrame({"order_id": [1, 2], "employee_id": ["0012", "0013"]})
    employees = pd.DataFrame({
        "employee_id": ["0012", "0012", "0013"],
        "department": ["Engineering", "Contractor", "Sales"],
    })
    joined = orders.merge(employees, on="employee_id", how="left")
    print("Rows before join:", len(orders))
    print("Rows after join:", len(joined))
    print("A non-unique employee key can multiply rows:")
    print(joined)

def numpy_example() -> None:
    values = np.array([10, 20, 30], dtype=np.int64)
    tax_rate = 0.1
    print("Shape:", values.shape)
    print("Data type:", values.dtype)
    print("With tax:", values * (1 + tax_rate))

if __name__ == "__main__":
    print("Plain Python totals:", plain_python_totals(DATA_FILE))
    print("Pandas totals:")
    print(pandas_totals(DATA_FILE))
    join_example()
    numpy_example()
