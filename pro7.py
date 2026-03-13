# Write a program to create a list and perform various operations on list using menu.

my_list = []

while True:
    print("\n---- LIST OPERATIONS MENU ----")
    print("1. Create List")
    print("2. Display List")
    print("3. Insert Element")
    print("4. Delete Element")
    print("5. Search Element")
    print("6. Sort List")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter number of elements: "))
        my_list = []
        for i in range(n):
            val = input("Enter element: ")
            my_list.append(val)
        print("List created successfully")

    elif choice == 2:
        print("List elements are:", my_list)

    elif choice == 3:
        pos = int(input("Enter position: "))
        val = input("Enter value to insert: ")
        my_list.insert(pos, val)
        print("Element inserted")

    elif choice == 4:
        val = input("Enter element to delete: ")
        if val in my_list:
            my_list.remove(val)
            print("Element deleted")
        else:
            print("Element not found")

    elif choice == 5:
        val = input("Enter element to search: ")
        if val in my_list:
            print("Element found at position", my_list.index(val))
        else:
            print("Element not found")

    elif choice == 6:
        my_list.sort()
        print("List sorted")

    elif choice == 7:
        print("Exiting program")
        break

    else:
        print("Invalid choice, try again")
