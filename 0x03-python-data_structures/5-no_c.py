#!/usr/bin/python3
def no_c(my_string):
    my_text = [l for l in my_string if l != 'c' and  l != 'C']
    return ("".join(my_text))
