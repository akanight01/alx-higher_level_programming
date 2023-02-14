#!/usr/bin/python3
<<<<<<< HEAD
"""
The module to write string to the file
Using: def write_file(filename="", text=""):
=======
"""This function writes a string to a text file
    and return number of characters written
>>>>>>> 0f9335aeefad229f6daf32095d498cf8bbd11781
"""


def write_file(filename="", text=""):
<<<<<<< HEAD
    """ The method writes a string to a text file (UTF8)
    and returns the number of characters written:
    Args:
        filename: a file name to write to
        text: text to be write
    Return:
        No. of character writen
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
=======
    """Write a string to a UTF8 text file.
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
>>>>>>> 0f9335aeefad229f6daf32095d498cf8bbd11781
