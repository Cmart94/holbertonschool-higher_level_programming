#!/usr/bin/python3
"""
define the size of a square
"""


class Square:
    def __init__(self, size=0):
        """
        Initialize size variable
        """
        self.__size = size

    @property
    def size(self):
        """Returns the square size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the square size with some conditions"""
        if type(value) is int:
            pass
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        calculate the square of a string
        """
        return (self.__size * self.__size)
