def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0:
            num = 'fizz'
           # print("{} ".format(num), end='')
        elif num % 5 == 0:
            num = 'Buzz'
        elif num % 3 == num % 5:
            num = 'FizzBuzz'
        else:
            num = num
        print("{} ".format(num), end='')

