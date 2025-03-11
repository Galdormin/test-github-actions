from math import sqrt


def add(x: int, y: int) -> int:
    return x + y


def sub(x: int, y: int) -> int:
    return x - y


def mul(x: int, y: int) -> int:
    return x * y


def div(x: int, y: int) -> int:
    if y == 0:
        raise ValueError("Cannot divide by 0.")

    return x // y


def root(x: int) -> float:
    return sqrt(x)


def square(x: int) -> int:
    return x * x
