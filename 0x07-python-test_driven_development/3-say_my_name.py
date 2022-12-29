#!/usr/bin/python3
"""Defines a name-printing function."""


def say_my_name(first_name, last_name=""):
    """
    A function that prints "My name is" followed
    by the first name and optional last name
    Args:
        first_name: String
        last_name:  String
    """
    if type(first_name) is not str:
        return TypeError("first_name must be a string")
    elif type(last_name) is not str:
        return TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
