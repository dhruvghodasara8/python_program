#Write a program to create function which shall accept any number of arguments and display total of all the numbers given as argument.

def find_total(*numbers):
    total = 0
    for num in numbers:
        total += num
    print("Total =", total)

find_total(10, 20, 30)
find_total(5, 15, 25, 35, 45)
