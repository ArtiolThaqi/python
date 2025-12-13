greeting = "Hello"

def greet(name):
    #Deklarojme mesazhin si variabel globale me funksionin global
    global message
    message = f"{greeting} {name}"
    print(message)

greet("Bob")
print(message)

message = f"{greeting}, student"
print(message)
