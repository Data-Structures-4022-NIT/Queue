class Queue:
    def __init__(self):
        self.items = []  # Initialize an empty list to hold queue items
        self.rear = 0  # Initialize rear pointer to track the end of the queue
        self.front = 0  # Initialize front pointer to track the start of the queue

    def enqueue(self, item):
        # Add an item to the rear of the queue
        self.items.append(item)  # Append the item to the list
        self.rear += 1  # Increment the rear pointer

    def dequeue(self):
        # Remove an item from the front of the queue
        if self.isEmpty():
            return "Underflow"  # Return "Underflow" if the queue is empty
        else:
            self.front += 1  # Increment the front pointer
            return self.items.pop(0)  # Remove and return the first item from the list

    def isEmpty(self):
        # Check if the queue is empty
        return self.rear == self.front  # True if rear equals front, else False

    def sizeOfQueue(self):
        # Return the current size of the queue
        return self.rear - self.front  # Calculate size by subtracting front from rear
