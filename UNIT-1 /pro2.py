#Write a program to input 2 numbers and one arithmetic operator. Perform operations as per arithmetic operator which is given as input

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operator = input("Enter an operator (+, -, *, /): ")

if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed")
else:
    print("Invalid operator")
