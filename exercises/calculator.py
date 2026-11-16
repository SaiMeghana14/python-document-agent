"""Small functions used to practise values, functions and exceptions."""

def calculate_total(prices: list[float]) -> float:
    if not prices:
        return 0.0
    return sum(prices)

def divide(first: float, second: float) -> float:
    try:
        return first / second
    except ZeroDivisionError as error:
        raise ValueError("The second number must not be zero.") from error

if __name__ == "__main__":
    print("Total:", calculate_total([10.5, 20.0, 4.5]))
    print("Division:", divide(10, 2))
