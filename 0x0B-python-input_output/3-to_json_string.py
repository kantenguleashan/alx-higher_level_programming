#!/usr/bin/python3
"""  MODULE THAT RETURNS JSON

"""
import json


def to_json_string(my_obj):
    """  FUNCTION THAT RETURNS JSON OBJECT REP

    Args:
        my_obj: object

    Raises:
        Exception: when the object can't be encoded

    """
    return json.dumps(my_obj)
