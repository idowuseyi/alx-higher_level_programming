#!/usr/bin/python3
def no_c(my_string):
    new_str = [my_string.translate({ord(i): None for i in 'Cc'})]
    return (" ".join(new_str))
