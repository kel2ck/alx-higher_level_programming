#!/usr/bin/python3
"""
function that returns a python object represented by a JSON string

"""

import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
