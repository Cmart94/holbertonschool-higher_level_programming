#!/usr/bin/python3
"""
This module inherite a Base class
"""

from models.base import Base


class Rectangle(Base):
    """
    My rectagle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        rectangle class atribute initialization
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Returns the rectangle width"""

        return (self.__width)

    @property
    def height(self):
        """Returns the rectangle height"""

        return (self.__height)

    @property
    def x(self):
        """Returns the rectangle x position"""

        return (self.__x)

    @property
    def y(self):
        """Returns the rectangle y position"""

        return (self.__y)

    @width.setter
    def width(self, width):
        """Set rectangle widht"""

        self.__width = width

    @height.setter
    def height(self, height):
        """Set rectangles height"""

        self.__heigth = height

    @x.setter
    def x(self, x):
        """Set rectangles x position"""

        self.__x = x

    @y.setter
    def y(self, y):
        """set rectangles y position"""

        self.__y = y
