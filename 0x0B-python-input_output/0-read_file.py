#!/usr/bin/python3
def read_file(filename=""):
    """
    This finction read a file
    """
    with open('filename') as f:
        for line in f:
            print(line, end='')
