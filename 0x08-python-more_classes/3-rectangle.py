#!/usr/bin/python3
# coding: utf-8
"""A simple rectangle module."""


class Rectangle:
    """A python class that represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Init method."""
        self.width = width
        self.height = height

    def __str__(self):
        """
        Set __str__ with custom function.

        Description: print '#' to represent the rectangle
        """
        if not (self.__height == 0 or self.__height == 0):
            for x in list(range(self.height)):
                for y in list(range(self.width)):
                    print('#', end='')
                print()
        return ''

    @property
    def width(self):
        """Getter for width property."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width property."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height property."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height property."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Get current rectangle instance area."""
        return self.__height * self.__width

    def perimeter(self):
        """Get current rectangle instance perimeter."""
        if self.__height == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)
