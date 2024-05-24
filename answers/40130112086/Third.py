class CircularQueue:

    #Initialize an empty circular queue with a maximum size.
    def __init__(self, max_size):
        self.max_size = max_size #size
        self.queue = [None] * max_size
        self.front = 0
        self.rear = 0
        self.num_items = 0

    #Add an item to the rear of the circular queue.
    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.max_size
        self.num_items += 1

    #Remove and return the front item from the circular queue.
    def dequeue(self):
        if self.is_empty():
            return None
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.max_size
        self.num_items -= 1
        return item

    #Check if the circular queue is empty.
    def is_empty(self):
        if self.num_items == 0:
            return True
        else:
            return False

    #Check if the circular queue is  full
    def is_full(self):
        if self.num_items == self.max_size:
            return True
        else:
            return False

    #Return the number of elements in the circular queue.
    def size(self):
        return self.num_items
