class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

def josephus(n, k):
    q = Queue()
    for i in range(1, n + 1):
        q.enqueue(i)

    while q.size() > 1:
        for _ in range(k - 1):
            q.enqueue(q.dequeue())
        q.dequeue()  # This is the k-th person to be eliminated

    return q.dequeue()

def main():
    n = int(input("Enter the number of participants (n): "))
    k = int(input("Enter the number of participants to skip (k): "))
    result = josephus(n, k)
    print(f"The last remaining person is at position: {result}")

if __name__ == "__main__":
    main()
