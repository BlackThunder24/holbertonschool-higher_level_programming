#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as black:
        print("Exception: {}".format(black), file=sys.stderr)
        return False
