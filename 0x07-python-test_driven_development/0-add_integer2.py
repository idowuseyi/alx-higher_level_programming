# #!/usr/bin/python3
def add_integer(a, b=98):
    """>>> from 0-add_integer import add_integer
    >>> print(add_integer(1, 2))
    3
    >>> print(add_integer(100, -2))
    98
    >>> print(add_integer(2))
    100
    >>> print(add_integer(100.3, -2))
    98
    >>> try:
    ...     print(add_integer(4, "School"))
    ... except Exception as e:
    ...     print(e)
    b must be an integer
    >>> try:
    ...    print(add_integer(None))
    ...    except Exception as e:
    ...    print(e)
    a must be an integer
    """

    if a is None or b is None:
        raise Exception('a must be an integer')
    elif type(a) != int or type(b) == float:
        a = int(a)
        b = int(b)
    else:
        if type(a) != int:
            raise TypeError('a must be an integer')

        elif type(b) != int:
            raise TypeError('b must be an integer')

    return a + b
# Test function


if __name__ == '__main__':
    '''print(add_integer(1, 2))
    print(add_integer(100, -2))
    print(add_integer(2))
    print(add_integer(100.3, -2))
    try:
        print(add_integer(4, "School"))
    except Exception as e:
        print(e)
    try:
        print(add_integer(None))
    except Exception as e:
        print(e)'''
