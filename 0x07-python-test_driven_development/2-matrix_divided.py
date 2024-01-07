#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
    - matrix: A list of lists of integers or floats.
    - div: A number (integer or float) to divide the elements of the matrix.

    Raises:
    - TypeError: If the matrix is not a list of lists of integers or floats,
                 if each row of the matrix is not of the same size, or
                 if div is not a number (integer or float).
    - ZeroDivisionError: If div is equal to 0.

    Returns:
    - A new matrix with all elements divided by div and rounded to 2 decimal places.
    """

    # Validate if matrix is a list of lists of integers or floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) \
            or not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate if each row of the matrix has the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Validate if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide all elements of the matrix by div, round to 2 decimal places
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix
