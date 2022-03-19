"""Testing the Calculator"""
from unittest import result

import pytest

from calculator import Calculator


def tuple_list():
    """Arranging data for AAA"""
    return 2, 4


def test_calculator_add_method():
    """Testing the Calculator Addition"""

    # Act for AAA
    result = Calculator.add(tuple_list())

    # Assertion for AAA
    assert result == 6


def test_calculator_subtract_method():
    """Testing the Calculator Subtract"""
    tuple_list = (2, 4)
    assert Calculator.subtract(tuple_list) == -2


def test_calculator_multiply_method():
    """Testing the Calculator Multiply"""
    tuple_list = (2, 4)
    assert Calculator.multiply(tuple_list) == 8


def test_calculator_divide_method():
    """ Testing the calculator division"""
    # Arrange
    tuple_list = (2, 4)
    # Act
    result = Calculator.divide(tuple_list)
    # Assert
    assert result == 0.5


def test_calculator_division_exception():
    """ Testing division exception for division by zero"""
    # Arrange
    value_a = 1
    value_b = 0
    # Act
    with pytest.raises(ZeroDivisionError):
        Calculator.divide_numbers(value_a, value_b)
    assert result is True
