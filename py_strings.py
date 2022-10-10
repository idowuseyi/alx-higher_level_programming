# More on python strings

course = 'Python for Beginners'
# we have to know the quotation mark to use always
print(course)
course2 = 'Python for "Beginners"'
print(course2)
# we can use multiple line comment, it is 3 single coats

long_name = '''
This is me programming in Python
Nothing is impossible
We can all do it
'''
print(long_name[0:-2])

# string functions: we can access this with the dot operator

print(len(course))
print(course.upper())

'''
There is a difference between functions and methods. When a functions belongs or is meant for a specific purpose we call it method
len is a general operand so we call it function
while upper, isalpha, etc are all methods cos they are used only on strings

note methods do not change string but create a new one entirely
'''

print(course.replace('Beginners', 'Absolute Beginners'))
# we can do plenty things with methods

print('Python' in course)
# note the find method produces an index while the in operator produces a boolean value
print(len(course))