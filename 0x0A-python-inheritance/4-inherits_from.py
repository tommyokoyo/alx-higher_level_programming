#!/usr/bin/python3
"""
    Checks if an object is an instance of,
    or if the object is an instance of a class
    that inherited from, the specified class
"""


def inherits_from(obj, a_class):
    """
        checks if obj is an instance of the class that inherited
        (directly or indirectly)
        Args:
            obj: object
            a_class: class
    """
    return type(obj) != a_class and isinstance(obj, a_class)
