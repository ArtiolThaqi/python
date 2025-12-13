greeting = "Hello"
name = "Bob"
def greet():
     global greeting
     name = "Alice"
     message = f"{greeting}, {name}!"
     print(message)
greet()
#Te pjesa par printohet mesazhi por pa emrin e bob se nuk eshte brenda funksionit te pjesa dyt printohet greeting dhe name qe jan jashta funkionit

print(greeting)
print(name)