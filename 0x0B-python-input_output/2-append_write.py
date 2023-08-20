#!/usr/bin/python3
"""
Defines a text file-append function.
"""


def append_write(filename="", text=""):
    """
    Append a string at the end of a text file(UTF8),
    and returns the number of characters added.
    """
    with open(filename, 'a', encoding='UTF8') as a_file:
        return a_file.write(text)
