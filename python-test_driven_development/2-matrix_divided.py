#!/usr/bin/python3
"""Module that defines a function to divide all elements of a matrix."""


def matrix_divided(matrix=None, div=None):
    """
    Divides all elements of a matrix by div, rounded to 2 decimals.

    Args:
        matrix (list of lists): Matrix of integers/floats
        div (int or float): Number to divide by

    Returns:
        list of lists: New matrix

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats
        TypeError: If rows are not same size
        TypeError: If div is not a number
        ZeroDivisionError: If div is 0
    """

    if matrix is None:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if div is None:
        raise TypeError("div must be a number")

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    for row in matrix:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if div == float('inf') or div == float('-inf'):
        return [[0.0 for _ in row] for row in matrix]

    new_matrix = []
    for row in matrix:
        new_row = [round(num / div, 2) for num in row]
        new_matrix.append(new_row)

    return new_matrix
