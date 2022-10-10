def greet_user(First_name, last_name):
    print(f'Hi {First_name} {last_name}!')
    print('Welcome aboard')

print("Start")
greet_user(last_name="Ade", First_name="Snow")
print("Finish")
'''
:parameter are the items we supply withing our function declaration
while arguments are the actual value we input into our function at the call of our function call
In python we have both positional and keyword argument
In positional argument the position of the argument we passed matters
In keyword argument we equate the specific arguments directory to the parameter at the call of our function
while dealing with functions with multiple argument it is good to use keywoord argument for readability.
Also we can have combined usage where positional argument must come first
'''

