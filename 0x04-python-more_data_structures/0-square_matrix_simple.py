#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        return[[i**2 for x in line] for line in matrix]
