import math
import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1.5) == 0.5

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-2, -3) == 1

def test_multiply():
    assert multiply(4, 0.5) == 2
    assert multiply(-3, -2) == 6

def test_divide_normal():
    assert divide(10, 2) == 5
    assert math.isclose(divide(7, 2), 3.5)

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
