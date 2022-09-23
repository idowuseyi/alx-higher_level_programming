#!/usr/bin/python3
#argument = 0
for argument in argv:
    if len(argv) == 0:
        print("{:d} arguments:".format(len(argv)))
    else:
        print("{:d} {:s}".format(argv, argv[argument]))
