#!/usr/bin/python3
"""Module that returns the dictionary description
   with simple data structure for JSON serialization of an object
   (list, dictionary, string, integer and boolean)
"""


def class_to_json(obj):
    """obj is an instance of a Class"""
    return obj.__dict__
