#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    max_number = my_list[0]
    for l in range(len(my_list)):
        if my_list[l] > max_number:
            max_number = my_list[l]
    return (max_number)
