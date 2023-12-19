#!/usr/bin/python3
"""Square Class

A Square Class

"""


class Square:
    def __init__(self, size=0):
        """Initialize a square

        Args:
            size (int, optional): Size of the square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
