import pytest

from test_package.simple_math import add, sub, mul, div, div_f, root, square


def test_add():
    assert add(5, 6) == 11
    assert add(6, 5) == 11


def test_sub():
    assert sub(6, 5) == 1
    assert sub(5, 6) == -1


def test_mul():
    assert mul(5, 6) == 30
    assert mul(6, 5) == 30


def test_div():
    assert div(5, 6) == 0
    assert div(6, 5) == 1

    with pytest.raises(ValueError):
        assert div(5, 0)


def test_div_f():
    assert div_f(10, 5) == 2.0
    assert div_f(6, 5) == 1.2

    with pytest.raises(ValueError):
        assert div_f(5, 0)


def test_root():
    assert root(4) == 2.0


def test_square():
    assert square(2) == 4
    assert square(-2) == 4
