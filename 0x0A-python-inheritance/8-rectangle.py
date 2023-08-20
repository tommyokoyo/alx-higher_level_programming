#!/usr/bin/python3
"""
    BaseGeometry module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        BaseGeometry class
    """

    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('height', height)

        self.width = width
        self.height = height
