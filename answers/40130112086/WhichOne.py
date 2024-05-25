#use PriorityQueue for this part
class PriorityQueue:
    #Initialize an queue of your choosing
    def __init__(self, string):
        self.queue = sorted([char for char in string], reverse=True)

    #Add an item according to its asscii value into the queue.
    def enqueue(self, item):
        index = self.binary_search(item)
        self.queue.insert(index, item)
    #Remove and return the item with the highest ascci value from the queue.
    def dequeue(self):
        return self.queue.pop(0)
    #Print all characters in the queue.
    def print(self):
        print(', '.join(self.queue))
    #Check if the circular queue is empty.
    def is_empty(self):
        return len(self.queue) == 0
    #Return the number of elements in the circular queue.
    def size(self):
        return len(self.queue)

    def binary_search(self, item):
        left = 0
        right = len(self.queue) - 1

        while left <= right:
            mid = (left + right) // 2
            if ord(self.queue[mid]) < ord(item):
                right = mid - 1
            else:
                left = mid + 1

        return left