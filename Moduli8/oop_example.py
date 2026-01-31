#oop perdor class per kod me te menagjushem class ka atribute dhe metoden
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


my_rectangle = Rectangle(2, 5)

area_calculated = my_rectangle.calculate_area()
perimeter_calculated = my_rectangle.calculate_perimeter()

print(f"The area of the rectangle is {area_calculated}")
print(f"The perimeter of the rectangle is {perimeter_calculated}")
