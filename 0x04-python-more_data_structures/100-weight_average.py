#!/usr/bin/python3

def weight_average(my_list=[]):
    """
    Find the average of weighted ints
    """
    if my_list is None or my_list == []:
        return 0
    s_xy = sum(map(lambda a: a[0] * a[1], my_list))
    s_x = sum(map(lambda a: a[1], my_list))
    return s_xy / s_x
