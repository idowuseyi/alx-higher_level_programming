#!/usr/bin/python3
"""Rectangle class to represent a square"""


class Rectangle:
    """
    Defines a Rectangle and its basic properties
    """
    def __init__(self, width=0, height=0):
        """
        Innitialize the width of the rectangle
        Innitialize the height of the rectangle
        :param width and height of the rectangle
        """
        self.__width = width
        self.__height = height

    def width(self, value):
        if value is None:
            return 1
        elif type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be >= 0')
        else:
            self.value = value

    def height(self, value):
        if value is None:
            return 1
        elif type(value) is not int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be >= 0')
        else:
            self.value = value


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print(my_rectangle.__dict__)

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle.__dict__)
    """
    try:
        print(my_rectangle.width)
    except Exception as e:
        print(e)

    try:
        print(my_rectangle.__width)
    except Exception as e:
        print(e)
    """