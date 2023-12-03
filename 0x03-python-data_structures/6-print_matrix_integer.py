#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for elem in matrix:
        if len(elem) == 0:
            print()
        for i in range(len(elem)):
            print("{:d}".format(elem[i]),
                  end="\n" if i is len(elem) - 1 else " ")
