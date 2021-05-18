#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    ls = []
    for i in range(list_length):
        try:
            div = (my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            div = 0
            print("division by 0")
        except TypeError:
            print("wrong type")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            ls.append(div)

    return ls
