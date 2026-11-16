"""Examples using pathlib, JSON, regular expressions, dates and Decimal."""

import json
import re
from datetime import UTC, datetime
from decimal import Decimal
from pathlib import Path

if __name__ == "__main__":
    sample_path = Path("samples/input/expenses.csv")
    print("File exists:", sample_path.exists())
    print("File size:", sample_path.stat().st_size)

    employee_code = "0012"
    print("Leading-zero ID stays text:", employee_code)

    amount = Decimal("125.50") + Decimal("45.25")
    print("Exact decimal total:", amount)
    print("Float example (may show rounding):", 0.1 + 0.2)

    text = "Contact: intern@example.com"
    match = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    print("Email found:", match.group(0) if match else "none")

    record = {
        "created_at": datetime.now(UTC).isoformat(),
        "employee_code": employee_code,
        "amount": str(amount),
    }
    output_path = Path("data/exercise_record.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(record, indent=4), encoding="utf-8")
    print("Saved:", output_path)
