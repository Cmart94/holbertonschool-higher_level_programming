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
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x  must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
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

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """Set rectangles height"""

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__heigth = height

    @x.setter
    def x(self, x):
        """Set rectangles x position"""

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """set rectangles y position"""

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Get rectangle area"""

        return (self.__width * self.__height)

    def display(self):
        """
        prints in stdout the Rectangle instance with the character #
        """

        array = ""
        for i in range(self.x):
            print()
        for i in range(self.height):
            for i in range(self.y):
                array = array + " "
            for j in range(self.width):
                array = array + ("#")
            print(array)
            array = ""

    def __str__(self):
        """Override the __str__ method"""

        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
            self.id, self.x, self.y, self.width, self.height)
