import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import LineString, Point
import logging

# Configure the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def save_grid_image(grid, path, start, end, filename):
    """Save the grid as an image with obstacles and path"""
    logger.info(f"Saving grid image as {filename}")
    
    fig, ax = plt.subplots(figsize=(grid.width / 10, grid.height / 10))  # Adjust size according to grid
    ax.imshow(grid.grid, cmap='Greys', origin='lower')
    
    if path:
        path_x, path_y = zip(*path)
        ax.plot(path_x, path_y, color='blue', lw=2, marker='o', markersize=5, label='Path')
    
    ax.plot(start[0], start[1], 'go', label='Start')
    ax.plot(end[0], end[1], 'ro', label='End')
    
    ax.set_title('Grid with Obstacles and Path')
    ax.set_xlabel('X coordinate')
    ax.set_ylabel('Y coordinate')
    ax.legend()
    
    plt.savefig(filename, format='svg')
    plt.close(fig)
    logger.info(f"Grid image saved as {filename}")
