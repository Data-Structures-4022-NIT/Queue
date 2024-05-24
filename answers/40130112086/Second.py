class PriorityQueue:

    #Initialize an empty priority queue.
    def __init__(self):
        self.queue = []

    #Add an item to the priority queue with the specified priority.
    def enqueue(self, item, priority):
        self.queue.append((priority, item))
        self.queue.sort(reverse=True)
        
    #Remove and return the item with the highest priority from the queue.
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop()[1]
        else:
            return None

    #Check if the priority queue is empty.
    def is_empty(self):
        length = self.size()
        if length == 0:
            return True
        else:
            return False

    #Return the number of elements in the priority queue.
    def size(self):
        return len(self.queue)