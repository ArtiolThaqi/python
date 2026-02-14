class Dog:
    def __init__(self,name):
     self.name = name

    def sound(self):
          print(f"{self.name} makes the sound:WOOF!")

class Cat:
    def __init__(self,name):
        self.name = name
        def sound(self):
         print(f"{self.name} makes the sound:MEOW!")

class Bird:
    def __init__(self,name):
        self.name = name
        def sound(self):
            print(f"{self.name} makes the sound:CHIRP!")

dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweetie")


for animal in ["Dog","Cat","Bird"]:
    animal.sound()


