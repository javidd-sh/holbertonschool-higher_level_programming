#!/usr/bin/env python3
"""Module for CountedIterator class."""


class CountedIterator:
    """An iterator that keeps track of the number of items iterated."""

    def __init__(self, iterable):
        """Initialize a new CountedIterator.

        Args:
            iterable: The iterable to iterate over.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """Return the number of items iterated so far.

        Returns:
            int: The number of items iterated.
        """
        return self.count

    def __next__(self):
        """Fetch the next item and increment the counter.

        Returns:
            The next item in the iterator.

        Raises:
            StopIteration: If there are no more items to iterate.
        """
        item = next(self.iterator)
        self.count += 1
        return item
