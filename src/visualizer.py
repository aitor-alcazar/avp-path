import matplotlib.pyplot as plt
import numpy as np
import os

def save_grid_image(grid, path, start, end, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    grid_data = grid.grid.copy()
    
    for (x, y) in path:
        grid_data[y, x] = 0.5
    
    grid_data[start[1], start[0]] = 0.8
    grid_data[end[1], end[0]] = 0.9
    
    fig, ax = plt.subplots()
    ax.imshow(grid_data, cmap='Greys', origin='upper')

    ax.scatter(*zip(*path), c='blue', s=10, label='Path')
    ax.scatter(*start, c='green', s=100, label='Start')
    ax.scatter(*end, c='red', s=100, label='End')
    ax.legend()

    # Mesh
    ax.set_xticks(np.arange(-0.5, grid.width, 1))
    ax.set_yticks(np.arange(-0.5, grid.height, 1))
    ax.grid(which='both', color='black', linestyle='-', linewidth=1)
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

    plt.savefig(filename)
    plt.close()
