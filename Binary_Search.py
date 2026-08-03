num=int(input("Enter number of Elements :  "))
list=[]
for i in range (num):
    element=float(input(f"Enter number {1+i} : "))
    list.append(element)
print("User's List")
print(list)
list.sort()
print("Sorted User's list")
print(list)

key=float(input("Enter the specific number to find : "))
low=0
high=num-1
while low<=high:
    mid=int((low+high)/2)
    if key == list[mid]:
        print("Found at position", mid+1)
        break
    elif key<=list[mid]:
        high = mid -1
    elif key>=list[mid]:
        low = mid+1
    else:
        print("Not Found")
    
