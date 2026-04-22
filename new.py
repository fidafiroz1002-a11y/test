

class Shape:
    def area(self):
         print("area not defined")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("the area of rectangle is: ", self.length * self.width)
        
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("the area of circle is: ", 3.14 * self.radius * self.radius)

r= Rectangle(18,5)
c= Circle(7)
r.area()
c.area()
