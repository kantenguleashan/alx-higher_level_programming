#!/usr/bin/python3
"""  MODULW WITH A FUNCTION THAT READS INPUT FILE"""


def read_file(filename=""):
    """ FUNCTION FOR A FILE

    Args:
        filename: filename

    Raises
        Exception: when the file can be opened

    """

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
