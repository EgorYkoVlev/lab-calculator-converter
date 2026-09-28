import pytest

from toolkit import calculator
from toolkit.errors import (
    DivisionByZeroError,
    EmptyExpressionError,
    InvalidCharacterError,
    InvalidSyntaxError,
    MissingOperandError,
    MissingOperatorError,
)


def test_priority_of_operations():
    assert calculator.calculate("2+3*4") == 14

def test_division():
    assert calculator.calculate("10 / 4") == 2.5

def test_multiplication_with_unary_operators():
    assert calculator.calculate("-2 * -3") == 6

def test_addition_with_unary_operators():
    assert calculator.calculate("1+-2") == -1

def test_expression_with_parentheses():
    assert calculator.calculate("4 * (12 / (-5 + 1))") == -12

def test_floating_point_numbers():
    assert calculator.calculate("12.5 / 0.8") == 15.625

def test_integer_division_and_mod():
    assert calculator.calculate("21 // 4 % 3") == 2

def test_empty_expression():
    with pytest.raises(EmptyExpressionError):
        calculator.calculate("")

def test_two_binary_operators_in_a_row():
    with pytest.raises(MissingOperandError):
        calculator.calculate("2*/3")

def test_invalid_character():
    with pytest.raises(InvalidCharacterError):
        calculator.calculate("1+a")

def test_division_by_zero():
    with pytest.raises(DivisionByZeroError):
        calculator.calculate("1/0")

def test_missing_operand():
    with pytest.raises(MissingOperandError):
        calculator.calculate("2 * 3 +")

def test_missing_operator():
    with pytest.raises(MissingOperatorError):
        calculator.calculate("2 + 3(8 - 7)")

def test_missing_digits_after_dot():
    with pytest.raises(InvalidSyntaxError):
        calculator.calculate("5.5 * 4.")
