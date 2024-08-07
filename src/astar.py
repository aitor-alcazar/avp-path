import heapq
import numpy as np
import logging

# Configure the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def astar(grid, start, end):
    """A* pathfinding algorithm"""
    logger.info("Starting A* pathfinding")
    
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    def get_neighbors(node):
        neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = node[0] + dx, node[1] + dy
            if 0 <= nx < grid.width and 0 <= ny < grid.height:
                if grid.grid[grid.height - ny - 1, nx] == 0:
                    neighbors.append((nx, ny))
        return neighbors
    
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, end), 0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, end)}
    
    while open_set:
        _, current_g, current = heapq.heappop(open_set)
        
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        for neighbor in get_neighbors(current):
            tentative_g_score = g_score[current] + 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                if neighbor not in [i[2] for i in open_set]:
                    heapq.heappush(open_set, (f_score[neighbor], tentative_g_score, neighbor))
    
    return []

