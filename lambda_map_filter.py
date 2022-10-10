

sum1 = lambda x, y: x + y
#sum1(3, 4)
print(sum1(3, 4))

C = [39.2, 36.5, 37.3, 38, 37.8]
F = list(map(lambda x: (float(9)/5)*x + 32, C))
print(F)

# filter filter(f, l) returns the element if the expression was true
'''
only produce value when a condition is met.
'''
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
odd_numbers = list(filter(lambda x: x % 2, fibonacci))
print(odd_numbers)
even_numbers = list(filter(lambda x: x % 2 == 0, fibonacci))
print(even_numbers)

# Reduce
'''
the function
reduce(func, seq)

keeps performing a function on two in a passed argument per time
just like recursion
'''

import functools
reducey = functools.reduce(lambda x,y: x+y, [47, 11, 42, 13])
print(reducey)

# max with reduce

from functools import reduce
f = lambda a,b: a if (a > b) else b
max_reduce = reduce(f, [47, 11, 42, 102, 13])
print(max_reduce)

# calculating sum of numbers from 1 to 100:

from functools import reduce
sum_reduce = reduce(lambda x, y: x+y, range(1, 101))
print(sum_reduce)