import math


class Shape:
    def __init__(self, l=0, w=0, r=0):
        self.length = l
        self.width = w
        self.radius = r

    def perimeter(self):
        if self.radius == 0:
            print("Perimeter :", (self.length + self.width) * 2)
        else:
            print("Perimeter :", self.radius * 2 * math.pi)

    def area(self):
        if self.radius == 0:
            print("Area :", self.length * self.width)
        else:
            print("Area :", (self.radius ** 2) * math.pi)


circle = Shape(r=4)
rectangle = Shape(l=3, w=7)

rectangle.area()
rectangle.perimeter()
circle.area()
circle.perimeter()
