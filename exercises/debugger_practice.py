"""Practise debugging a calculation with an intentional logical error."""

def calculate_total(price: float, quantity: int) -> float:
    print("Calculating total...")

    # Intentional mistake: addition is used instead of multiplication.
    total = price + quantity
    return total

price = 100
quantity = 3
result = calculate_total(price, quantity)
print("Final total:", result)