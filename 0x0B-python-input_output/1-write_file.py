#!/usr/bin/python3
"""
Contains the function "wrtie_file"

"""


def write_file(filename="", text=""):
    """writes a stringto a text file"""
    with open(filename, 'w', encoding="utf-8") as file_:
        return file_.write(text)
    return 0
