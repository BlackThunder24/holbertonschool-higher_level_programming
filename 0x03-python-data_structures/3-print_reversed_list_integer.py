#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if isinstance(my_list, int):
        my_list.reverse()
    for l in my_list:
        print("{:d}".format(l))