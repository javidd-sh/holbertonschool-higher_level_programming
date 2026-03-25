#!/usr/bin/env python3
"""Module for CustomObject class with pickle serialization."""
import pickle


class CustomObject:
    """A custom class that supports pickle serialization."""

    def __init__(self, name, age, is_student):
        """Initialize a new CustomObject.

        Args:
            name (str): The name of the object.
            age (int): The age of the object.
            is_student (bool): Whether the object is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print out the object's attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the current instance and save it to a file.

        Args:
            filename (str): The filename to save the serialized object to.

        Returns:
            None: If an exception occurs.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and return an instance of CustomObject from a file.

        Args:
            filename (str): The filename to load the object from.

        Returns:
            CustomObject: The deserialized object, or None if an error occurs.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
