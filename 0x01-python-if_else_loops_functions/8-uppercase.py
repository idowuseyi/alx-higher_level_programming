#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if 97 <= ord(ch) <= 122:
            ch = chr(ord(ch) - 32)
            print("{:s}". format(ch), end="")
        else:
            print("{:s}".format(ch), end="")
    sys.stdout.write('\n')
