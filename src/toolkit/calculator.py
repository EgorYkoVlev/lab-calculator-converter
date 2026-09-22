from toolkit.errors import InvalidCharacterError, InvalidSyntaxError, EmptyExpressionError


def tokenize(expression: str) -> list[str]:
    expression = expression.replace(" ", "")
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

        raise InvalidCharacterError(f"invalid character: {char}")

    if not tokens:
        raise EmptyExpressionError("expression is empty")

    return tokens

# def validate(tokens: list[str]) -> None:
#
#
# def calculate(tokens: list[str]) -> float:
