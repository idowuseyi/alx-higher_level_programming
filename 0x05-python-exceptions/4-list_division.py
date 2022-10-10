#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0

    try:
        for i in range(0, max(len(my_l_1), len(my_l_2))):
            list_length[i] = my_list_1[i] / my_list_2[i]
            print(list_length)
    except ZeroDivisionError:
        print("division by 0")
        continue
    except TypeError:
        print("out of range")
        continue
    finally:
        return list_length


my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1,my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1,my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)