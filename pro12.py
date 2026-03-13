#Write a program to display the use of local, global and nonlocal variables

x = 10

def display():

    y = 20
print("Inside display() function:")
print("Global variable x =", x)
print("Local variable y =", y)

def outer():
    z = 30

    def inner():
        nonlocal z
        z = 40
        print("\nInside inner() function:")
        print("Nonlocal variable z =", z)

    inner()
    print("Value of z in outer() after inner() call =", z)


