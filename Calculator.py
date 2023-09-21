def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

while True:
    print("Options:")
    print("Enter '+' for addition")
    print("Enter '-' for subtraction")
    print("Enter '*' for multiplication")
    print("Enter '/' for division")
    print("Enter 'end' to end the program")
    UserInput = input(": ")

    if UserInput == "end":
        break
    elif UserInput not in ("+", "-", "*", "/"):
        print("Invalid input")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if UserInput == "+":
        print("Result:", add(num1, num2))
    elif UserInput == "-":
        print("Result:", subtract(num1, num2))
    elif UserInput == "*":
        print("Result:", multiply(num1, num2))
    elif UserInput == "/":
        print("Result:", divide(num1, num2))
