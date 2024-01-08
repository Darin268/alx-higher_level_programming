#!/usr/bin/python3
"""Module to define a Square class."""


class BaseGeometry:
    """Class representing a base geometry."""

    def area(self):
        """Method to calculate the area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method to validate 'value' parameter."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Class representing a rectangle."""

    def __init__(self, width, height):
        """Initialize a rectangle instance."""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Method to compute the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description."""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """Class representing a square."""

    def __init__(self, size):
        """Initialize a square instance."""
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def __str__(self):
        """Return the square description."""
        return f"[Square] {self.__size}/{self.__size}"

