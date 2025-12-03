import pytest
import calculator


def test_add():
    assert calculator.add(10, 5) == 15.0
    assert calculator.add(-1, -1) == -2.0


def test_subtract():
    assert calculator.subtract(10, 5) == 5.0


def test_multiply():
    assert calculator.multiply(3, 3) == 9.0


def test_divide():
    assert calculator.divide(10, 2) == 5.0


def test_divide_by_zero():
    # We expect a ValueError here. If it DOESN'T happen, the test fails.
    with pytest.raises(ValueError):
        calculator.divide(10, 0)
