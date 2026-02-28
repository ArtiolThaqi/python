with open('example.txt','r') as file:
    for line in file:
        cleaned_lines = line.strip() # remove whitespaces
        print(cleaned_lines)

#splitting lines into words i ndan fjalt
with open('example.txt','r') as file:
    for line in file:
       words = line.strip().split()
       print(words)

name = "Alice"
age = 20
with open('output.txt','w') as file:
    file.write("Name:" + name + "\n")
    file.write("Age:" + str(age) + "\n")