#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the current rectangle.
         Args:
            height (int): height of the rectangle
            width (int): width of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return (0)

        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        new_str = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    new_str += "#"
                new_str += "\n"
            return new_str[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
