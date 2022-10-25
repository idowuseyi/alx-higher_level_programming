#!/usr/bin/python3
def is_same_class(obj, a_class):
    """This function checks if an object is an instance of the specified class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False


if __name__ == "__main__":
    a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
    if is_same_class(a, float):
        print("{} is an instance of the class {}".format(a, float.__name__))
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))
