#TRY AND EXCEPT BLOCK
#try jep paralajmrim por nuk e ndalon kodin
#try except perdoren kur nuk jemi te sigurt se ae kemi nje antar te caktuar

try:

    result = 10/0
except  ZeroDivisionError:
    print("OOPS! Tried to divide by zero!")

fruits = {
    "apple":5,
    "banana":7,
    "orange":3,
}
print(fruits["orange"])

try:
  print(fruits["cherry"])
except KeyError:
  print("The key does not exist in the directory")

text = "This is not a number"
try:
    text_to_int = int(text)
except Exception as e:  #Exception perfshine te gjitha erroret pra kur sjemi te sigurt qfar errori eshte e perdorum Exception
    print("An error occured while parsing data:",e)

#ELSE BLOCK
#Else egzekutohet qdo here nese kodi nuk gjen error
try:
    result = 10/5
except ZeroDivisionError:
       print("OOPS! Tried to divide by zero!")
else:
  print("Division successful.Result:", result)

#FINALLY BLOCK

try:
    result = 10/0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Finally block executed")

#Exercise

def divide_numbers(a,b):
  try:
     result = a / b
     print("Result division",result)
  except ZeroDivisionError:
   print("Cannot divide by zero!")
  except TypeError:
    print("Invalid type")
  except Exception as e:
    print(f"Unexcepted error,{e}")

divide_numbers(10,2)
divide_numbers(10,0)
divide_numbers(10,"2")