stack = []  # Initialize an empty stack

def push():
    item = input("Enter the item to push: ")
    stack.append(item)
    print("Item pushed successfully!")

def pop():
    if len(stack) == 0:
        print("Stack is empty!")
    else:
        item = stack.pop()
        print("Popped item:", item)

def display():
    if len(stack) == 0:
        print("Stack is empty!")
    else:
        print("Stack elements:")
        for i in range(len(stack)-1, -1, -1):  # Print from top to bottom
            print(stack[i])

while True:
    print("\nMenu:")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        push()
    elif choice == "2":
        pop()
    elif choice == "3":
        display()
    elif choice == "4":
        break
    else:
        print("Invalid choice!")

print("Exiting program...")
