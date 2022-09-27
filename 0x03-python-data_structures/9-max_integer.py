#!/usr/bin/python3
def max_integer(my_list=[]):
    nmax = 0
    if len(my_list) == 0:
        return None
    else:
        nmax = my_list[0]
        for item in my_list:
            if item > nmax:
                nmax = item
        return nmax
