import math


print("Welcome to calculator, shortly you will be asked to enter two numbers, and an operator. Please comply with it :)")
x = float(input("Num One: "))
y = float(input("Num Two: "))
op = input("Operator:")
if op == "/" and y == 0.0:
    print("Divide by zero error")
elif y != 0.0:
    if op == "/":  
        print(x/y)




if op == "x":
    print(x*y)



if op == "+":
    print(x+y)

if op == "-":
    print(x-y)

if op == "^":
    print(x^y)
if op == "sq":
    print(x**2)
if op == "sqrt":
    print(math.sqrt(x))