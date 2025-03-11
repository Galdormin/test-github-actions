from math import sqrt


def add(x: int, y: int) -> int:
    """Add 2 integers."""
    return x + y


def sub(x: int, y: int) -> int:
    """Subtract 2 integers."""
    return x - y


def mul(x: int, y: int) -> int:
    """Multiply 2 integers."""
    return x * y


def div(x: int, y: int) -> int:
    """Divide 2 integers and return the integer division."""
    if y == 0:
        raise ValueError("Cannot divide by 0.")

    return x // y


def div_f(x: int, y: int) -> float:
    """Divide 2 integers and return the float division."""
    if y == 0:
        raise ValueError("Cannot divide by 0.")

    return x / y


def root(x: int) -> float:
    """Compute the square root of an integer."""
    return sqrt(x)


def square(x: int) -> int:
    """Compute the square of an integer."""
    return x * x
