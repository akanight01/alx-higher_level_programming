#!/usr/bin/python3
<<<<<<< HEAD
"""
The module returns an object (Python data structure)
represented by a JSON string:
Using: def from_json_string(my_str):
"""

=======
# 6-from_json_string.py
"""Defines a JSON-to-object function."""
>>>>>>> 0f9335aeefad229f6daf32095d498cf8bbd11781
import json


def from_json_string(my_str):
<<<<<<< HEAD
    """ The method  returns an object (Python data structure)
    represented by a JSON string:
    Args:
       my_str: the string
    """
=======
    """Return the Python object representation of a JSON string."""
>>>>>>> 0f9335aeefad229f6daf32095d498cf8bbd11781
    return json.loads(my_str)
