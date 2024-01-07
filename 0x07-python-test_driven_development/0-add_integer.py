#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """
    Adds two integers or floats.

    Args:
    - a: An integer or float.
    - b: An integer or float (default is 98).

    Raises:
    - TypeError: If `a` or `b` is not an integer or float.

    Returns:
    - An integer: the addition of `a` and `b`.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    a = int(a)
    b = int(b)
    return a + b
