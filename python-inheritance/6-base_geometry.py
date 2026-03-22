#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """Defines a base geometry class with area method."""

    def area(self):
        """Calculate the area of the geometry.

        Raises:
            Exception: Always raises with message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
