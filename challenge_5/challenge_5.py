#!/usr/bin/python3
"""
Challenge 5 Module

TASK:
Create a function called factorial()
  - Takes one (1) int() argument
  - Returns int() calculated value
  - Returns int(0) if invalid input

    Example: factorial(4)   -> int(24)
             factorial('a') -> int(0)
             factorial(-1)  -> int(0)

Create a function named print_expanded()
  - Takes one (1) int() argument
  - Returns str() representation of calculations in decending order
  - Returns empty str('') on invalid input (i.e. empty string)

    Example: print_expanded(4)   -> '4x3x2x1 = 24'
             print_expanded('a') -> ''
             print_expanded(-1)  -> ''

INFO:
  A factorial is the product of a whole number and
  all positive whole numbers beneath it.
"""
import sys


def main():
    """
    Student will put all personal test code for challenge in main()
    Grading will be conducted souly against factorial() and print_expanded()
    """
    for value in sys.argv[1:]:
        print(f"factorial(value)      -> {factorial(value)}")
        print(f"print_expanded(value) -> {print_expanded(value)}")


def factorial(num: int) -> int:
    """factorial(int) -> int
    Returns factorial result of int(num) else 0
    """
    pass


def print_expanded(num: int) -> str:
    """print_expanded(int) -> str
    Returns a decending string of the calculations conducted
    and the resulting value.
    """
    pass


if __name__ == '__main__':
    main()
