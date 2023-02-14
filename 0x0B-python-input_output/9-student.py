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

    def to_json(self):
<<<<<<< HEAD
        """retrieves a dictionary representation of a Student instance"""
=======
        """Get a dictionary representation of the Student."""
>>>>>>> 0f9335aeefad229f6daf32095d498cf8bbd11781
        return self.__dict__
