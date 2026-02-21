#private i ka dy underline perpara si psh te rreshti 4
#variablat private smunesh  mju qas jashte funskionit
class MyClass:
    def __init__(self):
        self.__private_variable = "This is a private variable"

    def __private_method(self):
        print("This is a Private method")

my_class = MyClass()
print(MyClass.__private_variable)
print(MyClass.__private_method())