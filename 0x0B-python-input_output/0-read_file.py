#!/usr/bin/python3
"""This function reads a file and prints to standard output"""


def read_file(filename=""):
    """reads a file"""
    with open(filename, 'r') as file:
        print(file.read(), end="")
