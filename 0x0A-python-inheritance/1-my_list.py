#!/usr/bin/python3
"""CLASS THAT INHERITS FROM LISTS
"""


class MyList(list):
    """ INHERITED"""
    def print_sorted(self):
        """SORTED LIST PRINTED
        (ascending sort)
        """
        print(sorted(self))
