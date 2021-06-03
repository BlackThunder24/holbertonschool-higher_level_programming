#!/usr/bin/python3
"""Empty class"""


class BaseGeometry:
    '''class BaseGeometry'''

    def area(self):
        ''' raise'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
