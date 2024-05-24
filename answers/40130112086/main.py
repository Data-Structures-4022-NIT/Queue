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


    ### Question 1: Maze Solver using Queues
    def maze_solver(maze, start, end):
        #Define the movements directions
        #right,left,up,down
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        #determining the dimensions of the maze.
        rows, cols = len(maze), len(maze[0])
        #Initialize the queue and visited set
        queue = Queue()
        visited = set()
        #Add the starting point to the queue and visited set
        queue.enqueue(start)
        visited.add(start)
        #Keep track of the path
        path = {start: []}

        while not queue.is_empty():
            row,col = queue.dequeue()

            #Check if it is the end point
            if (row, col) == end:
                return path[(row, col)]

            #Explore the neighboring cells
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] == '0' and (
                new_row, new_col) not in visited:
                    queue.enqueue((new_row, new_col))
                    visited.add((new_row, new_col))
                    path[(new_row, new_col)] = path[(row, col)] + [(new_row, new_col)]
        return None

    ###Question 2: Josephus Problem
    def josephus(n, k):
        #Creating a queue
        queue = Queue()
        for i in range(1, n + 1):
            queue.enqueue(i)

        while queue.size() > 1:
            #Skip k-1 participants
            for i in range(k - 1):
                queue.enqueue(queue.dequeue())
            #Eliminate the one
            queue.dequeue()
        return queue.dequeue()
