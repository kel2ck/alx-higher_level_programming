#!/usr/bin/python3
""" Defines a module that adds two integers """


def add_integer(a, b=98):
    """
    A function that adds 2 integers
    Args:
        a: first integer
        b: second integer
    Returns:
        addition of two integers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
