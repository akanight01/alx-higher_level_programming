#!/usr/bin/python3
<<<<<<< HEAD
"""class Student that defines a student by:
Public instance attributes:
first_name
last_name
age
"""


class Student:
    """class Student"""

    def __init__(self, first_name, last_name, age):
=======
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
>>>>>>> 0f9335aeefad229f6daf32095d498cf8bbd11781
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
<<<<<<< HEAD
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for item in attrs:
                if hasattr(self, item):
                    new_dict[item] = getattr(self, item)
            return new_dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
=======
        """Get a dictionary representation of the Student.
        If attrs is a list of strings, represents only those attributes
        included in the list.
        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student.
        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
>>>>>>> 0f9335aeefad229f6daf32095d498cf8bbd11781
