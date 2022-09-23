#!/usr/bin/python3
def calculator_1():
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(10, 5)))
    print("{} - {} = {}".format(a, b, sub(10, 5)))
    print("{} * {} = {}".format(a, b, mul(10, 5)))
    print("{} / {} = {}".format(a, b, div(10, 5)))
if __name__ == "__main__":
    calculator_1()
