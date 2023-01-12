#!/usr/bin/python3
<<<<<<< HEAD
"""
The module to append string to the file
def append_write(filename="", text=""):
"""


def append_write(filename="", text=""):
    """ The method append a string to a text file (UTF8)
    and returns the number of characters written:
    Args:
        filename: a file name to write to
        text: text to be write
    Return:
        No. of character writen
    """
    with open(filename, 'a', encoding='utf-8') as f:
=======
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file."""
    with open(filename, "a", encoding="utf-8") as f:
>>>>>>> 0f9335aeefad229f6daf32095d498cf8bbd11781
        return f.write(text)
