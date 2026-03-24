#!/usr/bin/env python3
"""Module for SwimMixin, FlyMixin, and Dragon classes."""


class SwimMixin:
    """Mixin class that provides swimming ability."""

    def swim(self):
        """Print a swimming message."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class that provides flying ability."""

    def fly(self):
        """Print a flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Defines a dragon that can swim and fly."""

    def roar(self):
        """Print a roaring message."""
        print("The dragon roars!")
