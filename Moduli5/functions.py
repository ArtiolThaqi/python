def greet():
    print("Hello World")

greet() #greet eshte funksion i thjeshte me printu te dhena

def greet_person(name):
    print("Hello " + name)
greet_person("Alice") #greet nuk printohet pa e thirr edhe niher edhe nese e bajm print
greet_person("Bob")
greet_person("Carol")

'''
def add(x,y):
 z = x + y
 return z
add(3,7)
'''
def add(x,y):
 z = x + y
 return z
result = add(3,7)
print("The result of 3 + 7 is = ",result)