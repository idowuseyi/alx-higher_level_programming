'''
List comprehencsion allows for easy operation
 both in creating and manipulating list


'''

s = 2
r = 37
my_list = [1, 2, 3, 4, 5, 2, 1, 4, 89]
n_list = list(map(lambda x: x, my_list))
nn_list = [x if (x != x) for x in my_list]


print(nn_list)

# say we want to create list containing squares
# with a for loop
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

#with lambda

squres = list(map(lambda x: x**2, range(10)))

# directly
sqrs = [x**2 for x in range(10)]

print(squres, sqrs)

'''
also check the below
'''

combs1 = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]

# same thing as

combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
#combs1 == combs

note = [(x, (x/(x+1)), (x**2)) for x in range(10)]
print(note)