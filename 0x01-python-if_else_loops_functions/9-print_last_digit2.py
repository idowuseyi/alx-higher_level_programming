#!/usr/bin/python3
def print_last_digit(number):
    if number < 1:
        positive_num = abs(number)
        number = (positive_num % 10)
        print("{:d}".format(number), end='')
    elif number == 0:
        print("{:d}".format(number), end='')
    elif number > 0:
        print("{:d}".format(number % 10), end='')
    else:
        return (number)
