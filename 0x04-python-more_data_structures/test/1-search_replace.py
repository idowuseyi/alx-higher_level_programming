#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n_list = list(map(lambda x: x, my_list))
    n = len(n_list)
    for i in range(0, n-1):
        if n_list[i] == search:
            n_list[i] = replace
    return n_list

if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
    new_list = search_replace(my_list, 2, 89)
    
    print(new_list)
    print(my_list)

