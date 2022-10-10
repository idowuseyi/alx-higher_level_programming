'''
matrixa = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix2 = [
    [4, 5],
    [3, 8]
]

def print_matrix_integer(matrix=[[]]):
    if type(matrix) == list:
        for row in matrix:
            for item in row:
                print("{} ".format(item), end='')
            print()
    else:
        print(matrix)

#print_matrix_integer(matrixa)
#print_matrix_integer("--")
print_matrix_integer()

for i in matrix:
    print(())
'''

t = (3, , 5, 8, 9)

'''
nlen = len(t)
if type(t) == tuple:
    print('T', nlen)
else:
    print('f')
'''
