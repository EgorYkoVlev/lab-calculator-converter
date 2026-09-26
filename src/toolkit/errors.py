class ToolkitError(Exception):
    pass


class CalculatorError(ToolkitError):
    pass


class InvalidCharacterError(CalculatorError):
    pass


class InvalidSyntaxError(CalculatorError):
    pass


class EmptyExpressionError(CalculatorError):
    pass


class MissingOperatorError(CalculatorError):
    pass


class DivisionByZeroError(CalculatorError):
    pass

class MissingOperandError(CalculatorError):
    pass


class ConverterError(ToolkitError):
    pass


class UnknownUnitError(ConverterError):
    pass

class IncompatibleUnitsError(ConverterError):
    pass

class InvalidValueError(ConverterError):
    pass

class BelowAbsoluteZeroError(ConverterError):
    pass
