#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if type(matrix) == list:
        for row in matrix:
            for item in row:
                print("{}".format(item), end=' ')
            print()
    else:
        print(matrix)
