class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):

        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Example usage:
q = Queue()
print("Is the queue empty?", q.is_empty())  # Output: True

q.enqueue('a')
q.enqueue('b')
q.enqueue('c')


print("Queue size:", q.size())  # Output: 3
print("Is the queue empty?", q.is_empty())  # Output: False

print("Dequeued item:", q.dequeue())  # Output: 'a'
print("Queue size after dequeue:", q.size())  # Output: 2
