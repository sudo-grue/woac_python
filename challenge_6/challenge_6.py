#!/usr/bin/python3
"""
Challenge 6 Module

TASK:
Create a class object named 'Sphere'
  - Takes one (1) initializing argument float() or int() representing radius
  - radius will be stored as a private __radius instance attribute
  - Must have following methods
    - "secret" method   : prevents additional members (HINT: class attribute)

    - __init__()        : used when "creation" of object happens

    - radius()          : use @property decorator as getter
    - radius()          : use @radius.setter decorator as setter

    - get_surface_area(): returns surface area of sphere
    - get_volume()      : returns volume of sphere

    - __str__()         : used by print() to override default
    - __repr__()        : effectively a "How would you recreate this object?"

    - __lt__()          : Sphere <  (int, float, Sphere) -> bool
    - __le__()          : Sphere <= (int, float, Sphere) -> bool
    - __eq__()          : Sphere == (int, float, Sphere) -> bool
    - __ne__()          : Sphere != (int, float, Sphere) -> bool
    - __gt__()          : Sphere >  (int, float, Sphere) -> bool
    - __ge__()          : Sphere >= (int, float, Sphere) -> bool

    - __add__()         : Sphere + (int, float, Sphere) -> (int, float)
    - __sub__()         : Sphere - (int, float, Sphere) -> (int, float)
    - __radd__()        : (int, float) + Sphere         -> (int, float)
    - __rsub__()        : (int, float) - Sphere         -> (int, float)

  - When radius is updated, resulting surface area and volume will change
  - print() should yield the current radius
  - object.radius will not change value on invalid input (no error raised)
  - On creation, raise ValueError if invalid input

Note:
  To standardize calculations pi will be calculated to a precision of 2

  WARNING: Some methods may "wrongly" succeed until "secret" method implemented

  See https://docs.python.org/3/reference/datamodel.html#basic-customization
    for details about all dunder methods (including "secret")
"""
from typing import Union


def main():
    """
    Student will put all personal test code for challenge in main()
    execute with `python3 challenge_6.py`
    """
    pass


class Sphere():
    pi = 3.14 # class attribute, if changed, changes for all existing objects
    pass

if __name__ == '__main__':
    main()
