class Queue:

    #Initialize an empty queue.
    def __init__(self):
        self.items = []

    #Add an item to the rear of the queue.
    def enqueue(self, item):
        self.items.append(item)

    #Remove and return the front item from the queue.
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    #Check if the queue is empty.
    def is_empty(self):
        length=self.size()
        if length==0:
            return  True
        else:
            return False

    #Return the number of elements in the queue.
    def size(self):
        return len(self.items)