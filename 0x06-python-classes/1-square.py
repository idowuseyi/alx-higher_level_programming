#!/usr/bin/python3
"""Square class to represent a square"""


class Square:
    """
    Defines a Square and its basic properties
    >>> square_1 = Square()
    >>> square_2 = Square(7)
    """

    def __init__(self, size: int) -> None:
        """
        Innitialize the size of the square
        :param size: int size of square
        """
        self.__size = size


if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)
