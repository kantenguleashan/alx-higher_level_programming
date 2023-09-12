#!/usr/bin/python3
""" Contains module that reads from OUTPUT """


def read_file(filename=""):
    """ FUNCTION

    Args:
        filename:  FILE NAME

    Raises
        Exception: WHEN OPENED

    """

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
