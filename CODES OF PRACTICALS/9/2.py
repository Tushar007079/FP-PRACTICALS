class Stack:
    def __init__(self, size):
        self.S = []
        self.size = size

    def push(self, data):
        if (len(self.S) < self.size):
            self.S.append(data)
        else:
            print("Stack is Full! [OVERFLOW]")

    def pop(self):
        try:
            return self.S.pop()
        except IndexError:
            print("Stack is Empty! [UNDERFLOW]")

    def peek(self):
        return self.S[len(self.S)-1]

    def display(self):
        print(self.S)
S = Stack(3)
S.push(0)
S.push(0)
S.push(7)
S.display()
print("Elements of TOS : ", S.peek())
S.push(4)
print("Element Popped : ", S.pop())
S.display()
