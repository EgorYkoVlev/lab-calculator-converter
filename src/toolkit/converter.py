from toolkit.constants import (
    ABSOLUTE_ZERO_CELSIUS,
    ABSOLUTE_ZERO_FAHRENHEIT,
    ABSOLUTE_ZERO_KELVIN,
    LENGTH_UNITS,
    LENGTH_UNITS_COEFFICIENTS,
    TEMPERATURE_UNITS,
    WEIGHT_UNITS,
    WEIGHT_UNITS_COEFFICIENTS,
)
from toolkit.errors import (
    BelowAbsoluteZeroError,
    IncompatibleUnitsError,
    InvalidValueError,
    UnknownUnitError,
)


def validate(value: float, from_unit: str, to_unit: str) -> None:
    """Check the validity if the input arguments."""
    units_list: list[set] = [LENGTH_UNITS, WEIGHT_UNITS, TEMPERATURE_UNITS]

    source_unit_validate: bool = any(from_unit in i for i in units_list)
    target_unit_validate: bool = any(to_unit in i for i in units_list)

    if not(source_unit_validate and target_unit_validate):
        raise UnknownUnitError("unknown unit(s)")

    for units in units_list:

        if (from_unit in units) and (to_unit not in units):
            raise IncompatibleUnitsError("incompatible units")

    if (from_unit in LENGTH_UNITS or from_unit in WEIGHT_UNITS) and value < 0:
            raise InvalidValueError(f"value of {from_unit} cannot be negative")

    if from_unit in TEMPERATURE_UNITS:

        match from_unit:
            case "c":
                if value < ABSOLUTE_ZERO_CELSIUS:
                    raise BelowAbsoluteZeroError("below absolute zero")
            case "k":
                if value < ABSOLUTE_ZERO_KELVIN:
                    raise BelowAbsoluteZeroError("below absolute zero")
            case "f":
                if value < ABSOLUTE_ZERO_FAHRENHEIT:
                    raise BelowAbsoluteZeroError("below absolute zero")

def convert(value: float, from_unit: str, to_unit: str) -> float:
    """Convert the value between compatible units."""
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    validate(value, from_unit, to_unit)

    if from_unit in LENGTH_UNITS:

        match from_unit:
            case "mm":
                interim_value = value * LENGTH_UNITS_COEFFICIENTS[from_unit]
            case "cm":
                interim_value = value * LENGTH_UNITS_COEFFICIENTS[from_unit]
            case "m":
                interim_value = value * LENGTH_UNITS_COEFFICIENTS[from_unit]
            case "km":
                interim_value = value * LENGTH_UNITS_COEFFICIENTS[from_unit]

        match to_unit:
            case "mm":
                target_value = interim_value / LENGTH_UNITS_COEFFICIENTS[to_unit]
            case "cm":
                target_value = interim_value / LENGTH_UNITS_COEFFICIENTS[to_unit]
            case "m":
                target_value = interim_value / LENGTH_UNITS_COEFFICIENTS[to_unit]
            case "km":
                target_value = interim_value / LENGTH_UNITS_COEFFICIENTS[to_unit]

        return target_value

    if from_unit in WEIGHT_UNITS:

        match from_unit:
            case "g":
                interim_value = value * WEIGHT_UNITS_COEFFICIENTS[from_unit]
            case "kg":
                interim_value = value * WEIGHT_UNITS_COEFFICIENTS[from_unit]

        match to_unit:
            case "g":
                target_value = interim_value / WEIGHT_UNITS_COEFFICIENTS[to_unit]
            case "kg":
                target_value = interim_value / WEIGHT_UNITS_COEFFICIENTS[to_unit]

        return target_value

    if from_unit in TEMPERATURE_UNITS:

        match from_unit:
            case "k":
                interim_value = value - 273.15
            case "f":
                interim_value = (value - 32) * (5/9)
            case "c":
                interim_value = value

        match to_unit:
            case "k":
                target_value = interim_value + 273.15
            case "f":
                target_value = interim_value * (9/5) + 32
            case "c":
                target_value = interim_value

    return target_value
