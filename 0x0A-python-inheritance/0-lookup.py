#!usr/bin/python3
"""Module to return list of available attributes and methods"""


def lookup(obj):
    """Function that returns the list of available attributes
       and methods of an object.

       Args (obj): list
    """

    obj = []
    return dir(obj)
