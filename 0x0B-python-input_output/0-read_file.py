#!/usr/bin/python3
def read_file(filename=""):
    """
    This finction read a file
    """
    with open(filename, encoding='utf-8') as f:
        """ print the content of a utf-8 file to a stdout"""
        for line in f:
            print(line, end='')
