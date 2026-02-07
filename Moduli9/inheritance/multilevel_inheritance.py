#multilevel eshte terashigimi ku klasa 2 merr prej te 1 dhe klasa 3 merr prej 2 po i bie qe te marr edhe te 1
class Vehicle:
    def __init__(self,make,model,year): #konstruktori i klases eshte init
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

class Car(Vehicle):
    def __init__(self,make,model,year,body_style):
       super().__init__(make,model,year)
       self.body_style = body_style

class ElectricCar(Car):
    def __init__(self,make,model,year,body_style,battery_capacity):
        super().__init__(make,model,year,body_style)
        self.battery_capacity = battery_capacity

    def charge(self):
        print("Charging the Electric Car")

tesla = ElectricCar("Tesla","Cybertuck","2023","triangular","122.3")
tesla.charge()
tesla.display_info()
print("Body style:",tesla.body_style)
print("Battery Capacity:",tesla.battery_capacity)


