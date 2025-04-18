#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent a square."""
    __size = None

    def area(self):
        return self.__size ** 2

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise ValueError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
