#!/usr/bin/python3
"""Module for printing text with custom indentation."""


def text_indentation(text):
    """Print text with 2 newlines after '.', '?', or ':'. Strip lines.

    Args:
        text (str): input text

    Raises:
        TypeError: if text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ".?:"
    start = 0
    length = len(text)

    for i, char in enumerate(text):
        if char in separators:
            # Extract piece from start to current char (inclusive)
            piece = text[start:i + 1].strip()
            if piece:  # print only non-empty pieces
                print(piece)
                print()  # second newline
            start = i + 1

    # Print any remaining text after the last separator
    remaining = text[start:].strip()
    if remaining:
        print(remaining)
