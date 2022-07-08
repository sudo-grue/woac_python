#!/usr/bin/python3
"""
Challenge 6 Module

TASK:
Create a class object named 'Sphere'
  - Takes one (1) initializing argument float() or int() representing radius
  - radius will be stored as a private _radius instance attribute
  - print() should yield the current radius
  - On creation, raise appropriate error on invalid input
  - radius getter/setter raise appropriate error on invalid input
  - Sphere object allows all comparision operators against int/float/Sphere

Note:
  To standardize calculations pi will be calculated to a precision of 2

  WARNING: Some tests "wrongly" succeed until "secret" attribute implemented

  See https://docs.python.org/3/reference/datamodel.html#basic-customization
    for details about dunder methods including "secret test"
"""
from __future__ import annotations
from typing import Union


def main() -> int:
    """
    Student will put all personal test code for challenge in main()
    execute with `python3 challenge_6.py`
    """
    pass

class Sphere():
    """A sphere object with capability of providing specific space information

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
    def __init__(self, radius: int) -> None:
        pass

    def radius(self) -> Union[int, float]:
        pass

    def radius(self, radius: Union[int, float]) -> None:
        pass

    def get_surface_area(self) -> Union[int, float]:
        pass

    def get_volume(self) -> Union[int, float]:
        pass

    def __str__(self) -> str:
        pass

    def __repr__(self) -> str:
        pass

    def __eq__(self, other: object) -> bool:
        pass

    def __ne__(self, other: object) -> bool:
        pass

    def __lt__(self, other: Union[int, float, Sphere]) -> bool:
        pass

    def __le__(self, other: Union[int, float, Sphere]) -> bool:
        pass

    def __gt__(self, other: Union[int, float, Sphere]) -> bool:
        pass

    def __ge__(self, other: Union[int, float, Sphere]) -> bool:
        pass

    def __add__(self, other: Union[int, float, Sphere]) -> Union[int, float]:
        pass

    def __sub__(self, other: Union[int, float, Sphere]) -> Union[int, float]:
        pass

    def __radd__(self, other: Union[int, float, Sphere]) -> Union[int, float]:
        pass

    def __rsub__(self, other: Union[int, float, Sphere]) -> Union[int, float]:
        pass


if __name__ == '__main__':
    main()
