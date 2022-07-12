#!/usr/bin/env python3
"""
Testing suite for Challenge 7

Executed with `python3 -m unittest discover -s test -v` from challenge_7 dir
and testing code in ./test/
"""
from shutil import which
import unittest


from challenge_7.challenge_7 import next_fibonacci, which_fibonacci


class test_next_fib(unittest.TestCase):
    """
    Tests calculating the next fibonacci number after provided
    """
    def test_val_lt_zero_next(self):
        """Tests if input val less than 0 for next_fibonacci()
        """
        with self.assertRaises(ValueError):
            next_fibonacci(-55)

    def test_val_ne_int_next(self):
        """Tests if input not an integer
        """
        with self.assertRaises(TypeError):
            next_fibonacci('a')

    def test_val_inherited_int(self):
        """Tests if int inherited types allowed
        """
        with self.assertRaises(TypeError):
            next_fibonacci(True)

    def test_valid_input(self):
        """Validates valid input
        """
        self.assertEqual(next_fibonacci(0), 1)
        self.assertEqual(next_fibonacci(1), 2)
        self.assertEqual(next_fibonacci(2), 3)
        self.assertEqual(next_fibonacci(3), 5)
        self.assertEqual(next_fibonacci(4), 5)
        self.assertEqual(next_fibonacci(5), 8)
        self.assertEqual(next_fibonacci(956722026042), 1548008755920)

class test_which_fib(unittest.TestCase):
    """Tests calculating if a number is a fibonacci, and if so, which one
    """
    def test_val_lt_zero_next(self):
        """Tests if input val less than 0 for next_fibonacci()
        """
        with self.assertRaises(ValueError):
            which_fibonacci(-55)

    def test_val_ne_int_next(self):
        """Tests if input not an integer
        """
        with self.assertRaises(TypeError):
            which_fibonacci('a')

    def test_val_inherited_int(self):
        """Tests if int inherited types allowed
        """
        with self.assertRaises(TypeError):
            which_fibonacci(True)

    def test_valid_input(self):
        """Validates valid input
        """
        self.assertEqual(which_fibonacci(0), 0)
        self.assertEqual(which_fibonacci(1), 1)
        self.assertEqual(which_fibonacci(2), 3)
        self.assertEqual(which_fibonacci(3), 4)
        self.assertEqual(which_fibonacci(4), 0)
        self.assertEqual(which_fibonacci(5), 5)
        self.assertEqual(which_fibonacci(114059301025943970552219), 112)
        self.assertEqual(which_fibonacci(8670007398507948658051921), 121)


if __name__ == '__main__':
    unittest.main()
