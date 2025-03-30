from decimal import Decimal

def add(a, b):
    """Add two numbers and return the result."""
    # Convert inputs to Decimal for precise decimal arithmetic
    # then convert back to float for compatibility with the rest of the code
    return float(Decimal(str(a)) + Decimal(str(b)))


def subtract(a, b):
    """Subtract two numbers and return the result."""
    # Convert inputs to Decimal for precise decimal arithmetic
    # then convert back to float for compatibility with the rest of the code
    return float(Decimal(str(a)) - Decimal(str(b)))