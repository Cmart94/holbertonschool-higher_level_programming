#!/usr/bin/python3
"""
define the size of a square
"""


class Square:
    """Private square size validations atribute"""
    def __init__(self, __size=0):
        if type(__size) is int:
            pass
        else:
            raise TypeError("size must be an integer")
        if __size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = __size
