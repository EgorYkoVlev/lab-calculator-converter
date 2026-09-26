from toolkit.constants import OPERATOR_PRECEDENCE
from toolkit.errors import (
    DivisionByZeroError,
    EmptyExpressionError,
    InvalidCharacterError,
    InvalidSyntaxError,
    MissingOperandError,
    MissingOperatorError
)

def is_number(expression: str) -> bool:
    try:
        float(expression)
        return True
    except ValueError:
        return False

def tokenize(expression: str) -> list[str]:
    tokens: list[str] = []
    i = 0

    while i < len(expression):
        char = expression[i]

        if char.isspace():
            i += 1
            continue

        if char in ["+", "-", "*", "/", "%"]:

            if char == "/" and i + 1 < len(expression) and expression[i + 1] == "/":
                tokens.append(expression[i:i + 2])
                i += 1
            else:
                tokens.append(char)

            i += 1
            continue

        if char.isdigit():
            start = i

            while i < len(expression) and expression[i].isdigit():
                i += 1

            if i < len(expression) and expression[i] == ".":
                i += 1

                if i == len(expression) or (not expression[i].isdigit()):
                    raise InvalidSyntaxError("digits are expected after dot")

                while i < len(expression) and expression[i].isdigit():
                    i += 1

            tokens.append(expression[start:i])
            continue

        if char in ["(", ")"]:
            i += 1
            tokens.append(char)
            continue

        raise InvalidCharacterError(f"invalid character: '{char}'")

    if not tokens:
        raise EmptyExpressionError("expression is empty")

    return tokens

def validate(tokens: list[str]) -> None:
    i = 0
    open_parentheses_count = 0
    closing_parentheses_count = 0

    while i < len(tokens):
        token = tokens[i]

        if i == 0:

            if token in ["+", "-"]:

                if i < len(tokens) - 1 and is_number(tokens[i + 1]):
                    i += 1
                    continue

                raise MissingOperandError("missing operand")

            if token in ["*", "/", "%", "//"]:
                raise MissingOperandError("missing operand")

        if is_number(token):

            if i < len(tokens) - 1 and tokens[i + 1] == "(":
                raise MissingOperatorError("missing operator")

            if i < len(tokens) - 1 and is_number(tokens[i + 1]):
                raise MissingOperatorError("missing operator")

            i += 1
            continue

        if token == "(":
            open_parentheses_count += 1

            if (i < len(tokens) - 2
                and tokens[i + 1] in ["+", "-"]
                and is_number(tokens[i + 2])
            ):
                i += 2
                continue

            if i < len(tokens) - 1 and (tokens[i + 1] == "(" or is_number(tokens[i + 1])):
                i += 1
                continue

            raise MissingOperandError("missing operand")

        if token == ")":
            closing_parentheses_count += 1

            if closing_parentheses_count > open_parentheses_count:
                raise InvalidSyntaxError("opening parenthesis missing")

            if i < len(tokens) - 1 and (is_number(tokens[i + 1]) or tokens[i + 1] == "("):
                raise MissingOperatorError("missing operator")

            i += 1
            continue

        if token in ["*", "/", "%", "//", "+", "-"]:

            if i == len(tokens) - 1 or tokens[i + 1] in ["*", "/", "%", "//", ")"]:
                raise MissingOperandError("missing operand(s)")

            if i < len(tokens) - 2 and tokens[i + 1] in ["+", "-"] and (not is_number(tokens[i + 2])):
                raise MissingOperandError("missing operand")

            i += 1
            continue
    if closing_parentheses_count != open_parentheses_count:
        raise InvalidSyntaxError("closing parenthesis(es) missing")

def convert_unary_operators(tokens: list[str]) -> list[str]:
    new_tokens: list[str] = tokens.copy()
    i = 0

    while i < len(new_tokens):
        token = new_tokens[i]

        if (
            token in ["+", "-"]
            and (
                i == 0
                or new_tokens[i - 1] == "("
                or new_tokens[i - 1] in ["*", "/", "%", "//", "+", "-"]
            )
        ):
            new_tokens.insert(i+2, f"u{token}")
            new_tokens.pop(i)
            i += 2
            continue

        i += 1

    return new_tokens

def infix_to_rpn(tokens: list[str]) -> list[str]:
    new_tokens: list[str] = convert_unary_operators(tokens)
    output: list[str] = []
    operators: list[str] = []
    i = 0

    while i < len(new_tokens):
        token = new_tokens[i]

        if is_number(token):
            output.append(token)
            i += 1
            continue

        if token in ["*", "/", "//", "%", "+", "-", "u-", "u+"]:
            priority = OPERATOR_PRECEDENCE[token]
            j = len(operators) - 1

            while j > -1:
                if operators[j] == "(":
                    break

                if OPERATOR_PRECEDENCE[operators[j]] >= priority:
                    output.append(operators.pop(j))
                    j -= 1
                    continue

                j -= 1

            operators.append(token)
            i += 1
            continue

        if token == "(":
            operators.append(token)
            i += 1
            continue

        if token == ")":

            while operators[-1] != "(":
                output.append(operators.pop())

            operators.pop()
            i += 1

    while operators:
        output.append(operators.pop())

    return output

def evaluate_rpn(rpn: list[str]) -> float  :
    stack: list[float] = []

    for token in rpn:

        if is_number(token):
            stack.append(float(token))
            continue

        b = stack.pop()

        if token not in ["u-", "u+"]:
            a = stack.pop()

        if token in ["/", "//", "%"] and b == 0:
            raise DivisionByZeroError("division by zero")

        match token:
            case "*":
                stack.append(a * b)
            case "+":
                stack.append(a + b)
            case "-":
                stack.append(a - b)
            case "u-":
                stack.append(-b)
            case "/":
                stack.append(a / b)
            case "//":
                stack.append(a // b)
            case "%":
                stack.append(a % b)
            case _:
                stack.append(b)

    return stack.pop()

def calculate(expression: str) -> float:
    tokens = tokenize(expression)
    validate(tokens)
    rpn = infix_to_rpn(tokens)
    return evaluate_rpn(rpn)
