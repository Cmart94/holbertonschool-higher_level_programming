#!/usr/bin/python3
"""
This module define a class object that inherate a list
"""


class MyList(list):
    """class MyList"""

    def print_sorted(self):
        """
        print a list sorted
        """
        print(sorted(self))
