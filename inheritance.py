'''
Inheritance is a way of reusing code. It is mostly applied anywhere we have class
DRY: Dont repeat yourself. In programing we dont define things twice
'''
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")

class Cat(Mammal):
    def be_annoying(self):
        print("annoying")


dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.be_annoying()