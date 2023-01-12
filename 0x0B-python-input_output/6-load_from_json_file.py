#!/usr/bin/python3
<<<<<<< HEAD
"""
The module that creates an Object from a “JSON file”:
Using: def load_from_json_file(filename):
"""

=======
"""Defines a JSON file-reading function."""
>>>>>>> 0f9335aeefad229f6daf32095d498cf8bbd11781
import json


def load_from_json_file(filename):
<<<<<<< HEAD
    """ the method that creates an Object from a JSON file
    Args:
        filename: textfile name
    """
    with open(filename, 'r', encoding="utf-8") as f:
=======
    """Create a Python object from a JSON file."""
    with open(filename) as f:
>>>>>>> 0f9335aeefad229f6daf32095d498cf8bbd11781
        return json.load(f)
