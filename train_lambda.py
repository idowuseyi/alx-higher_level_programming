#operations with functions
def mul_ti_2(num):
    return num * 2

times_two = mul_ti_2(4)
print(times_two)

def do_math(func, num):
    return func(num)

print("8 * 2 =", do_math(mul_ti_2, 8))

# dynamically created function inside a function

def get_func_mult_by_num(num):

    def mult_by(value):
        return num * value

    return mult_by

generated_func = get_func_mult_by_num(5)

print("5 * 10 =", generated_func(10))

# return a function within a data structure

listoffuncs = [times_two, generated_func]
print("5 * 9 =", listoffuncs[1](9))



