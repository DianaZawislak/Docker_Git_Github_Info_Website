"""Testing the Calculator"""

import pytest

from calculator import Calculator


def test_calculator_add_method():
    """Testing the Calculator Addition"""
    # ARRANGE
    tuple_list = (1.0, 2.0)
    # ACT
    result = Calculator.add(tuple_list)
    # ASSERT
    assert result == 3.0


def test_calculator_subtract_method():
    """Testing the Calculator Subtract"""
    tuple_list = (1.0, 2.0)
    assert Calculator.subtract(tuple_list) == -1.0


def test_calculator_multiply_method():
    """Testing the Calculator Multiply"""
    tuple_list = (1.0, 2.0)
    assert Calculator.multiply(tuple_list) == 2.0


def test_calculator_divide_method():
    """ Testing the calculator division"""
    # ARRANGE
    tuple_list = (1.0, 2.0)
    # ACT
    result = Calculator.divide(tuple_list)
    # ASSERT
    assert result == 0.5


def test_calculator_division_exception():
    """ Testing division exception for division by zero"""
    # ARRANGE
    tuple_list = (1.0, 0.0)
    # ACT
    with pytest.raises(ZeroDivisionError):
        result = Calculator.divide(tuple_list)
    # ASSERT
        assert result is True
