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

    # Characters that trigger 2 newlines
    separators = ".?:"
    start = 0

    for i, char in enumerate(text):
        if char in separators:
            # Extract the piece and strip spaces
            piece = text[start:i + 1].strip()
            if piece:
                print(piece)
                print()  # extra newline
            start = i + 1

    # Print any remaining text after the last separator
    remaining = text[start:].strip()
    if remaining:
        print(remaining)
