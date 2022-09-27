#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    nlist = []
    if len(my_list) == 0:
        return None
    for item in my_list:
        if item % 2 == 0:
            nlist.append(True)
        else:
            nlist.append(False)
    return nlist
