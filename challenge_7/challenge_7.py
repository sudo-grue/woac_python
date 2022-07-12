#!/usr/bin/env python3
"""
challenge_7 Fibonacci
"""
from sys import argv

def main() -> None:
    for arg in [int(arg) for arg in argv[1:]]:
        print(f"{arg:>3} Index: {which_fibonacci(arg):>3}\tNext: {next_fibonacci(arg):>3}")


def which_fibonacci(value: int) -> int:
    """Returns the index of number if it's a fibonacci number

    Treats all fibonacci numbers as a 0-indexed value. With 0 == idx[0],
    1 == idx[1], 2 == idx[3] (because 1 appears twice in sequence, program
    should always assume 1 is index 1, not 2)

    Args:
        value (int): The number to be validated

    Returns:
        int: The index of the fibonacci number, else 0

    Raises:
        TypeError : Invalid type for input
        ValueError: Value out of possible range
    """
    pass


def next_fibonacci(value: int) -> int:
    """Calculates the next fibonacci number after value

    Calculates the next fibonacci number after value, in case value is a
    fibonacci number, still returns the one following it

    Args:
        value (int): The number to calculate against

    Returns:
        int: The fibonacci number after value

    Raises:
        TypeError: Non-int argument
        ValueError: Value < 0
    """
    pass

if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print(exc)
