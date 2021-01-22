"""
Challenge 6 Module

TASK:
Create a class object named 'Sphere'
  - Takes one (1) initializing argument float() or int() representing radius
  - Must have three (3) methods
    - get_surface_area() which returns surface area of sphere
    - get_volume() which returns volume of sphere
    - set_radius() which changes the radius already set
  - When radius is updated, resulting surface area and volume will change
  - On invalid initialization input, generate a None object
  - print() should yield the current radius

Note:
  To standardize calculations pi will be calculated to a precision of 2

INFO:
  Surface area formula: 4 * pi * r ^ 2
  Volume formula      : 4/3 * pi * r ^ 3
"""


def main():
    """
    Student will put all personal test code for challenge in main()
    """
    pass


class Sphere():
    """
    Sphere class containing three (3) methods:
    - get_surface_area()
    - get_volume()
    - set_radius()
    """
    def __init__(self, radius):
        self.pi = 3.14
        pass


if __name__ == '__main__':
    main()
