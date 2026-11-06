import argparse

from logger import Logger, LogLevel
from parentheses_validator import ParenthesesValidator


def main() -> None:
    parser = argparse.ArgumentParser(description="OOP laboratory: logging and parentheses")
    parser.add_argument("text", nargs="?", help="String to validate; omit to run the four required cases")
    parser.add_argument("--level", choices=[level.name for level in LogLevel], default="TRACE")
    parser.add_argument("--format", default="[%t] [%l] %n: %m", help="Placeholders: %%t %%l %%n %%m %%r")
    args = parser.parse_args()

    Logger.set_level(LogLevel[args.level])
    Logger.set_format(args.format)
    validator = ParenthesesValidator()

    if args.text is not None:
        result = validator.is_valid(args.text)
        print(f"Result: {str(result).lower()}")
        return

    cases = [("()", True), (")((()))", False), ("(", False), ("(())((()())())", True)]
    for text, expected in cases:
        print(f"\nInput: {text!r}; expected: {str(expected).lower()}")
        actual = validator.is_valid(text)
        print(f"Result: {str(actual).lower()}; test: {'PASS' if actual == expected else 'FAIL'}")


if __name__ == "__main__":
    main()
