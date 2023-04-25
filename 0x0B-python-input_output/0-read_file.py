#!/usr/bin/python3
<<<<<<< HEAD
=======
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
>>>>>>> 5e672edc13e61c221d0d9bc6cd742692f5d6e566
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
<<<<<<< HEAD
=======
>>>>>>> 0f9335aeefad229f6daf32095d498cf8bbd11781
>>>>>>> 5e672edc13e61c221d0d9bc6cd742692f5d6e566
