'''

lines = [2, 2, 2, 2, 5]
for x_count in lines:
    output = ''
    for count in range(x_count):
        output += "x"
    print(output)
'''
'''
names = ['John', 'Noah', 'Ade', 'seyi']
names[0] = 'Mary'
print(names[2:])
print(names)
'''

# find the highest value in a list
num = [2, -3, 90, 8, 8, 4, 3, 5, 3]
del num[1]

print(num)
'''
t = []
def div_by2(my_list=[ ]):
    nlist = []
    if len(my_list) == 0:
        return None
    
    for item in my_list:
        if item % 2 == 0:
            nlist.append(True)
        else:
            nlist.append(False)
    return nlist

print(nlist)
#div_by2(num)
div_by2(t)

def print_max(my_list=[]):
    val = 0
    for number in num:
        val = number
        for a_num in num:
            if a_num < val:
                continue
            else:
                val = a_num
    else:
        val = a_num
        #print(val)
        return val

print_max(num)
# python way of the solution

#max_num = max(num)
#print(max_num)
'''