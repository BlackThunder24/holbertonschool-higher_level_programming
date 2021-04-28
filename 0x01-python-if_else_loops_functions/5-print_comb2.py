#!/usr/bin/python3
for n in range(0, 99):
    if n <= 9:
        print(0, end="")
    print("{}".format(n), end=", " if n < 98 else ', {}\n'.format(99))
