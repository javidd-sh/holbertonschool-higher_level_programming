#!/usr/bin/python3
"""Module that defines a function to print a square with '#'."""


def print_square(size=None):
    """
    Prints a square of size `size` using the character '#'.

    Args:
        size (int): Size length of the square

    Raises:
        TypeError: If size is not an integer or is missing
        ValueError: If size is less than 0
    """

    # Handle missing argument or wrong type
    if size is None or not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Handle negative values
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for _ in range(size):
        print("#" * size)
