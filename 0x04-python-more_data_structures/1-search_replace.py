#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n_list = list(map(lambda x: x, my_list))
    n = len(n_list)
    for i in range(0, n-1):
        if n_list[i] == search:
            n_list[i] = replace
    return n_list
