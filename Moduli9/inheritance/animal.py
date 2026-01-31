#superclass o classa kryesore,classa baz primare si psh baba
#subclass o classa dytsore qe merr te dhenat nga supperclassa pra i trashigon si psh djali

class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Woof! Woof! Woof!")

class Cat(Animal):
    def sound(self):
        print("Meow! Meow! Meow!")

animal = Animal()
animal.sound()

#objektet jan met vogla e meotda eshte .sound
dog = Dog()
dog.sound()
cat = Cat()
cat.sound()
