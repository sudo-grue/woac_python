"""
Challenge 6 Module

TASK:
Create a class object named 'Sphere'
  - Takes one (1) initializing argument float() or int() representing radius
  - radius will be stored as a private ('__') instance attribute
  - Must have five (5) methods
    - get_surface_area() : returns surface area of sphere
    - get_volume()       : returns volume of sphere
    - radius()           : use @property decorator as getter
    - radius()           : use @radius.setter decorator as setter
    - __str__()          : used by print() to override default

  - When radius is updated, resulting surface area and volume will change
  - print() should yield the current radius
  - if set_radius() receives invalid input, do not update values
  - On creation, raise ValueError if invalid input

Note:
  To standardize calculations pi will be calculated to a precision of 2
"""
from typing import Union


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
    - radius() getter
    - radius() setter
    - __str__()
    """
    pi = 3.14

    def __init__(self, radius: Union[int, float]):
        self.__radius = radius
        pass

    @property
    def radius(self):
        pass

    @radius.setter
    def radius(self, radius):
        pass

    def get_surface_area(self):
        pass

    def get_volume(self):
        pass

    def __str__(self):
        pass


if __name__ == '__main__':
    main()
