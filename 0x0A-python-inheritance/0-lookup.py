#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """returns a list of all available attributes"""
    return dir(obj)
