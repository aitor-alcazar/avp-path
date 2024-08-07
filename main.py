from src.grid import Grid
from src.astar import astar

def main():
    grid = Grid(width=10, height=10, obstacles=[(1, 1), (1, 2), (2, 2)])
    start = (0, 0)
    end = (9, 9)
    path = astar(grid, start, end)
    
    if path:
        print("Path found:", path)
    else:
        print("No path found")

if __name__ == "__main__":
    main()
