import numpy as np

class Grid:
    def __init__(self, width, height, obstacles=[]):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width), dtype=int)
        for obstacle in obstacles:
            self.grid[obstacle[1], obstacle[0]] = 1

    def is_within_bounds(self, position):
        x, y = position
        return 0 <= x < self.width and 0 <= y < self.height

    def is_walkable(self, position):
        x, y = position
        return self.is_within_bounds(position) and self.grid[y, x] == 0
