#!/usr/bin/python3
"""
This module is a base object
"""


class Base:
    """
    Private base id definition
    """

    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = self. __nb_objects
