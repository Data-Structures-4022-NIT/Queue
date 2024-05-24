class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        self.queue.append((item, priority))
        self.queue.sort(key=lambda x: x[1])

    def dequeue(self):

        if self.is_empty():
            raise IndexError("Dequeue from empty priority queue")
        return self.queue.pop(0)[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


# Example usage:
pq = PriorityQueue()
print("Is the priority queue empty?", pq.is_empty())  # Output: True

pq.enqueue('task1', 3)
pq.enqueue('task2', 1)
pq.enqueue('task3', 2)

print("Priority queue size:", pq.size())  # Output: 3
print("Is the priority queue empty?", pq.is_empty())  # Output: False

print("Dequeued item:", pq.dequeue())  # Output: 'task2' (highest priority)
print("Priority queue size after dequeue:", pq.size())  # Output: 2
