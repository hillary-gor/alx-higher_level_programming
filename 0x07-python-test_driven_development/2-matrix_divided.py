#!/usr/bin/python3
"""
matrix_divided module
This function divides all elements in a matrix

"""


def matrix_divided(matrix, div):
        """Divide all elements in a matrix
    Args:
    param1: matrix type arg of list
    param2: div type int or float
    Return: new matrix with division calculated
    Raise: TypeError, ZeroError
    """


    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)")

    if not matrix or not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("All rows of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("All elements of the matrix must be numbers")
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    return new_matrix
