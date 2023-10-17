#!/usr/bin/python3

"""Integers addition module
"""


def add_integer(a, b=98):
    """Return addition of a and b

    Float arguments are casted to ints before addition.
    >>> add_integer(1, 3)
    4
    >>> add_integer(1, -4)
    3
    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)