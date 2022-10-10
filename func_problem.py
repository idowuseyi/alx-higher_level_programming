
'''
my_list = [1, 4, 3, 7, 5, 9, 2, 6]
def prob_func(list=[]):
    def funct_odd_list(list=[]):
        for i in range(len(list)-1):
            if list[i] % 2 != 0:
                list[i] = True
            else:
                list[i] = False
        #return list
    return list

print(prob_func(my_list))
'''

#solution

def is_it_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True

def change_list(list, func):
    oddlist = []
    for i in list:
        if func(i):
            oddlist.append(i)
    return oddlist
olist = range(1, 20)

print(change_list(olist, is_it_odd))