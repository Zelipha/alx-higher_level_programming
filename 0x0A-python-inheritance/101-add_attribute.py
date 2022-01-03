#!/usr/bin/python3
"""Module that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, attr, value):
    """Add new attribute to an object if possible

       Raises:
           TypeError: if the object can’t have new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
