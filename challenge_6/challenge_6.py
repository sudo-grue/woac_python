#!/usr/bin/python3
"""
Challenge 6 Module

TASK:
Create a class object named 'Sphere'
  - Takes one (1) initializing argument float() or int() representing radius
  - radius will be stored as a private _radius instance attribute
  - print() should yield the current radius
  - On creation, raise appropriate error on invalid input
  - radius getter.setter raise appropriate error on invalid input
  - Sphere object allows all comparision operators against int/float/Sphere

Note:
  To standardize calculations pi will be calculated to a precision of 2

  WARNING: Some tests may "wrongly" succeed until "secret" method implemented

  See https://docs.python.org/3/reference/datamodel.html#basic-customization
    for details about dunder methods including "secret test"
"""
from typing import Union


def main():
    """
    Student will put all personal test code for challenge in main()
    execute with `python3 challenge_6.py`
    """
    pass


class Sphere():
    """A sphere object with capability of providing specific math information

    Creates a sphere object with radius of Union[int, float] and calculates
    surface area and volume based on that radius.

    Attributes:
        pi     : A class attribute of float(3.14)
        radius : A positive Union[int, float] representing radius

    Methods:
        get_surface_area() : Calculates surface area of sphere
        get_volume()       : Calculates volume of sphere

    Raises:
        AttributeError     : Invalid attribute accessed
        TypeError          : Radius update was not int or float
        TypeError          : Comparison operator against invalid type
        ValueError         : Value is not in possible range
    """
    pi = 3.14 # class attribute, if changed, changes for all existing objects
    pass

if __name__ == '__main__':
    main()
