#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for keys in a_dictionary:
        if keys != key:
            continue
        else:
            return a_dictionary.pop(key)
