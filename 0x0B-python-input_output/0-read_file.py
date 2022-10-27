#!/usr/bin/python3
"""function that print the content of a utf8 encoded file to stdout"""
def read_file(filename=""):
    with open(filenane, encoding="utf-8") as f:
        """ prints the file content """
        for line in f:
            print(f.read(), end="")
