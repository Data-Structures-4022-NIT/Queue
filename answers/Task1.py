from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.queue.popleft()

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

def is_valid_move(maze, visited, row, col):
    return (0 <= row < len(maze)) and (0 <= col < len(maze[0])) and (maze[row][col] == '0') and (not visited[row][col])

def find_shortest_path(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    q = Queue()
    q.enqueue((start, [start]))  # Store the current position and the path taken to reach there
    visited[start[0]][start[1]] = True

    while not q.is_empty():
        (current, path) = q.dequeue()
        if current == end:
            return path

        for direction in directions:
            next_row, next_col = current[0] + direction[0], current[1] + direction[1]
            if is_valid_move(maze, visited, next_row, next_col):
                visited[next_row][next_col] = True
                q.enqueue(((next_row, next_col), path + [(next_row, next_col)]))

    return None  # No path found

# Example usage:
maze = [
    ['0', '1', '0', '0', '0'],
    ['0', '1', '0', '1', '0'],
    ['0', '0', '0', '1', '0'],
    ['0', '1', '1', '1', '0'],
    ['0', '0', '0', '0', '0']
]
start = (0, 0)
end = (4, 4)

path = find_shortest_path(maze, start, end)
if path:
    print("Shortest path:", path)
else:
    print("No path found")
