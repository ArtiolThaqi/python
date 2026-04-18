from abc import ABC, abstractmethod
import streamlit as st


class Person(ABC):
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self._weight = weight
        self._height = height

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
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


# ===== STREAMLIT APP =====
st.title("BMI Calculator")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=0, max_value=120, value=25)
weight = st.number_input("Enter your weight (kg)", min_value=0.0, value=70.0)
height = st.number_input("Enter your height (m)", min_value=0.0, value=1.75)

if st.button("Calculate BMI"):
    if age >= 18:
        person = Adult(name, age, weight, height)
    else:
        person = Child(name, age, weight, height)

    bmi = person.calculate_bmi()
    category = person.get_bmi_category()

    st.success(f"Name: {name}")
    st.write(f"BMI: {bmi:.2f}")
    st.write(f"Category: {category}")