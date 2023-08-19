#!/usr/bin/python3
"""
    Check if an object is an instance of the specified
    class
"""


def is_same_class(obj, a_class):
    """
        checks if object is in same class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
