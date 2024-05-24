class CircularQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * max_size
        self.front = 0
        self.rear = 0
        self.count = 0

    def enqueue(self, item):
        if self.count == self.max_size:
            print("Queue is full")
            return
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.max_size
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            print("Queue is empty")
            return None
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.max_size
        self.count -= 1
        return item

    def is_empty(self):
        return self.count == 0

    def size(self):
        return self.count

# Example usage:
cq = CircularQueue(5)
print("Is empty?", cq.is_empty())  # Is empty? True
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
print("Size:", cq.size())  # Size: 3
print("Dequeue:", cq.dequeue())  # Dequeue: 1
print("Size:", cq.size())  # Size: 2
cq.enqueue(4)
cq.enqueue(5)
cq.enqueue(6)  # Queue is full
print("Is empty?", cq.is_empty())  # Is empty? False
print("Size:", cq.size())  # Size: 5
