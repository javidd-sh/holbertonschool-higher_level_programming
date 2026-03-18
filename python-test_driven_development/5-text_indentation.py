#!/usr/bin/python3
"""Module that defines a function to print text with proper indentation."""


def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?', or ':'.

    Args:
        text (str): Input text

    Raises:
        TypeError: If text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Characters after which to insert 2 newlines
    split_chars = ".?:"

    start = 0
    length = len(text)

    while start < length:
        # Find the nearest occurrence of any split character
        index = length  # default: end of text
        char_found = ""
        for c in split_chars:
            i = text.find(c, start)
            if i != -1 and i < index:
                index = i
                char_found = c

        if index == length:
            # No more split chars, print remaining text
            line = text[start:].strip()
            if line:
                print(line)
            break

        # Print up to and including the split character
        line = text[start:index + 1].strip()
        print(line)
        print()  # second newline
        start = index + 1
