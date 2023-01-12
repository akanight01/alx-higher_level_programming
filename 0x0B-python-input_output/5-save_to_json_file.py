#!/usr/bin/python3
<<<<<<< HEAD
"""
The module that writes an Object to a text file,
using a JSON representation:
Using: def save_to_json_file(my_obj, filename):
"""

=======
"""Defines a JSON file-writing function."""
>>>>>>> 0f9335aeefad229f6daf32095d498cf8bbd11781
import json


def save_to_json_file(my_obj, filename):
<<<<<<< HEAD
    """ The method that writes an Object to a text file,
    using a JSON representation:
    Args:
         my_obj: an object
         filename: text file name
    """
    with open(filename, 'w', encoding='utf-8') as f:
=======
    """Write an object to a text file using JSON representation."""
    with open(filename, "w") as f:
>>>>>>> 0f9335aeefad229f6daf32095d498cf8bbd11781
        json.dump(my_obj, f)
