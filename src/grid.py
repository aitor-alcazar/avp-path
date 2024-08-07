import numpy as np

class Grid:
    def __init__(self, width, height, obstacles=None):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width))

        if obstacles:
            for (x, y) in obstacles:
                self.grid[y, x] = 1

    def add_obstacles(self, num_obstacles):
        count = 0
        while count < num_obstacles:
            x = np.random.randint(0, self.width)
            y = np.random.randint(0, self.height)
            if self.grid[y, x] == 0:  # Ensure not placing on an existing obstacle
                self.grid[y, x] = 1
                count += 1

    def get_neighbors(self, node):
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for direction in directions:
            neighbor = (node[0] + direction[0], node[1] + direction[1])
            if 0 <= neighbor[0] < self.width and 0 <= neighbor[1] < self.height:
                if self.grid[neighbor[1], neighbor[0]] == 0:
                    neighbors.append(neighbor)
        return neighbors
