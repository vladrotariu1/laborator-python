# 1)
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.insert(len(self.stack), item)

    def pop(self):
        if not self.is_empty():
            val = self.stack[len(self.stack) - 1]
            self.stack = self.stack[:-1]
            return val
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[len(self.stack)-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


def main():
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    while not stack.is_empty():
        print(stack.peek())
        print(stack.pop())

    print(stack.peek())
    print(stack.pop())


if __name__ == "__main__":
    main()
