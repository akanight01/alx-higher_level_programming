#!/usr/bin/python3
<<<<<<< HEAD
"""-class_to_json.py"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization
    of an object
    """
=======
"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""
>>>>>>> 0f9335aeefad229f6daf32095d498cf8bbd11781
    return obj.__dict__
