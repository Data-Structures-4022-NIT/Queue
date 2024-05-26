class Queue:
    def __init__(self):
        self.items = []  # Initialize the list to hold the queue items
        self.rear = 0  # Rear pointer to track the end of the queue
        self.front = 0  # Front pointer to track the start of the queue

    def enqueue(self, item):
        # Add an item to the rear of the queue
        self.items.append(item)  # Append item to the list
        self.rear += 1  # Increment the rear pointer

    def dequeue(self):
        # Remove an item from the front of the queue
        if self.isEmpty():
            return "Underflow"  # Return underflow if the queue is empty
        else:
            self.front += 1  # Increment the front pointer
            return self.items.pop(0)  # Pop the first item from the list

    def isEmpty(self):
        # Check if the queue is empty
        return self.rear == self.front  # True if rear equals front, else False

    def sizeOfQueue(self):
        # Return the current size of the queue
        return self.rear - self.front  # Calculate the size by subtracting front from rear

def shortest_path(maze, start, end):
    # Find the shortest path in a maze from start to end
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Possible movement directions
    rows, cols = len(maze), len(maze[0])  # Dimensions of the maze
    visited = set()  # Set to track visited positions
    queue = Queue()  # Initialize the queue

    queue.enqueue((start, 0))  # Enqueue the start position with distance 0

    while not queue.isEmpty():
        current_pos, dist = queue.dequeue()  # Dequeue the current position and distance

        if current_pos == end:
            return dist  # Return the distance if end is reached

        visited.add(current_pos)  # Mark the current position as visited

        for dx, dy in directions:
            # Calculate the new position
            new_x, new_y = current_pos[0] + dx, current_pos[1] + dy

            # Check if the new position is valid and not visited
            if 0 <= new_x < rows and 0 <= new_y < cols and maze[new_x][new_y] == 0 and (new_x, new_y) not in visited:
                queue.enqueue(((new_x, new_y), dist + 1))  # Enqueue the new position with updated distance

    return -1  # Return -1 if no path is found
