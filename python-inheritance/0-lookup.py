#!/usr/bin/python3
"""Module for lookup function."""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
        obj: The object to look up.

    Returns:
        list: A list of available attributes and methods.
    """
    return dir(obj)
