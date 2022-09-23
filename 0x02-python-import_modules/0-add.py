#!/usr/bin/python3
# importing add_o from its file
def main():
    import add_0 as add_num
    # assigning variable
    a = 1
    b = 2
    # printing the result
    print(f"{a} + {b} = {add_num.add(a, b)}")
if __name__ == "__main__":
    main()
