#!/usr/bin/python3
"""Module for MyList class."""


class MyList(list):
    """A class that inherits from list with a print_sorted method."""

    def print_sorted(self):
        """Print the list in ascending sorted order.

        The original list is not modified.
        """
        print(sorted(self))
