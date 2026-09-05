class Vehicle:
    def __init__(self, make,model,year_of_production):
        self.make = make
        self.model = model
        self.year_of_production = year_of_production

    def __repr__(self):
        return f" Make: {self.make}, Model: {self.model}, Year: {self.year_of_production}"

class Car(Vehicle):
    def __init__(self,make,model,year_of_production, color):
        super().__init__(make, model, year_of_production)
        self.color = color

    def __repr__(self):
        return f'super().__repr__(), Color: {self.color}'

class ElectricCar(Vehicle):
    def __init__(self,make,model,year_of_production,battery_capacity):
        super().__init__(make,model,year_of_production)
        self.battery_capacity = battery_capacity

        def battery_charging(self)->None:
            print("Charging the Electric Car:",self.battery_capacity)

        def __repr__(self):
            return f'This is an Electric Car: {super().__repr__()}.'

def main():
    tesla:ElectricCar = ElectricCar('Tesla','model X',2016,600)
    tesla.battery_charging()
    print(tesla)
    vw:Car = Car('VW','Tiguan',2016, Black)
    print(vw)

if __name__ == '__main__':
    main()