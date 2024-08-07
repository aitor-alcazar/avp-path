import logging
from src.grid import Grid
from src.astar import astar
from src.visualizer import save_grid_image

# Configure the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    # Define grid size
    grid_width = 100
    grid_height = 100
    
    # Create grid instance
    grid = Grid(grid_width, grid_height)
    
    # Path to GeoJSON file
    geojson_path = 'data/PlantaBajaGeo.geojson'
    
    # Load obstacles from GeoJSON
    logger.info("Loading obstacles from GeoJSON")
    grid.load_obstacles_from_geojson(geojson_path)
    
    # Define start and end points
    start = (10, 10)
    end = (80, 80)
    
    # Find path using A* algorithm
    logger.info("Finding path using A* algorithm")
    path = astar(grid, start, end)
    
    # Print path
    logger.info(f"Path found: {path}")
    
    # Save grid image
    image_path = 'images/grid.svg'
    save_grid_image(grid, path, start, end, image_path)
    logger.info(f"Grid image saved as {image_path}")

if __name__ == "__main__":
    main()
