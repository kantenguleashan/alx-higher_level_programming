#!/usr/bin/python3
"""  MODULE THAT READS FROM FILE
"""


def append_write(filename="", text=""):
    """  APPENDING FUNCTION To a text file

    Args:
        filename: filename
        text: text to write

    Raises
        Exception: ON OPENED
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
