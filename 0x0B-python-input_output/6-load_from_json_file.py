#!/usr/bin/python3
""" MODULE FOR CREATING JSON FROM OBJECT
"""
import json


def load_from_json_file(filename):
    """ FUNCTION THAT CREATS OJBECT

    Args:
        filename: textfile name

    Raises:
        Exception: when the object can't be encoded

    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
