#!/usr/bin/python3
"""Module to write an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """Function that writes an Object to text file, using JSON rep"""

    with open(filename, 'w', encoding='utf-8') as f:
        return json.dump(my_obj, f)
