#Write a program to create 4 lambda functions which shall accept 2 numbers and one arithmetic operator. As per arithmetic operator related lambda functions shall be invoked.

add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: x / y if y != 0 else "Division by zero not allowed"

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    result = add(a, b)

elif op == '-':
    result = sub(a, b)

elif op == '*':
    result = mul(a, b)

elif op == '/':
    result = div(a, b)

else:
    result = "Invalid operator"

print("Result:", result)
