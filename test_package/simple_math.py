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
