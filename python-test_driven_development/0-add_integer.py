#!/usr/bin/python3
"""Module for adding two integers."""


def add_integer(a, b=98):
    """Adds two integers and returns the result.

    a and b must be integers or floats.
    Floats are cast to integers before addition.
    """

    # Type checking
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # NaN check (NaN is not equal to itself)
    if a != a:
        raise TypeError("a must be an integer")
    if b != b:
        raise TypeError("b must be an integer")

    # Infinity check
    if a == float("inf") or a == float("-inf"):
        raise TypeError("a must be an integer")
    if b == float("inf") or b == float("-inf"):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
