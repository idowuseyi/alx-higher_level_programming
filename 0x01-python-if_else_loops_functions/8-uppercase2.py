#!/usr/bin/python3
def uppercase(str):
    for c in range(0, len(str)):
        if ord(str[c]) >= 97 and ord(str[c]) <=122:
            ord[c] -= 32
            i = ord[c]
            print("{}".format(chr(i)), end='')
        else:
            print("{}".format(str[c]), end='')
