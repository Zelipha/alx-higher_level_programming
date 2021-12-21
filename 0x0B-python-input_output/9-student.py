#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """Represents the class"""

    def __init__(self, first_name, last_name, age):
        """Initializes the data of the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dict representation of a Student instance"""
        return self.__dict__
