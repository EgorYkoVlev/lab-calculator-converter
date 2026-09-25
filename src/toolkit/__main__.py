import argparse
import sys

from toolkit.calculator import calculate
from toolkit.errors import CalculatorError


def create_parser() -> argparse.ArgumentParser:
    """Create the command-line argument parser."""
    parser = argparse.ArgumentParser(
        prog="toolkit",
        description="Calculator and unit converter.",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    calc_parser = subparsers.add_parser(
        "calc",
        help="Evaluate an arithmetic expression.",
    )
    calc_parser.add_argument(
        "expression",
        type=str,
        help="Arithmetic expression to evaluate.",
    )

    convert_parser = subparsers.add_parser(
        "convert",
        help="Convert a value between compatible units.",
    )
    convert_parser.add_argument(
        "value",
        type=float,
        help="Value to convert.",
    )
    convert_parser.add_argument(
        "--from",
        dest="from_unit",
        type=str,
        required=True,
        help="Source unit.",
    )
    convert_parser.add_argument(
        "--to",
        dest="to_unit",
        type=str,
        required=True,
        help="Target unit.",
    )

    return parser

def format_result(result: float) -> str:
    if result.is_integer():
        return str(int(result))

    return str(result)

def main() -> int:
    """Run the command-line application."""
    parser = create_parser()
    args = parser.parse_args()

    if args.command == "calc":

        try:
            res = calculate(args.expression)
        except CalculatorError as e:
            print(f"Calculator error: {e}", file=sys.stderr)
            return 2

        print(format_result(res))

    elif args.command == "convert":
        print(args.value, args.from_unit, args.to_unit)

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
