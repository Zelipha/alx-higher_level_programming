#!/usr/bin/python3
"""Defines a class and inherited class-checking function"""


def is_kind_of_class(obj, a_class):
    """Checks if the object is an instance of a class that inherited from,
       the specified class.
    """
    return isinstance(obj, a_class)
