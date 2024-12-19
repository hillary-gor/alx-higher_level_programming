#!/usr/bin/python3
"""Define a class Rectangle that inherits from BaseGeometry (7-base_geometry.py), (task based on 8-rectangle.py)"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Type class of Rectangle inherit BaseGeometry"""

    def __init__(self, width, height):

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):

        return self.__width * self.__height

    def __str__(self):

        string = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return string

