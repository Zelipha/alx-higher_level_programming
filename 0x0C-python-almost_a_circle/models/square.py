#!/usr/bin/python3
"""Defines a class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a class square that inherits from class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.width = value

    def __str__(self):
        """Overloading __str__ method to return [Square] (<id>)
           <x>/<y> - <size>
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
