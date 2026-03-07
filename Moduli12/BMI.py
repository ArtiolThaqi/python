from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self._weight = weight
        self._height = height

    @property
    def weight(self):   # përdoret për të lexuar weight sepse është private
        return self._weight

    @weight.setter
    def weight(self, value):   # përdoret për të ndryshuar weight
        if value < 0:
            raise ValueError("Weight must be positive")
        self._weight = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("Height must be positive")
        self._height = value

    @abstractmethod
    def calculate_bmi(self):
        pass

    @abstractmethod
    def get_bmi_category(self):
        pass

    def print_info(self):
        print(f"{self.name}, Age: {self.age}, Weight: {self._weight} kg, Height: {self._height} m, "
              f"BMI: {self.calculate_bmi():.2f}, Category: {self.get_bmi_category()}")


class Adult(Person):
    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def get_bmi_category(self):
        bmi = self.calculate_bmi()

        if bmi <= 18.5:
            return "Underweight"
        elif bmi <= 24.9:
            return "Normal weight"
        elif bmi <= 29.9:
            return "Overweight"
        else:
            return "Obese"


class Child(Person):
    def calculate_bmi(self):
        return (self.weight / (self.height ** 2)) * 1.3

    def get_bmi_category(self):
        bmi = self.calculate_bmi()

        if bmi <= 14:
            return "Underweight"
        elif bmi <= 18:
            return "Normal weight"
        elif bmi <= 24:
            return "Overweight"
        else:
            return "Obese"


class BMIapp:
    def __init__(self):
        self.people = []

    def add_people(self, person):
        self.people.append(person)

    def collect_user_data(self):
        name = input("Please enter your name: ")
        age = int(input("Please enter your age: "))
        weight = float(input("Please enter your weight: "))
        height = float(input("Please enter your height: "))

        if age >= 18:
            person = Adult(name, age, weight, height)
        else:
            person = Child(name, age, weight, height)

        self.add_people(person)

    def print_results(self):
        print("\n--- BMI RESULTS ---")
        for person in self.people:
            person.print_info()

    def run(self):
        while True:
            self.collect_user_data()
            cont = input("Would you like to add another person? (yes/no) ").strip().lower()

            if cont != "yes":
                break

        self.print_results()


# Run the application
app = BMIapp()
app.run()