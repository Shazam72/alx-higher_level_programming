#!/usr/bin/python3
# coding: utf-8
"""A simple rectangle module."""


class Rectangle:
    """A python class that represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Init."""
        self.width = width
        self.height = height

    def __str__(self):
        """
        Set __str__ with custom function.

        Description: print '#' to represent the rectangle
        """
        if self.width == 0 or self.height == 0:
            return ''
        for x in list(range(0, self.height)):
            for y in list(range(0, self.width)):
                print('#', end='')
            if x != self.height - 1:
                print()
        return ''

    def __repr__(self):
        """
        Set __repr__ with custom function.

        Description: just a custom __repr__
        """
        return "Rectangle({}, {})".format(self.width, self.height)

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
        return self.height * self.width

    def perimeter(self):
        """Get current rectangle instance perimeter."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.height + self.width)
