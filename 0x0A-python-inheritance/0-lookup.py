#!/usr/bin/python3
"""
this module define a lookup for a object
"""


def lookup(obj):
    """
    return the list od available attributes
    and methods of an object
    """
    return (dir(obj))
