import argparse
import sys

import calculator


def main():
    parser = argparse.ArgumentParser(description="A simple CLI calculator.")

    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- add command
    add_parser = subparsers.add_parser("add", help="Add two numbers.")
    add_parser.add_argument("a", type=float, help="first number.")
    add_parser.add_argument("b", type=float, help="second number.")

    # --- subtract command
    add_parser = subparsers.add_parser("sub", help="Subtract two numbers.")
    add_parser.add_argument("a", type=float, help="first number.")
    add_parser.add_argument("b", type=float, help="second number.")

    # --- multiply command
    add_parser = subparsers.add_parser("mul", help="Multiply two numbers.")
    add_parser.add_argument("a", type=float, help="first number.")
    add_parser.add_argument("b", type=float, help="second number.")

    # --- add command
    add_parser = subparsers.add_parser("div", help="Divide two numbers.")
    add_parser.add_argument("a", type=float, help="first number.")
    add_parser.add_argument("b", type=float, help="second number.")

    args = parser.parse_args()

    result = 0.0

    try:
        if args.command == "add":
            result = calculator.add(args.a, args.b)
        elif args.command == "sub":
            result = calculator.subtract(args.a, args.b)
        elif args.command == "mul":
            result = calculator.multiply(args.a, args.b)
        elif args.command == "div":
            result = calculator.divide(args.a, args.b)

        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
