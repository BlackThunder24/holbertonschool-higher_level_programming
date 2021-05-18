#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ls = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            ls += 1
    except IndexError:
        None
    print()
    return ls
