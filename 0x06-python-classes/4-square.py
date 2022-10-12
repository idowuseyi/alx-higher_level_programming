#!/usr/bin/python3
"""Square class to represent a square"""


class Square:
    """
    Defines a Square and its basic properties
    >>> square_1 = Square()
    >>> square_2 = Square(7)
    """

    def __init__(self, size=0) -> None:
        """
        Innitialize the size of the square. the size can be specified.
        If they are not, the size defaults to 0
        :param size: int size of square ( > 0)
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self) -> int:
        """
        Retrieve the instance attribute size
        :return: the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value: int) -> None:
        """
        Set the value of the size
        :param: int size
        """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self) -> int:
        """
        Calculates and returns the area of the square
        :return: the area of the square
        """

        return self.__size ** 2


if __name__ == "__main__":
    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)
