# Working with Common Data Structures
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else None

    def peek(self):
        return self.items[-1] if self.items else None

    def is_empty(self):
        return len(self.items) == 0

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0) if self.items else None

    def is_empty(self):
        return len(self.items) == 0

s = Stack()
s.push(1); s.push(2); s.push(3)
print(s.pop(), s.pop())

q = Queue()
q.enqueue("a"); q.enqueue("b")
print(q.dequeue(), q.dequeue())
