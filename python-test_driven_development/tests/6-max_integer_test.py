#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test class for max_integer function"""

    def test_empty_list(self):
        """Test empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test list with one element"""
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        """Test list with positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unsorted_list(self):
        """Test unsorted list"""
        self.assertEqual(max_integer([3, 1, 4, 2]), 4)

    def test_negative_numbers(self):
        """Test list with negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test list with mixed positive and negative"""
        self.assertEqual(max_integer([-10, 5, 3, -1]), 5)

    def test_duplicates(self):
        """Test list with duplicate values"""
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_max_at_beginning(self):
        """Max value at beginning"""
        self.assertEqual(max_integer([9, 1, 2, 3]), 9)

    def test_max_at_end(self):
        """Max value at end"""
        self.assertEqual(max_integer([1, 2, 3, 9]), 9)

    def test_float_values(self):
        """Test list with floats"""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)


if __name__ == '__main__':
    unittest.main()
