#!/usr/bin/python3
"""Module for integer addition"""


def add_integer(a, b=98):
    """Adds two integers or floats and returns an integer"""

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")

    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
