#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    atuple = list(tuple_a)
    btuple = list(tuple_b)
    for val in atuple:
        if val is None:
            val = 0
        else:
            val = val
    for val in tuple_b:
        if val2 is None:
            val2 = 0
        else:
            val2 = 0
    tuple_a = tuple(atuple[0], atuple[1])
    tuple_b = tuple(btuple[0], btuple[1])
    add_tuple = tuple(map(lambda i, j: i + j, tuple_a, tuple_b))
    return (add_tuple)
