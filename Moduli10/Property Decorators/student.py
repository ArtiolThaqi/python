class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

#property eshte get
    @property
    def name(self): #get_name eshte metode e enkapspulimit qe perdoret me iu qase variablave private
        return self.__name
#setter eshte set
    @name.setter
    def name(self, name): #metoda set perdort kur dojm mi ndyshu te dhenat e nje variable te caktuar
        self.__name = name
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.__age = age

student1 = Student("Alice", 17)
print("Name:",student1.name)
print("Age:",student1.age)

student1.name = "Bob"
print("Updated Name:",student1.name)

student1.age = 30
print("Updated Age:",student1.age)
