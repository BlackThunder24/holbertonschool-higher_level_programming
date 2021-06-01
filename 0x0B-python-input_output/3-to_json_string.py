#!/usr/bin/python3
"""This function converts an object to JSON"""


import json


def to_json_string(my_obj):
    """Convert object to json"""
    return json.dumps(my_obj)
