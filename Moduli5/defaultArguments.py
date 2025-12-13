def greet_person(name, greeting="Hello"):
    message = f"{greeting}, {name}!"
    return message
default_greeting = greet_person("Alice")
print(default_greeting)
#Te rasti i par e kemi permbush vetem parametrin e emrit per ket shkak printohet dhe paramtra e greeting Hello
custom_greeting = greet_person("Alice", "Hi")
print(custom_greeting)
#Te rasti dyt i kemi permbush dy paramterat per ket shkak printohet me qfardo greeting qe deshirojm si pershemmbull Hi