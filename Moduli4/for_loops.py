names = ['Alice', 'Bob', 'David','Charlie']
for name in names:
    print(name)

sentence = 'Hello World'
for letter in sentence:
    print(letter)

#Range printon te dhenat duke fillu nga 0
for number in range(6):
    print(number)

numbers = [12,45,6,7,94,304,34]

max = numbers[0]#12

for number in numbers:
    if number > max:
        max = number#304
print('Maksimumi eshte:',max)

count = 1
while count <= 5:
    print("Rrite vleren per nje",count)
    count += 1

#Target gjen numrin qe na e caktojm
#Break e nal kodin
numbers = [1,2,3,4,5,6]
target =4
for number in numbers:
    print(number)
    if number == target:
        print("Target found",target)
        break

scores = [68, 42, 57, 86, 73, 50, 92, 30]
total = 0
count = 0

for score in scores:
    if score < 50:
        continue
    total += score
    count += 1

mesatarja = total / count
print("Mesatarja ka qene:", mesatarja)


#Do while loop niher egzekuton kodin me pas kushtin
#input funksioni qe useri mundet me shtyp diqka
while True:
    user_input = input("Shtyp nje numer pozitiv: ")
    if user_input.isnumeric():
        number = int(user_input)
        if number > 0:
            break
    print("Invalid. Try again")
print("You enter a positive number")


