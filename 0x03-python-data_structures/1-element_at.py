def element_at(my_list, idx):
    n = len(my_list)
    if idx < 0 or idx > n-1:
        return (None)
    else:
        print("{:d}".format(my_list[idx]))
