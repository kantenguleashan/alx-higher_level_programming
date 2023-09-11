#!/usr/bin/python3
"""MODULE ONLY SUBCLASS
"""


def inherits_from(obj, a_class):
    """
RETURNS true if object is an instance of a
 class inherited from specified class .
    """
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
