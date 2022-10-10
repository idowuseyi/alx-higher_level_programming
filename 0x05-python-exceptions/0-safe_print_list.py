
def safe_print_list(my_list=[], x=0):
    count = 0
    while count < x:
        try:
            print("{:d}".format(my_list[count]), end='')
            count += 1
        except IndexError:
            break
    print()
    return count
'''
    count = 0
    for i in range(0, len(my_list)):
        if i < x:
            print("{}".format(my_list[i]), end="")
            count += 1
    print()
    return count
'''

my_list = [1, 2, 3, 4, 5, 6]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list(my_list, (len(my_list) + 2))
print("nb_print: {:d}".format(nb_print))