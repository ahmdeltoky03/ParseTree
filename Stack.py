class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def printStack(self):
        print(self.items)

# stack = Stack()
# stack.push(3)
# stack.push(4)
# stack.push(5)
# stack.push(6)
# stack.push(7)
#
# print(stack.isEmpty())
# stack.printStack()
# stack.pop()
# stack.printStack()
# stack.pop()
# stack.printStack()
# print(stack.peek())
# stack.printStack()
# stack.pop()
# print(stack.peek())
# stack.printStack()
# stack.pop()
# stack.pop()
# stack.printStack()
# print(stack.isEmpty())
