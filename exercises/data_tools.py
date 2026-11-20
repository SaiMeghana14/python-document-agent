"""Practise CSV handling, missing values, Decimal, pandas and NumPy."""
import csv
from decimal import Decimal
from pathlib import Path

import numpy as np
import pandas as pd

# File locations
DATA_FILE = Path("samples/input/expenses.csv")
CLEAN_FILE = Path("data/expenses_cleaned.csv")

def clean_csv(path: Path, output_path: Path) -> pd.DataFrame:
    """Read a CSV, remove duplicate rows and save a cleaned copy."""

    # Keep employee IDs as strings so leading zeros are not lost.
    data = pd.read_csv(path, dtype={"employee_id": "string"})

    # Remove duplicate rows.
    data = data.drop_duplicates()

    # Create the output folder if it does not exist.
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Save the cleaned data.
    data.to_csv(output_path, index=False)
    return data

def plain_python_totals(path: Path) -> dict[str, Decimal]:
    """Calculate department totals using Python and Decimal."""

    totals: dict[str, Decimal] = {}

    with path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            department = row["department"].strip()

            if not department:
                department = "(missing department)"

            amount_text = row["amount"].strip()

            # Skip rows where the amount is missing.
            if not amount_text:
                continue

            amount = Decimal(amount_text)
            totals[department] = (
                totals.get(department, Decimal(0)) + amount
            )

    return totals

def pandas_totals(path: Path) -> dict[str, Decimal]:
    """Calculate department totals using pandas."""
    data = pd.read_csv(path, dtype={"employee_id": "string"})

    # Replace missing department names.
    data["department"] = data["department"].fillna(
        "(missing department)"
    )

    # Convert amounts to numbers.
    data["amount"] = pd.to_numeric(
        data["amount"], errors="coerce"
    )

    # Group rows by department and calculate totals.
    grouped = data.groupby("department")["amount"].sum(min_count=1)
    return {
        name: Decimal(str(value))
        for name, value in grouped.items()
        if pd.notna(value)
    }

def compare_totals(path: Path) -> None:
    """Compare Python totals with pandas totals."""

    python_result = plain_python_totals(path)
    pandas_result = pandas_totals(path)

    print("\nPlain Python totals:", python_result)
    print("Pandas totals:", pandas_result)
    print("Results match:", python_result == pandas_result)

def show_missing_values(data: pd.DataFrame) -> None:
    """Display missing-value counts and affected rows."""

    print("\nMissing values:")
    print(data.isna().sum())

    print("\nRows with missing values:")
    print(data[data.isna().any(axis=1)])

def fill_missing_values(data: pd.DataFrame) -> pd.DataFrame:
    """Fill missing department names and amounts."""

    filled_data = data.copy()

    filled_data["department"] = filled_data["department"].fillna(
        "Unknown"
    )

    filled_data["amount"] = filled_data["amount"].fillna(0)

    print("\nAfter filling missing values:")
    print(filled_data)

    return filled_data

def join_example() -> None:
    """Practise joining two tables and validating duplicate keys."""

    orders = pd.DataFrame(
        {
            "order_id": [1, 2],
            "employee_id": ["0012", "0013"],
        }
    )
    employees = pd.DataFrame(
        {
            "employee_id": ["0012", "0012", "0013"],
            "department": ["Engineering", "Contractor", "Sales"],
        }
    )

    print("\nOrders before join:", len(orders))

    try:
        result = orders.merge(
            employees,
            on="employee_id",
            how="left",
            validate="many_to_one",
        )

        print("Join result:")
        print(result)

    except pd.errors.MergeError as error:
        print("Join stopped because employee_id is not unique:")
        print(error)

def numpy_example() -> None:
    """Practise NumPy arrays, shapes, data types and broadcasting."""
    amounts = np.array(
        [
            [10, 20, 30],
            [40, 50, 60],
        ]
    )
    tax_rates = np.array([0.05, 0.10, 0.15])

    print("\nNumPy example:")

    print("Amounts:")
    print(amounts)

    print("Shape:", amounts.shape)
    print("Data type:", amounts.dtype)

    print("Tax rates:", tax_rates)
    print("Tax rates shape:", tax_rates.shape)

    # Each column gets its corresponding tax rate.
    amounts_with_tax = amounts * (1 + tax_rates)

    print("\nAmounts with tax (broadcasting):")
    print(amounts_with_tax)


def main() -> None:
    """Run all CSV and data-handling exercises."""

    # 1. Clean the CSV file.
    cleaned = clean_csv(DATA_FILE, CLEAN_FILE)

    print("Cleaned CSV saved to:", CLEAN_FILE)

    # 2. Display employee IDs.
    print("\nEmployee IDs:")
    print(cleaned["employee_id"].tolist())

    # 3. Check missing values.
    show_missing_values(cleaned)

    # 4. Fill missing values in a separate copy.
    filled_data = fill_missing_values(cleaned)

    # 5. Reload the saved CSV and check employee IDs.
    reloaded = pd.read_csv(
        CLEAN_FILE,
        dtype={"employee_id": "string"},
    )
    print("\nReloaded employee IDs:")
    print(reloaded["employee_id"].tolist())

    print(
        "Reloaded missing amounts:",
        reloaded["amount"].isna().sum(),
    )

    # 6. Compare Python and pandas calculations.
    compare_totals(CLEAN_FILE)

    # 7. Practise pandas joins.
    join_example()

    # 8. Practise NumPy.
    numpy_example()

if __name__ == "__main__":
    main()