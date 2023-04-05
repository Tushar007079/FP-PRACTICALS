class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("Stack: ", self.items)

s = Stack()

while True:
    print("****************")
    print("|  1. Push     |")
    print("|  2. Pop      |")
    print("|  3. Peek     |")
    print("|  4. Display  |")
    print("|  5. Quit     |")
    print("****************")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter the item to be pushed: ")
        s.push(item)
    elif choice == 2:
        if s.is_empty():
            print("Stack is empty!")
        else:
            print("Popped item: ", s.pop())
    elif choice == 3:
        if s.is_empty():
            print("Stack is empty!")
        else:
            print("Top item: ", s.peek())
    elif choice == 4:
        s.display()
    elif choice == 5:
        break
    else:
        print("Invalid choice!")
