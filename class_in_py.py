'''
We use class to define new type
We use class.
Also we use pascal naming convention, we capitalize each word
with each class we can define a type or method and with each type we can define a new object.
'''

class Point:
    def move(self):
        print('move')

    def draw(self):
        print('draw')

#to create object

point1 = Point()
#object can have attribute
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)