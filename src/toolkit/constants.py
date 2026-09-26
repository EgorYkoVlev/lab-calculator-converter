LENGTH_UNITS: set[str] = {"mm", "cm", "m", "km"}
TEMPERATURE_UNITS: set[str] = {"c", "f", "k"}
WEIGHT_UNITS: set[str] = {"kg", "g"}

ABSOLUTE_ZERO_CELSIUS: float = -273.15
ABSOLUTE_ZERO_KELVIN: float = 0.0
ABSOLUTE_ZERO_FAHRENHEIT: float = -459.67

LENGTH_UNITS_COEFFICIENTS: dict[str, float] = {"mm":0.001, "cm": 0.01, "m":1, "km":1000}
WEIGHT_UNITS_COEFFICIENTS: dict[str, float] = {"g":0.001, "kg":1}

OPERATOR_PRECEDENCE: dict[str, int] = {
        "+":1,
        "-":1,
        "*":2,
        "/":2,
        "//":2,
        "%":2,
        "u-":3,
        "u+":3
    }
