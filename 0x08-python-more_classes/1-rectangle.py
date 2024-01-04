#!/usr/bin/python3
"""

Module with a Rectangle

"""


class Rectangle:
    """
    Class Rectangle defines a rectangle.

    Attributes:
        __width (int): Private instance attribute for width.
        __height (int): Private instance attribute for height.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): Optional, defaults to 0. Width of the rectangle.
            height (int): Optional, defaults to 0. Height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for width attribute.

        Returns:
            int: Width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width attribute.

        Args:
            value (int): Value to set as the width.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for height attribute.

        Returns:
            int: Height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height attribute.

        Args:
            value (int): Value to set as the height.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

