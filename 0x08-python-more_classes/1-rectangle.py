#!/usr/bin/python3
# coding: utf-8
"""A simple rectangle module."""


class Rectangle:
    """A python class that represent a rectangle."""

    def __init(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width property."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width property."""
        self.__width = value

    @property
    def height(self):
        """Getter for height property."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height property."""
        self.__height = value
