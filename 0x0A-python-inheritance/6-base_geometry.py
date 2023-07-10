#!/usr/bin/python3
"""Contains the class BaseGeometry."""


class BaseGeometry:
    """A class with public attribute area."""

    def area(self):
        """Raise an exception when called."""
        raise Exception("area() is not implemented")
