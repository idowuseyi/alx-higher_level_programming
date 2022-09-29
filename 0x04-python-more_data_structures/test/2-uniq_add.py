#!/usr/bin/python3
def uniq_add(my_list=[]):
    conv_list = set(my_list)
    total = 0
    unique_list = list(conv_list)
    n = len(unique_list)
    for i in range(n):
        total += unique_list[i]
    return total

if __name__ == '__main__':
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))
