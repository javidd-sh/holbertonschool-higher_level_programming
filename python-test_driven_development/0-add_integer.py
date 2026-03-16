#!/usr/bin/python3
"""Module that defines add_integer(a, b=98) function."""


def add_integer(a, b=98):
    """Add two integers or floats and return an integer.

    Floats are cast to integers.
    Raises TypeError if a or b is not int or float (bool not allowed).
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
