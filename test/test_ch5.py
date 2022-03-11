#!/usr/bin/python3
"""
Testing suite for Challenge 5

Executed with `python3 -m unittest discover -s test -v` from challenge_5 dir
and testing code in ./test/
"""
import unittest


from challenge_5.challenge_5 import factorial, print_expanded


class test_factorial(unittest.TestCase):
    """
    Tests factorial function in Challenge 5
    """
    def test_fact_lt_one(self):
        """
        Tests response for vaules less than one (1)
        """
        self.assertEqual(factorial(0), 0)
        self.assertEqual(factorial(-1), 0)

    def test_fact_not_int(self):
        """
        Tests handling of non-int input
        """
        self.assertEqual(factorial("a"), 0)
        self.assertEqual(factorial(5.0), 0)

    def test_fact_normal_value(self):
        """
        Tests postive ints for expected output
        """
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(7), 5040)
        self.assertEqual(factorial(8), 40320)
        self.assertEqual(factorial(9), 362880)
        self.assertEqual(factorial(10), 3628800)

class test_expanded(unittest.TestCase):
    """
    Tests print_expanded function in Challenge 5
    """
    def test_expanded_lt_one(self):
        """
        Tests response for values less than one (1)
        """
        self.assertEqual(print_expanded(0), '')
        self.assertEqual(print_expanded(-1), '')

    def test_expanded_not_int(self):
        """
        Tests response for values that are not an int() object
        """
        self.assertEqual(print_expanded("a"), '')
        self.assertEqual(print_expanded(5.0), '')

    def test_expanded_normal(self):
        self.assertEqual(print_expanded(1), '1 = 1')
        self.assertEqual(print_expanded(2), '2x1 = 2')
        self.assertEqual(print_expanded(3), '3x2x1 = 6')
        self.assertEqual(print_expanded(4), '4x3x2x1 = 24')


if __name__ == '__main__':
    unittest.main()
