#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if type(matrix) == list:
        n = len(matrix)
        nlist = ('\n'.join([''.join(['{:n}'.format(item) for item in row])"n"
                 for row in matrix]))
        return (nlist)
    else:
        return (matrix)
