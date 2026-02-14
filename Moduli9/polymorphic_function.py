def add(x,y):
    return x+y
def concatenate(x,y): #concatenate i bashkon dy stringje
    return str(x) + str(y)
def operate(operation,x,y):
    return operation(x,y)

result_sum = operate(add,3,5)
result_concatenate = operate(concatenate,"Hello","World")
print("Result of concatenate",result_concatenate)
print("Result of sum",result_sum)
