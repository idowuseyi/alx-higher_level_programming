#!/usr/bin/python3
def read_file(filename=""):
    """
    This finction read a file
    """
    with open('filename', encoding='utf-8') as input_file:
         print(input_file.read())
