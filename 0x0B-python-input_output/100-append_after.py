#!/usr/bin/python3
"""
Defines Append after line function.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file,
    after each line containing as a specific string.

    Creates file, gets line string
    if line string == search_string
    appends new string after.

    """
    file_text = ""
    with open(filename, 'r+', encoding="UTF8") as a_file:
        for line in a_file:
            file_text += line
            if search_string in line:
                file_text += new_string
        a_file.seek(0)
        a_file.write(file_text)
