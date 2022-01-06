#!/usr/bin/python3
"""Defines a class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Represents a class Rectangle that inherits from class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get/set the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the width"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get/set x"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get/set y"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the rectangle area"""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        for emptyline in range(self.__y):
            print('')
        for newline in range(self.__height):
            for space in range(self.__x):
                print(' ', end='')
            for symbol in range(self.__width):
                print("#", end="")
            print('')

    def __str__(self):
        """Overrides __str__ method to return [Rectangle] (<id>)
           <x>/<y> - <width>/<height>
        """
        return (f"[Rectangle] " + f"({self.id}) {self.__x}/"
                + f"{self.y} - {self.__width}/{self.__height}")

    def update(self, *args):
        """Assigns an argument to each attribute

           Args:
                *args (int): The values replacing the attributes
                **kwargs (dict): Key, Value pairs of the attributes
        """
