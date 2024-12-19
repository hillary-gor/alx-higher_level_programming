#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        result = max_integer(ordered)
        self.assertEqual(result, 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 2, 4, 3]
        result = max_integer(unordered)
        self.assertEqual(result, 4)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [4, 3, 2, 1]
        result = max_integer(max_at_beginning)
        self.assertEqual(result, 4)

    def test_empty_list(self):
        """Test with an empty list: should return None."""
        empty = []
        result = max_integer(empty)
        self.assertEqual(result, None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [7]
        result = max_integer(one_element)
        self.assertEqual(result, 7)

    def test_floats(self):
        """Test with a list of floats: should return the max."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        result = max_integer(floats)
        self.assertEqual(result, 15.2)

    def test_ints_and_floats(self):
        """Test with a list of ints and floats: should return the max."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        result = max_integer(ints_and_floats)
        self.assertEqual(result, 15.5)

    def test_string(self):
        """Test with a string."""
        string = "Brennan"
        result = max_integer(string)
        self.assertEqual(result, 'r')

    def test_list_of_strings(self):
        """Test with a list of strings: should return the last string."""
        strings = ["Brennan", "is", "my", "name"]
        result = max_integer(strings)
        self.assertEqual(result, "name")

    def test_empty_string(self):
        """Test an empty string."""
        empty_string = ""
        result = max_integer(empty_string)
        self.assertEqual(result, None)

    def test_neagtive(self):
        """Test with a list of negative value: should return the max"""
        neg_nums = [-2, -6, -1]
        result = max_integer(neg_nums)
        self.assertEqual(result, -1)

    def test_identical(self):
        """Test with a list of identical values: should return the value"""
        identical_nums = [3, 3, 3, 3, 3, 3]
        result = max_integer(identical_nums)
        self.assertEqual(result, 3)

    def test_identical(self):
        """Test with a list of identical values: should return the value"""
        identical_nums = [3, 3, 3, 3, 3, 3]
        result = max_integer(identical_nums)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
