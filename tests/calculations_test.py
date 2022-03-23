"""Testing the Calculator with AAA"""
import pytest
from calculator.Calculation import Addition, Subtraction, Multiplication, Division


def test_calculation_addition_instance():
    """Testing the Calculator Addition"""
    # ARRANGE
    tuple_list = (1, 2)
    # ACT
    calculation = Addition.create(tuple_list)
    # ASSERT
    assert isinstance(calculation, Addition)


def test_calculation_subtraction_instance():
    """Testing the Calculator Subtract"""
    # ARRANGE
    tuple_list = (1, 2)
    # ACT
    calculation = Subtraction.create(tuple_list)
    # ASSERT
    assert isinstance(calculation, Subtraction)


def test_calculation_multiplication_instance():
    """Testing the Calculator Multiply"""
    # ARRANGE
    tuple_list = (1, 2)
    # ACT
    calculation = Multiplication.create(tuple_list)
    # ASSERT
    assert isinstance(calculation, Multiplication)


def test_calculation_division_instance():
    """Testing the Calculator Multiply"""
    # ARRANGE
    tuple_list = (1, 2)
    # ACT
    calculation = Division.create(tuple_list)
    # ASSERT
    assert isinstance(calculation, Division)


def test_calculation_add_get_result_method():
    """Testing the Calculator"""
    # ARRANGE
    tuple_list = (1, 2)
    # ACT
    calculation = Addition.create(tuple_list)
    # ASSERT
    assert calculation.get_result() == 3


def test_calculation_subtract_get_result_method():
    """Testing the Calculator Subtract"""
    # ARRANGE
    tuple_list = (1, 2)
    # ACT
    calculation = Subtraction.create(tuple_list)
    # ASSERT
    assert calculation.get_result() == -1


def test_calculation_multiply_get_result_method():
    """Testing the Calculator Multiplication"""
    # ARRANGE
    tuple_list = (1, 2)
    # ACT
    calculation = Multiplication.create(tuple_list)
    # ASSERT
    assert calculation.get_result() == 2


def test_calculation_division_get_results_method():
    """Testing the calculator division"""
    # ARRANGE
    tuple_list = (1, 2)
    # ACT
    calculation = Division.create(tuple_list)
    # ASSERT
    assert calculation.get_result() == 0.5


def test_calculator_division_exception():
    """ Testing division exception for division by zero"""
    # ARRANGE
    tuple_list = (1.0, 0.0)
    # ACT
    calculation = Division.create(tuple_list)
    # ASSERT
    with pytest.raises(ZeroDivisionError):
        result = calculation.get_result()
        assert result is True
