class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, val):
        self.data.insert(0, val)

    def dequeue(self):
        if len(self.data) > 0:
            return self.data.pop()
        return "Queue is Empty"

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return len(self.data) == 0

    def peek(self):
        if not self.isEmpty():
            return self.data[-1]
        return "Queue is Empty"
