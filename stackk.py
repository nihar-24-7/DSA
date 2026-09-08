stack = []
MAX = 5
#PUSH
print("Push Operation in Stack")
def push(value):
    if len(stack) == MAX:
        print("Stack Overflow")
    else:
        stack.append(value)
        print(value, "pushed into stack")

n = int(input("Enter number of values: "))

for i in range(n):
    value = int(input("Enter value: "))
    push(value)

print("Stack:", stack)

#POP
def pop():
    if len(stack) == 0:
        print("Stack Underflow")
    else:
        value = stack.pop()
        print(value, "popped from stack")



print("Stack:", stack)

pop()

print("Stack after pop:", stack)

#PEEK
def peek():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Top element:", stack[-1])

peek()

#DISPLAY
def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack elements:")
        for i in range(len(stack) - 1, -1, -1):
            print(stack[i])

display()

#isEmpty
def isEmpty():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack is not empty")

isEmpty()

#isFull
# isFull
def isFull():
    if len(stack) == MAX:
        print("Stack is full")
    else:
        print("Stack is not full")

        