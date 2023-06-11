#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    rows = len(matrix)
    for i in list(range(0, rows)):
        cols = len(matrix[i])
        for j in list(range(0, cols)):
            to_print = "{}".format(matrix[i][j])
            if matrix[i][j] != matrix[i][cols - 1]:
                to_print += " "
            print(to_print, end="")
        print('')
