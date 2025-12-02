import argparse
import sys

import calculator
import history


def main():
    parser = argparse.ArgumentParser(description="A simple CLI calculator.")

    subparsers = parser.add_subparsers(dest="command", required=True)

    def add_math_args(p):
        p.add_argument("a", type=float, help="First number")
        p.add_argument("b", type=float, help="Second number")

    # --- add command
    add_parser = subparsers.add_parser("add", help="Add two numbers.")
    add_math_args(add_parser)

    # --- subtract command
    sub_parser = subparsers.add_parser("sub", help="Subtract two numbers.")
    add_math_args(sub_parser)

    # --- multiply command
    mul_parser = subparsers.add_parser("mul", help="Multiply two numbers.")
    add_math_args(mul_parser)

    # --- add command
    div_parser = subparsers.add_parser("div", help="Divide two numbers.")
    add_math_args(div_parser)

    # --- history command
    subparsers.add_parser("history", help="Show past calculations.")
    subparsers.add_parser("clear", help="Clear history.")

    args = parser.parse_args()

    if args.command == "history":
        records = history.load_history()
        if not records:
            print("No history found.")
        else:
            print(f"{'TIMESTAMP':<26} | {'OP':<5} | {'EXPRESSION':<20}")
            print("-" * 60)
            for r in records:
                expr = f"{r['a']} {r['operation']} {r['b']} = {r['result']}"
                print(f"{r['timestamp']:<25} | {r['operation']:<5} | {expr}")

        return

    if args.command == "clear":
        history.clear_history()
        print("History cleared.")
        return

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
        history.save_record(args.command, args.a, args.b, result)

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
