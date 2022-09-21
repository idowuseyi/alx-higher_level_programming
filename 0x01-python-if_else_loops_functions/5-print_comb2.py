#!/usr/bin/python3
sep = ','
for i in range(0, 100):
    if i == (100 - 1):
        print("{}".format(str(i).zfill(2)), end='')
    else:
        print("{}{} ".format(str(i).zfill(2), sep), end='')
    i += 1
print('\n')


