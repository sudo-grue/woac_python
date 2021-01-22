"""
Testing suite for Challenge 6 

Executed with `python3 -m unittest discover -s test -v` from root dir
which targets ./test/ directory
"""
import unittest


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
        self.assertEqual(self.sphere.get_radius(), 5)

    def test_set_radius(self):
        """
        Tests if setter updates radius
        """
        self.sphere.set_radius(4)
        self.assertEqual(self.sphere.get_radius(), 4)

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

    def test_invalid_input(self):
        self.sphere.set_radius('a')
        self.assertEqual(self.sphere.get_radius(), 5)

        self.sphere.set_radius(-1)
        self.assertEqual(self.sphere.get_radius(), 5)

        self.sphere.set_radius(float("nan"))
        self.assertEqual(self.sphere.get_radius(), 5)

        self.sphere.set_radius(None)
        self.assertEqual(self.sphere.get_radius(), 5)

    def test_valid_input(self):
        test_sphere = Sphere(5.5)
        self.assertIsNotNone(test_sphere)

        test_sphere = Sphere(0.000001)
        self.assertIsNotNone(test_sphere)


if __name__ == '__main__':
    unittest.main()
