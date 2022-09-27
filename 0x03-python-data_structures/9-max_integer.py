#!/usr/bin/python3
def max_integer(my_list=[]):
    nmax = 0
    if len(my_list) == 0:
        return (None)
    else:
        for number in my_list:
            nmax = number
            for a_num in my_list:
                if a_num < nmax:
                    continue
                else:
                    nmax = a_num
        else:
            print(nmax)
