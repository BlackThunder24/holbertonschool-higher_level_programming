#!/usr/bin/python3
"""Function inherits_from"""


def inherits_from(obj, a_class):
    """inherits_from"""
    if type(obj) is not a_class and isinstance(obj, a_class):
        return True

    else:
        return False
