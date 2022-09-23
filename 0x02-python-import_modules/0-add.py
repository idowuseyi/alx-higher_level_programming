#!/usr/bin/python3
def add_0():
    from add_0 import add
    a = 1
    b = 2
    print(f"{a} + {b} = {add(1, 2)}")
if __name__ == "__main__":
    add_0()
