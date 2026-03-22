#!/usr/bin/python3
"""Module for is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or inherits from it.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or a subclass of it,
              False otherwise.
    """
    return isinstance(obj, a_class)
