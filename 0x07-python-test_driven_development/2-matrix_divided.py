#!/usr/bin/python3
"""
    Contains a function that takes in
    a matrix and divides by a given number
"""


def matrix_divided(matrix, div):
    """
        Funtion that divides elements of a matrix
        Args:
            matrix: (list)
            div: (int/float)
    """
    if matrix:
        for lists in matrix:
            if isinstance(lists, list):
                pass
            else:
                print("matrix must be a matrix\
                      (list of lists) of integers/floats")
        matrix_counter = 0
        lists_len = 0
        for lists in range(len(matrix)):
            if matrix_counter == 0:
                lists_len = len(matrix[lists])
                matrix_counter += 1
            else:
                if len(matrix[lists]) == lists_len:
                    for items in matrix[lists]:
                        if type(items) is int or type(items) is float:
                            if type(div) is int or type(div) is float:
                                if div == 0:
                                    raise ZeroDivisionError("division by zero")
                                else:
                                    pass
                            else:
                                raise TypeError("div must be a number")
                        else:
                            raise TypeError("matrix must be a matrix\
                                (lists of lists) of integers/floats")
                else:
                    raise TypeError("Each row of the matrix\
                                    must have the same size")
        return [[round(items/div, 2) for items in lists] for lists in matrix]
