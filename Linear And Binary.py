j = int(input("Enter which method you want to use (1: Binary, 2: Linear): "))

# Binary Search
if j == 1:
    l = []

    n = int(input("Enter number of elements: "))

    for i in range(n):
        e = int(input("Enter an element: "))
        l.append(e)

    l.sort()
    print("Sorted list:", l)

    key = int(input("Enter the element you want to find: "))

    low = 0
    high = len(l) - 1

    while low <= high:
        mid = (low + high) // 2

        if key == l[mid]:
            print("Found at position:", mid + 1)
            break

        elif key < l[mid]:
            high = mid - 1

        else:
            low = mid + 1

    else:
        print("Element not present in list")


# Linear Search
elif j == 2:
    n = int(input("Enter the number of customers: "))

    Id = []

    for i in range(n):
        id = int(input("Enter customer ID: "))
        Id.append(id)

    key = int(input("Enter Account ID to Search: "))

    for i in range(len(Id)):
        if Id[i] == key:
            print("Found at position:", i + 1)
            break

    else:
        print("Not Found")


# Invalid choice
else:
    print("Invalid choice! Please enter 1 or 2.")
