import math
from abc import ABC, abstractmethod

class Shape (ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi*self.radius**2

class Square(Shape):
    def __init__(self,length):
        self.length = length
    def area(self):
        return self.length**2

square = Square(2)
print(square.area())

circle = Circle(7)
print(circle.area())
