class ToolkitError(Exception):
    pass


class CalculatorError(ToolkitError):
    pass


class ConverterError(ToolkitError):
    pass


class InvalidCharacterError(ToolkitError):
    pass


class InvalidSyntaxError(ToolkitError):
    pass


class EmptyExpressionError(ToolkitError):
    pass
