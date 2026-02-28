#file_path = "example.txt" kjo o metoda par perdoret ma pak se duhet gjithmone me mbyll filen e hapur
#file = open(file_path,"r")
#content = file.read()
#print(content)
#file.close()
import os

file_path = "example.txt" #metoda dyt perdoret ma shum pasi nuka nevoje me mbyll filen
with open(file_path,"r") as file:
    content = file.read()
    print(content)

#Files mode:
# 'r' - read mode
# 'w' - write shton nje fjal qe kemi zgjedhur por zevendson komplet tekstin dhe e le veq at fjal
# 'a' - append  Shton nje fjal qe e kemi zgjedhur duke mos zevendsuar asgjee veqq shtohet
# 'binary' - binary mode

with open(file_path,"r") as file:
    content = file.read() # lexon kejt kontentin
    line = file.readline() # lexon veq nje rresht
    lines = file.readlines() # lexon krejt rreshtat ne nje list


#Writing to files
with open(file_path,"w") as file:
    file.writelines("Today is saturday")

lines1 = ['Hello World \n','Welcome to Python \n']
with open(file_path,"w") as file:
    file.writelines(lines1)

#Moving the Cursor
with open(file_path,"r") as file:
    file.seek(0) #moves the cursor to the begining of the file
    data = file.read()
    print(data)

#Checking file existence
if os.path.exists('example.txt'): #metode qe me dit a egzistion nje file si psh. file example.txt
    print('file exists')

with open(file_path,"a") as file:
    file.write("U shtu rreshti ri")


#Reading and writing binary files
data = b'This is some binary data'
with open('example.bin',"wb") as file:
    file.write(data)

with open('example.bin',"rb") as file:
    data = file.read()
    print(data)
