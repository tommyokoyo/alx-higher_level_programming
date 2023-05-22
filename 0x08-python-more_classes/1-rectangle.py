#!/usr/bin/python3
"""
    Rectangle class defination
"""


class Rectangle:
    """
        Defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """
            args:
                width: (int) width of the rectangle
                height: (int) height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """
            Args:
                width: takes in an interger not less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """
            Args:
                height: takes in an interger not less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
