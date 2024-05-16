class Stack:

    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def __bool__(self):
        return bool(self.stack)

    def clear(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

# Create an instance of the Stack class
stack = Stack()

# Push items onto the stack
stack.push(5)
stack.push(10)

# Peek at the top item of the stack
print(stack.peek())  # Output: 10