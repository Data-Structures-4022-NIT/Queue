class CircularQueue:
    def __init__(self, max_size):
        self.max_size = max_size  # Maximum size of the queue
        self.CircleQ = [None] * max_size  # Initialize the queue with None values
        self.rear = 0  # Index for the rear end of the queue
        self.front = 0  # Index for the front end of the queue
        self.size = 0  # Current number of elements in the queue
    
    def enqueue(self, item):
        # Add an item to the queue
        if self.size == self.max_size:
            return "Overflow"  # Queue is full
        else:
            self.CircleQ[self.rear] = item  # Place the item at the rear end
            self.rear = (self.rear + 1) % self.max_size  # Move rear to the next position
            self.size += 1  # Increment the size of the queue

    def dequeue(self):
        # Remove an item from the queue
        if self.isEmpty():
            return "Queue is empty"  # Queue is empty
        else:
            item = self.CircleQ[self.front]  # Get the item at the front end
            self.CircleQ[self.front] = None  # Clear the spot
            self.front = (self.front + 1) % self.max_size  # Move front to the next position
            self.size -= 1  # Decrement the size of the queue
            return item  # Return the dequeued item
            
    def isEmpty(self):
        # Check if the queue is empty
        return self.size == 0  # True if size is 0, else False

    def SizeOfQueue(self):
        # Get the current size of the queue
        return self.size  # Return the number of elements in the queue
