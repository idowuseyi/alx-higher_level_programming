# This program takes user input weight and convert it to the other unit

weight = int(input('Input your weight: '))

weight_unit = input("(L)bs or (K)g: ")

if weight_unit.upper() == "L":
    converted = weight / 2.2
    print(f"You are {converted} kilos ")
elif weight_unit.upper() == "K":
    converted = weight * 2.2
    print(f"You are {converted} pounds")
else:
    print("Input the right weight unit")