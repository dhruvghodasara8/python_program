#Write a program to create a function which accepts 2 numbers and one arithmetic operator. Return the answer accordingly.

def calculate(num1, num2, operator):
    
    if operator == '+':
        return num1 + num2
    
    elif operator == '-':
        return num1 - num2
    
    elif operator == '*':
        return num1 * num2
    
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Division by zero is not allowed"
    
    elif operator == '%':
        return num1 % num2
    
    else:
        return "Invalid operator"

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /, %): ")

result = calculate(a, b, op)

print("Result:", result)
