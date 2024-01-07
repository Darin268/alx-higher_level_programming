#!/usr/bin/python3
"""Defines a square-printing function."""


def print_square(size):
    """
    Prints a square of '#' characters with the given size length.

    Args:
    - size: An integer representing the size length of the square.

    Raises:
    - TypeError: If size is not an integer or if size is a float less than 0.
    - ValueError: If size is less than 0.

    Returns:
    - None. Prints the square pattern.
    """

    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is less than 0 or a float less than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Create and print the square pattern
    for i in range(size):
        print("#" * size)
