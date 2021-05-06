#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for m in range(len(matrix)):
        for r in range(len(matrix[m])):
            print("{:d}".format(matrix[m][r]), end="")
            if r != (len(matrix[m]) - 1):
                print(" ", end="")
        print("")
