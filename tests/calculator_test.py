"""Testing the Calculator"""

import pytest

from calculator import Calculator


def tuple_list():
    """Arranging data for AAA"""
    return 1.0, 2.0


def test_calculator_add_method():
    """Testing the Calculator Addition"""
    # Act
    result = Calculator.add(tuple_list())
    # Assert
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
    # Arrange
    tuple_list = (1.0, 2.0)
    # Act
    result = Calculator.divide(tuple_list)
    # Assert
    assert result == 0.5


def test_calculator_division_exception():
    """ Testing division exception for division by zero"""
    # Arrange
    tuple_list = (1.0, 0.0)
    # Act
    with pytest.raises(ZeroDivisionError):
        result = Calculator.divide(tuple_list)
    # Assert
        assert result is True
