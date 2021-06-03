#!/usr/bin/python3
"""Function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class"""
    if type(obj) is a_class or isinstance(obj, a_class):
        return True

    else:
        return False
