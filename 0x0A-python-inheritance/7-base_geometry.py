#!/usr/bin/python3
"""
    BaseGeometry module
"""


class BaseGeometry:
    """
        BaseGeometry class
    """
    def area(self):
        """
            A method that raises an exception
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
            validates the value
            Args:
                name
                value
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
