#!/usr/bin/python3
"""Class Myint"""


class MyInt(int):
    """My int class"""
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
