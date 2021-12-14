#!/usr/bin/python3
"""Module to add 2 integers"""


def add_integer(a, b=98):
    """Function that adds 2 integers and returns an int
       Args: a and b
         If not integers or floats raise TypeError
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
