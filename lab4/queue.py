# 2)
class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.insert(len(self.queue), item)

    def pop(self):
        if not self.is_empty():
            item = self.queue[0]
            self.queue = self.queue[1:]
            return item
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None

    def is_empty(self):
        return  len(self.queue) == 0

    def size(self):
        return len(self.queue)


def main():
    queue = Queue()

    queue.push(1)
    queue.push(2)
    queue.push(3)

    while not queue.is_empty():
        print(queue.peek())
        print(queue.pop())

    print(queue.peek())
    print(queue.pop())


if __name__ == "__main__":
    main()
