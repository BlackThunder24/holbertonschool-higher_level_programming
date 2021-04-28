#!/usr/bin/python3
for numero in range(0, 10):
    for numero2 in range(0, 10):
        if numero is 8 and numero2 is 9:
            print("{:d}{:d}".format(numero, numero2))
        elif numero < numero2:
            print("{:d}{:d}".format(numero, numero2), end=", ")
