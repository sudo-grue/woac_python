"""
Challenge 6 Module

TASK:
Create a class object named 'Sphere'
  - Takes one (1) initializing argument float() or int() representing radius
  - Must have three (3) methods
    - get_surface_area(): returns surface area of sphere
    - get_volume()      : returns volume of sphere
    - get_radius()      : returns the numeric value stored in radius
    - set_radius()      : sets (updates) the radius

  - When radius is updated, resulting surface area and volume will change
  - print() should yield the current radius
  - if set_radius() receives invalid input, do not update values

Note:
  To standardize calculations pi will be calculated to a precision of 2

INFO:
  Surface area formula: 4 * pi * (r ^ 2)
  Volume formula      : (4/3) * pi * (r ^ 3)
"""


def main():
    """
    Student will put all personal test code for challenge in main()
    """
    pass


class Sphere():
    """
    Sphere class containing four (4) methods:
    - get_surface_area()
    - get_volume()
    - get_radius()
    - set_radius()
    """
    pi = 3.14

    def __init__(self, radius):
        pass


if __name__ == '__main__':
    main()
