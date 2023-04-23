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

    def area(self):
        return (self.__size)**2

    @property
    def size(self):
        """size: size of the square
        setter validating size is int and >= 0

        Raise:
             TypeError and ValueError
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size: size of the square
        setter validating size is int and >= 0

        Raise:
             TypeError and ValueError
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
            prints in stdout the square with the character #
        """
        print("\n".join(["".join(["#" for a in range(self.__size)]) for b in range(self.__size)]))

my_square = Square(3)
my_square.my_print()