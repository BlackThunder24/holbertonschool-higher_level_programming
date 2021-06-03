#!/usr/bin/python3
"""Add attribute""" 

def add_attribute(obj, name, value):
    """Add attribute"""
    if "__dict__" in dir(obj):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
