#!/usr/bin/python3
"""Defines a class Base"""
import json


class Base:
    """Represents the base with a private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the base"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method that returns the JSON string representation
            of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method that writes the JSON string representation of
            list_objs to a file
        """
        file_name = "{}.json".format(cls.__name__)
        with open(file_name, 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                new_list = []
                for i in list_objs:
                    new_list.append(i.to_dictionary())
                f.write(Base.to_json_string(new_list))
