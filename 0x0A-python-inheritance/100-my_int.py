#!/usr/bin/python3
"""
Defines a class MyInt that inherits from int.

"""


class MyInt(int):
    """A custom integer class."""

    def __ne__(self, x):
        """Return True if x is equal to self."""
        return int(self) == x

    def __eq__(self, x):
        """Return True if x is not equal to self."""
        return int(self) != 
