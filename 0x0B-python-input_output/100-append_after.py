#!/usr/bin/python3
<<<<<<< HEAD
""" Module that executes a function that appends a line """


def append_after(filename="", search_string="", new_string=""):
    """ Function that appends a new line when a string is found
    Args:
        filename: filename
        search_string: string to search
        new_string: string to append
    """

    res_line = []
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            res_line += [line]
            if line.find(search_string) != -1:
                res_line += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(res_line))
=======
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.
    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
>>>>>>> 0f9335aeefad229f6daf32095d498cf8bbd11781
