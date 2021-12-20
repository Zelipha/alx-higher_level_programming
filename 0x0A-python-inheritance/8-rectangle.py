#!/usr/bin/python3
"""Define a class BaseGeometry with a public instance method"""


class BaseGeometry:
    """Represents base geometry"""
    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Represents a class Rectangle that inherits from the base class"""
    def __init__(self, width, height):
        """Initializes new rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
