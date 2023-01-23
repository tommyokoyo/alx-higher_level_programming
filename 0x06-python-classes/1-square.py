#!/usr/bin/python3
"""
square class defination
"""


class Square:
    """
    Class with private instance variable
    """

    def __init__(self, size=0):
        """
        Args:
            size: size of square
        """
        self.__size = size
