# Write a program to input p, r, n and find out interest using simple input output statement.

p = float(input("Enter Principal amount (P): "))
r = float(input("Enter Rate of Interest (R): "))
n = float(input("Enter Time in years (N): "))

simple_interest = (p * r * n) / 100

print("Simple Interest is:", simple_interest)
