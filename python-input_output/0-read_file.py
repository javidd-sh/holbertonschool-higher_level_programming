#!/usr/bin/python3
"""Module for read_file function."""


def read_file(filename=""):
    """Read a text file and print its contents to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
