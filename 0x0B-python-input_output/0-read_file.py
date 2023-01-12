#!/usr/bin/python3
<<<<<<< HEAD
"""
The Module to read a file and print our to stdout
Using: def read_file(filename=""):
"""


def read_file(filename=""):
    """ the methond which read a text file with UTF8
        and print it to stdour
    Args:
       filename: a file name to be readed
    """
    with open(filename, encoding="utf-8") as r:
        print(r.read(), end="")
=======
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
>>>>>>> 0f9335aeefad229f6daf32095d498cf8bbd11781
