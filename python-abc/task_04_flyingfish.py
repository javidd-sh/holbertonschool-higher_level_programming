#!/usr/bin/env python3
"""Module for Fish, Bird, and FlyingFish classes."""


class Fish:
    """Defines a fish."""

    def swim(self):
        """Print a swimming message."""
        print("The fish is swimming")

    def habitat(self):
        """Print the habitat of a fish."""
        print("The fish lives in water")


class Bird:
    """Defines a bird."""

    def fly(self):
        """Print a flying message."""
        print("The bird is flying")

    def habitat(self):
        """Print the habitat of a bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Defines a flying fish that inherits from both Fish and Bird."""

    def swim(self):
        """Print a swimming message for the flying fish."""
        print("The flying fish is swimming!")

    def fly(self):
        """Print a flying message for the flying fish."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Print the habitat of the flying fish."""
        print("The flying fish lives both in water and the sky!")
