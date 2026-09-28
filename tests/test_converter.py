import pytest

from toolkit import converter
from toolkit.errors import (
    BelowAbsoluteZeroError,
    IncompatibleUnitsError,
    InvalidValueError,
    UnknownUnitError,
)


def test_convert_length():
    assert converter.convert(1000, "mm", "m") == 1

def test_convert_weight():
    assert converter.convert(1.5, "kg", "g") == 1500

def test_convert_temperature_from_c_to_f():
    assert converter.convert(0, "c", "f") == 32

def test_convert_temperature_from_c_to_k():
    assert converter.convert(-273.15, "c", "k") == 0

def test_convert_temperature_from_f_to_k():
    assert converter.convert(302, "f", "k") == pytest.approx(423.15)

def test_upper_case():
    assert converter.convert(1, "kM", "CM") == 100_000

def test_below_absolute_zero_c():
    with pytest.raises(BelowAbsoluteZeroError):
        converter.convert(-273.16, "c", "k")

def test_below_absolute_zero_f():
    with pytest.raises(BelowAbsoluteZeroError):
        converter.convert(-460, "f", "c")

def test_below_absolute_zero_k():
    with pytest.raises(BelowAbsoluteZeroError):
        converter.convert(-1, "k", "c")

def test_unknown_units():
    with pytest.raises(UnknownUnitError):
        converter.convert(1, "in", "ml")

def test_incompatible_units():
    with pytest.raises(IncompatibleUnitsError):
        converter.convert(1, "kg", "m")

def test_invalid_value():
    with pytest.raises(InvalidValueError):
        converter.convert(-20, "cm", "m")
