#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    divide = []
    for l in range(len(my_list)):
        if my_list[l] % 2 == 0:
            divide.append(True)
        else:
            divide.append(False)
    return (divide)
