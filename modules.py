'''
we use module to section our code. Just like sectioning in a supermarket
we use it to break our code into multiple sections
'''

#we can import the entire module
import converters
#or specific module
from converters import kg_to_lbs
kg_to_lbs(100)
print(converters.kg_to_lbs(70))