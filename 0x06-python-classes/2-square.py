#!/usr/bin/python3
"""Defines a Square Class"""


class Square:
    def __init__(self, size=0):
        """Initialize a square

        Args:
            size (int, optional): Size of the square. Defaults to 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
