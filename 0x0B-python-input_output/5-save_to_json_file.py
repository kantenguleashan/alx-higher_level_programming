#!/usr/bin/python3
""" MODULE THAT WRITES AN OBJECT TO A TExt file
"""
import json


def save_to_json_file(my_obj, filename):
    """ Function FOR WRITING A JSON OBJECT

    Args:
        my_obj: object
        filename: textfile name

    Raises:
        Exception: WHEN FAILS TO DECODE

    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
