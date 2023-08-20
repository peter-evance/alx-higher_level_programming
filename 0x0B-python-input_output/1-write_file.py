#!/usr/bin/python3
"""
Defines a text file-writing function.
"""


def write_file(filename="", text=""):
    """
    Writes to text file and returns num chars written
    """
    with open(filename, 'w+', encoding='UTF8') as a_file:
        return (a_file.write(text))
