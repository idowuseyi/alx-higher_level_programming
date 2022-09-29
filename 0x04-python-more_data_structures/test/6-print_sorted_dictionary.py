#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for items in sorted(a_dictionary):
        print("{}: {}".format(items, dico.get(items)))

if __name__ == '__name__':
    a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
    print_sorted_dictionary(a_dictionary)
