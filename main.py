from src.grid import Grid
from src.astar import astar
from src.visualizer import save_grid_image

def main():
    grid = Grid(width=20, height=20)
    grid.add_obstacles(num_obstacles=20)
    start = (0, 0)
    end = (16, 18)
    path = astar(grid, start, end)
    
    if path:
        print("Path found:", path)
    else:
        print("No path found")

    save_grid_image(grid, path, start, end, 'images/grid.png')

if __name__ == "__main__":
    main()
