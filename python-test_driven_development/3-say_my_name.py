#!/usr/bin/python3
"""Module for say_my_name function."""


def say_my_name(first_name, last_name=""):
    """Print 'My name is <first_name> <last_name>'.

    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print. Defaults to "".

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
