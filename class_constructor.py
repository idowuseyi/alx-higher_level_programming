'''
We can use constructor function to define what happens when our class is called
a class is also called a type
'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')


point = Point(10, 20)
print(point.x)


'''
class class
#for a method
    def __init__(self, name):
        self.name = name
        
        
    def method():
        body
'''
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("John Smith")
id = Person("Oluwaseyi Idowu")
john.talk()
id.talk()