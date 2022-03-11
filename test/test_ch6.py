"""
Testing suite for Challenge 6 

Executed with `python3 -m unittest discover -s test -v` from root dir
which targets ./test/ directory
"""
import unittest
from math import isnan

from challenge_6.challenge_6 import Sphere


class test_challenge6(unittest.TestCase):
    """
    Tests functions created in Challenge 6
    """
    def setUp(self):
        self.sphere = Sphere(5)

    def test_check_pi(self):
        """
        Tests if student modified pi
        """
        self.assertEqual(self.sphere.pi, 3.14)

    def test_get_radius(self):
        """
        Tests if initialize value handled correctly
        """
        self.assertEqual(self.sphere.radius, 5)

    def test_set_radius(self):
        """
        Tests if setter updates radius
        """
        self.sphere.radius = 4
        self.assertEqual(self.sphere.radius, 4)

    def test_get_area(self):
        """
        Tests if surface area calculated correctly 4 * pi * (r ^ 2)
        using the get_surface_area() method
        """
        self.assertAlmostEqual(self.sphere.get_surface_area(), 314.0,
                               places=2)

    def test_print(self):
        """
        Tests if interface for print() created
        """
        self.assertEqual(self.sphere.__str__(), '5')

    def test_get_volume(self):
        """
        Tests the volume calculation
        """
        self.assertAlmostEqual(self.sphere.get_volume(), 523.33, places=2)

    def test_invalid_edit(self):
        """
        Tests invalid set method confirms input before changes
        """
        self.sphere.radius = 'a'
        self.assertEqual(self.sphere.radius, 5)

        self.sphere.radius = -1
        self.assertEqual(self.sphere.radius, 5)

        self.sphere.radius = float("nan")
        self.assertEqual(self.sphere.radius, 5)

        self.sphere.radius = None
        self.assertEqual(self.sphere.radius, 5)

    def test_valid_input(self):
        """
        Tests more obscure inputs are valid
        """
        test_sphere = Sphere(5.5)
        self.assertIsNotNone(test_sphere)

        test_sphere = Sphere(0.000001)
        self.assertIsNotNone(test_sphere)

    def test_invalid_creation(self):
        """
        Tests that no object created on invalid input
        """
        with self.assertRaises(ValueError):
            Sphere(None)
        with self.assertRaises(ValueError):
            Sphere(float("nan"))
        with self.assertRaises(ValueError):
            Sphere(-1)

    def test_string(self):
        """
        Tests print/str return the string interpretation of radius
        """
        self.assertTrue("5" == str(self.sphere))
        test_sphere = Sphere(3)
        self.assertTrue("3" == str(test_sphere))

    def test_repr(self):
        """
        Tests repr returns string to recreate object
        """
        self.assertTrue("Sphere(5)" == repr(self.sphere))
        test_sphere = Sphere(3)
        self.assertTrue("Sphere(3)" == repr(test_sphere))

    def test_secret(self):
        """
        Tests discovery learning task
        """
        with self.assertRaises(AttributeError):
            self.sphere.aslkdgjalksdgjaslk = 5

    def test_less_than(self):
        """
        Tests '<' of Sphere to (Sphere, int, float)
        """
        other_sphere = Sphere(6)
        self.assertTrue(self.sphere < other_sphere)
        self.assertFalse(other_sphere < self.sphere)
        self.assertTrue(self.sphere < 6)
        self.assertFalse(self.sphere < 4)
        self.assertTrue(self.sphere < 5.5)
        self.assertFalse(self.sphere < 3.3)
        self.assertFalse(self.sphere < float("nan"))
        with self.assertRaises(TypeError):
            self.sphere < 'a'
        with self.assertRaises(TypeError):
            'a' < self.sphere

    def test_equal(self):
        """
        Tests '==' of Sphere to (Sphere, int, float)
        """
        test_sphere = Sphere(5)
        other_sphere = Sphere(6)
        self.assertTrue(self.sphere == test_sphere)
        self.assertFalse(self.sphere == other_sphere)
        self.assertTrue(self.sphere == 5)
        self.assertFalse(self.sphere == 4)
        self.assertTrue(self.sphere == 5.0)
        self.assertFalse(self.sphere == 4.4)
        self.assertFalse(self.sphere == float("nan"))
        self.assertFalse(self.sphere == 'a')
        self.assertFalse(self.sphere == None)

    def test_less_equal(self):
        """
        Tests '<=' of Sphere to (Sphere, int, float)
        """
        test_sphere = Sphere(5)
        self.assertTrue(self.sphere <= test_sphere)
        test_sphere.radius = 4
        self.assertFalse(self.sphere <= test_sphere)
        self.assertTrue(test_sphere <= self.sphere)

        self.assertTrue(self.sphere <= 5)
        self.assertTrue(self.sphere <= 6)
        self.assertTrue(self.sphere <= 5.0)
        self.assertTrue(self.sphere <= 6.0)

        self.assertFalse(self.sphere <= 3)
        self.assertFalse(self.sphere <= 3.3)
        self.assertFalse(self.sphere <= float("nan"))

        with self.assertRaises(TypeError):
            self.sphere <= None
        with self.assertRaises(TypeError):
            None <= self.sphere
        with self.assertRaises(TypeError):
            self.sphere <= 'a'
        with self.assertRaises(TypeError):
            'a' <= self.sphere
    
    def test_greater(self):
        """
        Tests '>' of Sphere to (Sphere, int, float)
        """
        test_sphere = Sphere(5)
        self.assertFalse(self.sphere > test_sphere)
        test_sphere.radius = 4.5
        self.assertTrue(self.sphere > test_sphere)
        self.assertTrue(self.sphere > 3)
        self.assertTrue(self.sphere > 3.3)

        self.assertFalse(self.sphere > 6)
        self.assertFalse(self.sphere > 6.6)
        self.assertFalse(self.sphere > float("nan"))

        with self.assertRaises(TypeError):
            self.sphere > None
        with self.assertRaises(TypeError):
            None > self.sphere
        with self.assertRaises(TypeError):
            self.sphere > 'a'
        with self.assertRaises(TypeError):
            'a' > self.sphere

    def test_greater_equal(self):
        """
        Tests '>=' of Sphere to (Sphere, int, float)
        """
        test_sphere = Sphere(5)
        self.assertTrue(self.sphere >= test_sphere)
        test_sphere.radius = 4
        self.assertTrue(self.sphere >= test_sphere)
        self.assertFalse(test_sphere >= self.sphere)

        self.assertTrue(self.sphere >= 5)
        self.assertTrue(self.sphere >= 4)
        self.assertTrue(self.sphere >= 5.0)
        self.assertTrue(self.sphere >= 4.0)

        self.assertFalse(self.sphere >= 6)
        self.assertFalse(self.sphere >= 6.3)
        self.assertFalse(self.sphere >= float("nan"))

        with self.assertRaises(TypeError):
            self.sphere >= None
        with self.assertRaises(TypeError):
            None >= self.sphere
        with self.assertRaises(TypeError):
            self.sphere >= 'a'
        with self.assertRaises(TypeError):
            'a' >= self.sphere

    def test_not_equal(self):
        """
        Tests '!=' of Sphere to (Sphere, int, float)
        """
        test_sphere = Sphere(5)
        other_sphere = Sphere(6)
        self.assertFalse(self.sphere != test_sphere)
        self.assertTrue(self.sphere != other_sphere)
        self.assertFalse(self.sphere != 5)
        self.assertTrue(self.sphere != 4)
        self.assertFalse(self.sphere != 5.0)
        self.assertTrue(self.sphere != 4.4)
        self.assertTrue(self.sphere != float("nan"))
        self.assertTrue(self.sphere != 'a')
        self.assertTrue(self.sphere != None)

    def test_add(self):
        """
        Tests '+' of Sphere to (Sphere, int, float)
        """
        test_sphere = Sphere(3)
        self.assertEqual(self.sphere + test_sphere, 8)
        test_sphere.radius = 3.0
        self.assertEqual(self.sphere + test_sphere, 8.0)

        self.assertEqual(self.sphere + 3, 8)
        self.assertEqual(self.sphere + 3.0, 8.0)

        self.assertTrue(isnan(self.sphere + float("nan")))

        with self.assertRaises(TypeError):
            self.sphere + None
        with self.assertRaises(TypeError):
            self.sphere + 'a'

    def test_radd(self):
        """
        Tests '+' of (int, float) to Sphere
        """
        self.assertEqual(3 + self.sphere, 8)

    def test_sub(self):
        """
        Tests '-' of Sphere to (Sphere, int, float)
        """
        test_sphere = Sphere(3)
        self.assertEqual(self.sphere - test_sphere, 2)
        test_sphere.radius = 2.0
        self.assertEqual(self.sphere - test_sphere, 3.0)

        self.assertEqual(self.sphere - 3, 2)
        self.assertEqual(self.sphere - 2.0, 3.0)

        self.assertTrue(isnan(self.sphere - float("nan")))

        with self.assertRaises(TypeError):
            self.sphere - None
        with self.assertRaises(TypeError):
            self.sphere - 'a'

    def test_rsub(self):
        """
        Tests '-' of (int, sphere) to Sphere
        """
        self.assertEqual(8 - self.sphere, 3)


if __name__ == '__main__':
    unittest.main()
