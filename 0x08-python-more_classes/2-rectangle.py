#!/usr/bin/python3
# coding: utf-8
"""A simple rectangle module."""


class Rectangle:
    """A python class that represent a rectangle."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

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
        if self.height == 0 or self.height == 0:
            return 0
        return 2 * (self.height + self.width)
