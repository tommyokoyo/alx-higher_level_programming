#!/usr/bin/python3
"""
    prints out list in sorted order
"""


class MyList(list):
    """Inherits from list
    """
    def print_sorted(self):
        """Prints the list in ascending order
        """
        print(sorted(self))
