a = 89
b = 10
#a, b = b, a
'''
a ^= b
b ^= a
a ^= b

a = a + b
b = a - b
a = a - b

a = a * b
b = a / b
a = a / b
'''
print("a={:d} - b={:d}".format(a, b))