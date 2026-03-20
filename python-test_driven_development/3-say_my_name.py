#!/usr/bin/python3
"""Module for printing a name."""


def say_my_name(first_name, last_name=""):
    """Prints 'My name is <first_name> <last_name>'.

    first_name and last_name must be strings.
    last_name defaults to empty string.
    Output has no extra spaces and ends with a newline.
    """

    # Type checking
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Strip whitespace from names
    first_name = first_name.strip()
    last_name = last_name.strip()

    # Build full name safely
    full_name = "{} {}".format(first_name, last_name).strip()

    # Print exactly one newline at the end, no extra spaces
    print("My name is {}".format(full_name))
