#!/usr/bin/python3
"""function that reads a text file"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        content = f.read()
        if content != "":
            print(content[:-1])
