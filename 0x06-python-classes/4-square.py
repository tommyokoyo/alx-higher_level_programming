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
        if type(size) is not int:
            raise TypeError("Size must be an interger")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return (self.__size)**2
    
    def size(self):
        return self.size
    
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.size = value
