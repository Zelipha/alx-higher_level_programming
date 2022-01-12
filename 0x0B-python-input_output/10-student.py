#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """Represents the class"""

    def __init__(self, first_name, last_name, age):
        """Initializes the data of the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dict representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            new_list = []
            for i in attrs:
                if i in self.__dict__:
                    new_list.append(i)
            return {x: self.__dict__[x] for x in new_list}
