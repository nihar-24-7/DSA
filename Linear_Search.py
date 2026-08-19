n=int(input("Enter no. of ids : "))
list=[]
for i in range (n):
    element=int(input(f"Enter id {i+1} : "))
    list.append(element)
print("Customer ids : ",list)

check=int(input("Enter id to search : "))
for i in range (n) :
    if list[i]==check:
        print("Available at postion ",i+1)
        break;
if list[i]!=check :
    print("Not Available")
