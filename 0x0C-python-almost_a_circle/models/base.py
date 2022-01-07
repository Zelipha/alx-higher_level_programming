#!/usr/bin/python3
"""Defines a class Base"""
import json
import os


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

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            instance = cls(3, 6)
        else:
            instance = cls(3)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        file_name = cls.__name__ + ".json"
        if os.path.exists(file_name) is False:
            return []
        with open(file_name, 'r', encoding='utf-8') as f:
            list_str = f.read()

        list_cls = cls.from_json_string(list_str)
        new_list = []

        for index in range(len(list_cls)):
            new_list.append(cls.create(**list_cls[index]))
        return new_list
