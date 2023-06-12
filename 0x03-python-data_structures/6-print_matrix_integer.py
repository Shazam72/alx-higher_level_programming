#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        list_len = len(i)
        if list_len > 0:
            last = i[list_len - 1]
            for j in i:
                print("{:d}".format(j), end=" " if j != last else "")
        print('')
