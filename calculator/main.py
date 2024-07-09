"""import os
from art import logo
print(logo)
def sum(a,b):
    return a +b
def div (a,b):
    return a/b
def mul(a,b):
    return a*b
def min(a,b):
    return a-b

def oper(a,b,o):
    if o=="+":
        return sum(a,b)
    elif o=="-":
        return min(a,b)
    elif o=="*":
        return mul(a,b)
    elif o=="/":
        return div(a,b)
a= float(input("what is the first number?: ")) 
o=input("+\n-\n*\n/\nPick an operation")    
b= float(input("what is the second number?: "))
result=oper(a,b,o)
print(f"{a} {o} {b} = {result}")
test=True
while test == True:
    
    
    check=input(f"Type y to continue with {result} n to start over")
    if check=="y":
        a=result
        o=input("+\n-\n*\n/\nPick an operation")    
        b= float(input("what is the second number?: "))
        result=oper(result,b,o)
        print(f"{a} {o} {b} = {result}")
    elif check=="n":
        os.system('cls')
        print(logo)
        a= float(input("what is the first number?: ")) 
        o=input("+\n-\n*\n/\nPick an operation")    
        b= float(input("what is the second number?: "))
        result=oper(a,b,o)
        print(f"{a} {o} {b} = {result}")
"""
#=====>>>>>>>> the dectionary will return funktion that i can use later
#op={
#    "+":sum,
#    "-":min,
#    "*":mul,
#    "/":div
#}



import os

from art import logo


def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("what is the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      os.system('cls')
      calculator()

calculator()