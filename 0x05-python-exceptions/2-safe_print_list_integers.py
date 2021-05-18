#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    reckon = 0
    for r in range(0, x):
        try:
            print("{:d}".format(my_list[r]), end="")
            reckon += 1
        except TypeError:
            None
        except ValueError:
            None
    print()
    return reckon
