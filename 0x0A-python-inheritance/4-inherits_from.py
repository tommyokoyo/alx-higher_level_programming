#!/usr/bin/python3
"""
    Checks if an object is an instance of,
    or if the object is an instance of a class
    that inherited from, the specified class
"""


def inherits_from(obj, a_class):
    """
        checks if obj is an instance of the class a_class
    """
    return isinstance(obj, a_class)
