#!/usr/bin/python3
def add_0():
    import add_0 as add_num
    a = 1
    b = 2
    print(f"{a} + {b} = {add_num.add(1, 2)}")
if __name__ == "__main__":
    add_0()
