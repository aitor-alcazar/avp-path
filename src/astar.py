from heapq import heappush, heappop
from src.node import Node

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, end):
    start_node = Node(start)
    end_node = Node(end)
    open_list = []
    closed_list = set()
    heappush(open_list, start_node)

    while open_list:
        current_node = heappop(open_list)
        closed_list.add(current_node.position)

        if current_node == end_node:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for new_position in neighbors:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if not grid.is_walkable(node_position):
                continue

            neighbor_node = Node(node_position, current_node)
            if neighbor_node.position in closed_list:
                continue

            neighbor_node.g = current_node.g + 1
            neighbor_node.h = heuristic(neighbor_node.position, end_node.position)
            neighbor_node.f = neighbor_node.g + neighbor_node.h

            if any(open_node for open_node in open_list if neighbor_node == open_node and neighbor_node.g > open_node.g):
                continue

            heappush(open_list, neighbor_node)

    return None
