def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
choice=input("ENTER WHICH OPERATION YOU WANT TO PERFORM, ADD, SUBTRACT, MULTIPLY OR DIVIDE: ")
num1=int(input("ENTER THE FIRST NUMBER: "))
num2=int(input("ENTER THE SECOND NUMBER: "))
if choice=="add":
    print("THE SUM OF", num1,"and", num2,"is", add(num1,num2))
elif choice=="subtract":
    print("THE SUBTRACTION OF", num1,"and", num2,"is", subtract(num1,num2))
elif choice=="multiply":
    print("THE MULTIPLICATION OF", num1,"and", num2,"is", multiply(num1,num2))
elif choice=="divide":
    print("THE DIVISION OF", num1,"and", num2,"is", divide(num1,num2))
else:
    print("invalid input")