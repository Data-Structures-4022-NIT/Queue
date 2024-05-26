class Data:
    def __init__(self, priority, item):
        self.priority = priority  # Set the priority of the item
        self.item = item  # Set the item

class PriorityQueue:
    def __init__(self):
        self.pQueue = []  # Initialize the priority queue as an empty list
        self.rear = 0  # Rear pointer starts at 0
        self.front = 0  # Front pointer starts at 0

    def enqueue(self, item, priority):
        # Add an item to the priority queue
        new_data = Data(priority, item)  # Create a new Data object
        if self.isEmpty():
            self.pQueue.append(new_data)  # Add the item to the queue
        else:
            inserted = False
            for i in range(len(self.pQueue)):
                if self.pQueue[i].priority <= new_data.priority:
                    self.pQueue.insert(i, new_data)  # Insert the item based on priority
                    inserted = True
                    break
            if not inserted:
                self.pQueue.append(new_data)  # Append if it's the highest priority
        self.rear += 1  # Increment the rear pointer

    def dequeue(self):
        # Remove an item from the priority queue
        if self.isEmpty():
            return "Underflow"  # The queue is empty
        else:
            self.front += 1  # Increment the front pointer
            return self.pQueue.pop(0).item  # Return and remove the item with the highest priority

    def isEmpty(self):
        # Check if the queue is empty
        return self.rear == self.front  # True if rear and front are equal, else False

    def sizeOfQueue(self):
        # Get the current size of the queue
        return self.rear - self.front  # Return the number of elements in the queue
