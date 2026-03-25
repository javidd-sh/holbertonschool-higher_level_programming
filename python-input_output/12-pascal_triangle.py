#!/usr/bin/python3
"""Module for pascal_triangle function."""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle of n.

    Args:
        n (int): The number of rows of Pascal's triangle.

    Returns:
        list: A list of lists of integers representing Pascal's triangle,
              or an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
