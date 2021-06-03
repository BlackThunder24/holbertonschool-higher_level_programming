#!/usr/bin/python3
"""Module MyList class"""


class MyList(list):
    """class of list"""
    def __init__(self):
        """initializes"""
        super().__init__()

    def print_sorted(self):
        """prints the list"""
        print(sorted(self))
