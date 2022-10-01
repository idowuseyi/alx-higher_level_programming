#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    n = len(a_dictionary)
    for keys in a_dictionary:
        if keys == key:
            a_dictionary[keys] = value
        else:
            a_dictionary[key] = value
        return a_dictionary
