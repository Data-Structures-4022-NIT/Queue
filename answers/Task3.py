class AsciiPriorityQueue:
    def __init__(self, string):
        self.queue = []
        for char in string:
            self.enqueue(char)

    def enqueue(self, item):
        self.queue.append(item)
        self._heapify_up(len(self.queue) - 1)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        # Swap the first and the last item, remove the last (maximum) item
        self._swap(0, len(self.queue) - 1)
        highest = self.queue.pop()
        self._heapify_down(0)
        return highest

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def print(self):
        print(", ".join(self.queue))

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if parent_index >= 0 and self.queue[index] > self.queue[parent_index]:
            self._swap(index, parent_index)
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        largest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.queue) and self.queue[left_child] > self.queue[largest]:
            largest = left_child

        if right_child < len(self.queue) and self.queue[right_child] > self.queue[largest]:
            largest = right_child

        if largest != index:
            self._swap(index, largest)
            self._heapify_down(largest)

    def _swap(self, i, j):
        self.queue[i], self.queue[j] = self.queue[j], self.queue[i]

def main():
    string = input("Enter the sequence of characters: ")
    queue = AsciiPriorityQueue(string)

    print("Initial queue state:")
    queue.print()

    while not queue.is_empty():
        removed_item = queue.dequeue()
        print(f"Dequeued item with highest ASCII value: {removed_item}")
        print("Current queue state:")
        queue.print()

if __name__ == "__main__":
    main()
