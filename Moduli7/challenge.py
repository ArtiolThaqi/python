def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        raise ValueError("Invalid operator")

try:
  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))
  operator = input("Enter an operator:(+,-,*,/): ")
  result = calculate(num1, num2, operator)
  print(f"The result of {num1} {operator} {num2} is:",result)
except ValueError as e:
    print(f"Invalid input:{e}")
except ZeroDivisionError as e:
    print("Cannot divide by zero")
except Exception as e:
    print(f"Unexpected error occurred: {e}")
finally:
    print("End of the program")