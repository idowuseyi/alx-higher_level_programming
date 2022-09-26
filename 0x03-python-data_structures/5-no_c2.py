#!/usr/bin/python3
def no_c(my_string):
    for char in my_string:
        if char == '\n':
            break
        elif char == 'c' or char == 'C':
            continue
        else:
            print("{}".format(char), end="")
