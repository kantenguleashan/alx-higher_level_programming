#!/usr/bin/python3
"""DEFINES A TETX INSERTION FUNCT.."""


def append_after(filename="", search_string="", new_string=""):
    """INSERT A TEXT AFTER EACH LINE.

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

