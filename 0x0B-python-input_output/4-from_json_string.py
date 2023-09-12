#!/usr/bin/python3
""" FUNCTION MODULE THAT RETURNS JSON REPRE.
"""
import json


def from_json_string(my_str):
    """ Function that returns an object by a JSON representation

    Args:
        my_str: JSON representation

    Raises:
        Exception: WHEN STRING CANT BE DECODED

    """
    return json.loads(my_str)
