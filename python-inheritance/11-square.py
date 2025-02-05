#!/usr/bin/python3
"""Module for the class Square."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that inherits from Rectangle"""

    def __init__(self, size):
        """Method that initializes the square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Method that return the areo of the square"""
        return self.__size ** 2

    def __str__(self):
        """Method that return a square description."""
        return "[Square] {}/{}".format(self.__size, self.__size)
