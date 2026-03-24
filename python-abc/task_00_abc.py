#!/usr/bin/env python3
"""Module for Animal abstract class and its subclasses."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Return the sound of the animal."""
        pass


class Dog(Animal):
    """Defines a dog that inherits from Animal."""

    def sound(self):
        """Return the sound of a dog.

        Returns:
            str: The string 'Bark'.
        """
        return "Bark"


class Cat(Animal):
    """Defines a cat that inherits from Animal."""

    def sound(self):
        """Return the sound of a cat.

        Returns:
            str: The string 'Meow'.
        """
        return "Meow"
