#!/usr/bin/python3
"""Defines a class Base"""
import json
import os
import csv
import turtle


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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Function that saves list of objects to a CSV file

            Args:
                list_objs (list): list of instances
        """
        file_name = cls.__name__ + ".csv"
        with open(file_name, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=field_names)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Returns the list of instance depending on class from a CSV

               Reads from `<cls.__name__>.csv`
        """
        file_name = cls.__name__ + ".csv"
        try:
            with open(file_name, 'r', newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=field_names)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares"""
        my_turtle = turtle.Turtle()
        my_turtle.shape("turtle")
        my_turtle.pensize(2)

        for rec in list_rectangles:
            if rec.x > 0 and rec.y > 0:
                my_turtle.penup()
                my_turtle.goto(rec.x, rec.y)
                my_turtle.pendown()
            else:
                my_turtle.penup()
                my_turtle.home()
                my_turtle.pendown()
            my_turtle.pencolor("green")
            for i in range(2):
                my_turtle.fd(rec.width)
                my_turtle.rt(90)
                my_turtle.fd(rec.height)
                my_turtle.rt(90)
        for s in list_squares:
            if s.x > 0 and s.y > 0:
                my_turtle.penup()
                my_turtle.goto(s.x, s.y)
                my_turtle.pendown()
            else:
                my_turtle.penup()
                my_turtle.home()
                my_turtle.pendown()
            my_turtle.pencolor("red")
            for i in range(4):
                my_turtle.fd(s.size)
                my_turtle.rt(90)
                my_turtle.ht()
