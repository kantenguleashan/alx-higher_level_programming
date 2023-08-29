#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """print the all elements.

    Args:
        my_list (list):  List.
        x (int): elements number

    Returns:
    PRINTED number.
    """
    ret = 0
    for p in range(x):
        try:
            print("{}".format(my_list[p]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (re)
