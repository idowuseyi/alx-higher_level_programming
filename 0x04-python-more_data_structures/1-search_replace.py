#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n = len(my_list)
    for i in range(n):
        if my_list[i] == search:
            my_list[i] = replace
    return my_list
