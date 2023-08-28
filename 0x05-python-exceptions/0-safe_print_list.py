#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Printing the right elements for my program
    Args:
        where we will print.
        numbers to be printed.

    Returns:
        The number of elements printed.
    """
    sett = 0
    for k in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (sett)

