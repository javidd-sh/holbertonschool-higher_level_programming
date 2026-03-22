#!/usr/bin/python3
"""Module for inherits_from function."""


def inherits_from(obj, a_class):
    """Return True if obj is instance of a class that inherited from a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class,
              False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
