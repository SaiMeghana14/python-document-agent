"""Practise CSV cleaning, Decimal, pandas, joins and NumPy."""

import csv
from decimal import Decimal
from pathlib import Path

import numpy as np
import pandas as pd

DATA_FILE = Path("samples/input/expenses.csv")
CLEAN_FILE = Path("data/expenses_cleaned.csv")

def clean_csv(path: Path, output_path: Path) -> pd.DataFrame:
    """Remove duplicate rows and save a cleaned copy without changing the source."""
    data = pd.read_csv(path, dtype={"employee_id": "string"})
    data = data.drop_duplicates()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    data.to_csv(output_path, index=False)
    return data

def plain_python_totals(path: Path) -> dict[str, Decimal]:
    """Add available amounts by department, keeping money as Decimal."""
    totals: dict[str, Decimal] = {}
    with path.open("r", encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            department = row["department"].strip() or "(missing department)"
            amount_text = row["amount"].strip()
            if not amount_text:
                continue
            amount = Decimal(amount_text)
            totals[department] = totals.get(department, Decimal(0)) + amount
    return totals

def pandas_totals(path: Path) -> dict[str, Decimal]:
    """Calculate the same totals with pandas."""
    data = pd.read_csv(path, dtype={"employee_id": "string"})
    data["department"] = data["department"].fillna("(missing department)")
    data["amount"] = pd.to_numeric(data["amount"], errors="coerce")
    grouped = data.groupby("department", dropna=False)["amount"].sum(min_count=1)
    return {name: Decimal(str(value)) for name, value in grouped.items() if pd.notna(value)}

def compare_totals(path: Path) -> None:
    python_result = plain_python_totals(path)
    pandas_result = pandas_totals(path)
    print("Plain Python totals:", python_result)
    print("Pandas totals:", pandas_result)
    print("Results match:", python_result == pandas_result)

def join_example() -> None:
    orders = pd.DataFrame({"order_id": [1, 2], "employee_id": ["0012", "0013"]})
    employees = pd.DataFrame(
        {
            "employee_id": ["0012", "0012", "0013"],
            "department": ["Engineering", "Contractor", "Sales"],
        }
    )

    print("Orders before join:", len(orders))
    try:
        result = orders.merge(
            employees, on="employee_id", how="left", validate="many_to_one"
        )
        print(result)
    except pd.errors.MergeError as error:
        print("Join stopped because employee_id is not unique:", error)

def numpy_example() -> None:
    amounts = np.array([[10, 20, 30], [40, 50, 60]])
    tax_rates = np.array([0.05, 0.10, 0.15])
    print("Shape:", amounts.shape)
    print("Data type:", amounts.dtype)
    print("Tax rates shape:", tax_rates.shape)
    print("Amounts with tax (broadcasting):")
    print(amounts * (1 + tax_rates))

def main() -> None:
    cleaned = clean_csv(DATA_FILE, CLEAN_FILE)
    print("Cleaned CSV saved to:", CLEAN_FILE)
    print("Employee IDs:", cleaned["employee_id"].tolist())
    print("Missing values:")
    print(cleaned.isna().sum())

    # Read the saved file again to check the values were preserved.
    reloaded = pd.read_csv(CLEAN_FILE, dtype={"employee_id": "string"})
    print("Reloaded employee IDs:", reloaded["employee_id"].tolist())
    print("Reloaded missing amounts:", reloaded["amount"].isna().sum())

    compare_totals(CLEAN_FILE)
    join_example()
    numpy_example()

if __name__ == "__main__":
    main()