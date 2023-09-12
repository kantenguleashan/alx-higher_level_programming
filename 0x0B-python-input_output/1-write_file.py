#!/usr/bin/python3
"""  MODULE THAT READS FROM FILE
"""


def write_file(filename="", text=""):
    """ FUNCTION THAT WRITES TO TEXT

    Args:
        filename: filename
        text: text to write

    Raises
        Exception: WHEN OPENED

    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
