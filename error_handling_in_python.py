try:
    age = int(input('Age: '))
    income = 8000
    earn_index = income / age
    print(earn_index)
except ZeroDivisionError:
    print('Age cannot be 0')
except ValueError:
    print('Invalid Value')

'''
0 means success while 1 means a scrash

in case of a wrong input
We can handle the error ourself - exception error
we use try: except
We must handle different kinds of error in our program
'''