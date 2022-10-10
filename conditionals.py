#conditional helps in decision
'''
is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear something warm")
else:
    print("It's a lovely day")
print("Enjoy your day")
'''
'''
price = 1000000

good_credit_buyer = True

print("Your down payment is: ")
if good_credit_buyer:
    print(f"${price*(10/100)}")
else:
    print(f"${price*(20/100)}")
'''

has_high_income = True
has_good_credit = True

#logical operators

if has_high_income and has_good_credit:
    print("Eligible for loan")
if has_high_income or has_good_credit:
    print("Eligible for loan")
if has_high_income and not has_good_credit:
    print("Eligible for loan")
# Comparism Operator

temperature = 30

if temperature > 30:
    print("It's a hot day")
elif temperature == 30:
    print("It's a good day")
else:
    print("It's not a hot day")