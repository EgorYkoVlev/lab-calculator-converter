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


class ConverterError(ToolkitError):
    pass
