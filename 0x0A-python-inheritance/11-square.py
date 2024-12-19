#!/usr/bin/python3
"""Define a Square class that inherits from Rectangle (9-rectangle.py), (task based on 10-square.py)"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Type class of a square inherit a rectangle"""

    def __init__(self, size):

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):

        string = "[Square] " + str(self.__size) + "/" + str(self.__size)
        return string

