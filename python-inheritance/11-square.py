#!/usr/bin/python3
"""Module for Square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """Return a string description of the square.

        Returns:
            str: The square description in format [Square] size/size.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
