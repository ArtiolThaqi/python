class Person:
    def __init__(self, name, age): #atributet
        self.name = name
        self.age = age

    def greet(self): #metoda
        print(f"Hello, I am {self.name}, my age is {self.age} years old")

person1 = Person("Bob", 18)
person2 = Person("Alice", 20)
person1.greet()
person2.greet()
#accessmodifires eshte pjesa me aksesu ajo eshte private publike protected