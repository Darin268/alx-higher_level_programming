#!/usr/bin/python3
"""Defines a name-printing function."""


def say_my_name(first_name, last_name=""):
    """
    Prints the name in the format "My name is <first name> <last name>"

    Args:
    - first_name: A string representing the first name.
    - last_name: A string representing the last name (default is an empty string).

    Raises:
    - TypeError: If first_name or last_name is not a string.

    Returns:
    - None. Prints the formatted name.
    """

    # Validate if first_name and last_name are strings
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the formatted name
    if last_name != "":
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
