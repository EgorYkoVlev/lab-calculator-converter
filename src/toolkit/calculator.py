from toolkit.errors import (InvalidCharacterError,
                            InvalidSyntaxError,
                            EmptyExpressionError,
                            MissingOperatorError)

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
                    raise InvalidSyntaxError("number is expected after dot")

                while i < len(expression) and expression[i].isdigit():
                    i += 1

            tokens.append(expression[start:i])
            continue

        if char in ["(", ")"]:
            i += 1
            tokens.append(char)
            continue

        raise InvalidCharacterError(f"invalid character: {char}")

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

                if i < len(tokens) - 1 and is_number(tokens[i+1]):
                    i += 1
                    continue

                raise InvalidSyntaxError("invalid syntax")

            if token in ["*", "/", "%", "//"]:
                raise InvalidSyntaxError("invalid syntax")

        if is_number(token):

            if i < len(tokens) - 1 and tokens[i + 1] == "(":
                raise InvalidSyntaxError("invalid syntax")

            if i < len(tokens) - 1 and is_number(tokens[i + 1]):
                raise MissingOperatorError("missing operator")

            i += 1
            continue

        if token == "(":
            open_parentheses_count += 1

            if i < len(tokens) - 1 and tokens[i + 1] in ["+", "-"]:

                if i + 1 < len(tokens) - 1 and is_number(tokens[i+2]):
                    i += 2
                    continue

            if i < len(tokens) - 1 and (tokens[i + 1] in "(" or is_number(tokens[i + 1])):
                i += 1
                continue

            raise InvalidSyntaxError("invalid syntax")

        if token == ")":
            closing_parentheses_count += 1

            if closing_parentheses_count > open_parentheses_count:
                raise InvalidSyntaxError("invalid syntax")

            if i < len(tokens) - 1 and (is_number(tokens[i + 1]) or tokens[i + 1] == "("):
                raise InvalidSyntaxError("invalid syntax")

            i += 1
            continue

        if token in ["*", "/", "%", "//", "+", "-"]:

            if i == len(tokens) - 1 or tokens[i + 1] in ["*", "/", "%", "//", ")"]:
                raise InvalidSyntaxError("invalid syntax")

            if i < len(tokens) - 2 and tokens[i + 1] in ["+", "-"] and (not is_number(tokens[i + 2])):
                raise InvalidSyntaxError("invalid syntax")

            i += 1
            continue
    if closing_parentheses_count != open_parentheses_count:
        raise InvalidSyntaxError("invalid syntax")

# def calculate(expression: str) -> float:
#     pass
