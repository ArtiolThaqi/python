#class protected definohet me ni underline eshte e krijuar per te qen ne nje funksion por ban edhe jashta funksionit por me kujdes pasi eshte delikate
class Square:
    def __init__(self):
        self._length ="this variable is with length 5"
    def area(self):
        return self._length * self._lengt

square = Square()
print(square._length)