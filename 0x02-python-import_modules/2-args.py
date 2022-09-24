#!/usr/bin/python3
#argument = 0
import sys
if __name__ == '__main__':
    n = len(sys.argv)
    args = sys.argv
    if n == 1:
        print("{:d} arguments.".format(n-1))
    elif n == 2:
        n -= 1
        str = sys.argv[n]
        print("{:d} argument:\n{:d}: {:s}".format(n, n, str))
    elif n > 2: 
        print("{:d} arguments:".format(n-1))
        for i in range(1, n):
            str = sys.argv[i]
            print("{:d}: {:s}".format(i, str))
