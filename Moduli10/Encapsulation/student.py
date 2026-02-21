class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self): #get_name eshte metode e enkapspulimit qe perdoret me iu qase variablave private
        return self.__name

    def set_name(self, name): #metoda set perdort kur dojm mi ndyshu te dhenat e nje variable te caktuar
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age


student1 = Student("Alice", 17)
print("Name:",student1.get_name())
print("Age:",student1.get_age())

student1.set_name("Bob")
print("Updated Name:",student1.get_name())

student1.set_age(20)
print("Updated Age:",student1.get_age())

