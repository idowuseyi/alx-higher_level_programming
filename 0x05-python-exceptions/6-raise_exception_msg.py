#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        raise NameError('')
    finally:
        print("{}".format(message), end='')


if __name__ == "__main__":
    try:
        raise_exception_msg("C is fun")
    except NameError as ne:
        print(ne)