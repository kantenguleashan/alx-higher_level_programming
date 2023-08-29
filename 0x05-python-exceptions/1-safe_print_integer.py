#!/usr/bin/python3
def safe_print_integer(value):
    """Print int with a certain format

    Args:
        value (int):  the int to print

    RETURN:
        false for typeerror or return true
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)

