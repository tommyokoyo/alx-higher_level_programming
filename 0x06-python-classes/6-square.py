#!/usr/bin/python3
"""
square class defination
"""


class Square:
    """
    Class with private instance variable
    """

    def __init__(self, size=0, position=(0, 0)):
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
        
        self.__position = position

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
    
    @property
    def position(self):
        """Position: position of the square"""
        return self.__position
    
    @position.setter
    def position(self, position):
        """Position: must be a tuple of two intergers"""
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(type(m) != int for m in position) or any(n < 0 for n in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        return (self.__size)**2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for y in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(' ', end='')
                for j in range(self.__size):
                    print('#', end='')
                print()
