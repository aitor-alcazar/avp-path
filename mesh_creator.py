import os
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()
GEOJSON_FILE = os.getenv('GEOJSON_FILE')
MESH_OUTPUT_PATH = os.getenv('MESH_OUTPUT_PATH')

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def ensure_output_directory_exists(output_path):
    """Ensure the output directory exists."""
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        logger.info(f"Created directory: {output_dir}")

def plot_geojson_with_mesh(input_path, output_path):
    """Plot GeoJSON data with a mesh overlay."""
    logger.info(f"Reading GeoJSON file: {input_path}")
    gdf = gpd.read_file(input_path)

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 10))
    gdf.plot(ax=ax, edgecolor='black', alpha=0.5)
    
    # Add mesh grid overlay
    bounds = gdf.total_bounds
    x_min, y_min, x_max, y_max = bounds
    x_ticks = np.arange(np.floor(x_min), np.ceil(x_max), (x_max - x_min) / 10)
    y_ticks = np.arange(np.floor(y_min), np.ceil(y_max), (y_max - y_min) / 10)

    for x in x_ticks:
        plt.axvline(x=x, color='blue', linestyle='--', linewidth=0.5)
    for y in y_ticks:
        plt.axhline(y=y, color='blue', linestyle='--', linewidth=0.5)
    
    plt.axis('equal')
    plt.axis('off')
    plt.savefig(output_path, format='svg', bbox_inches='tight', pad_inches=0)
    plt.close(fig)
    logger.info(f"Mesh overlay image saved to: {output_path}")

def main():
    logger.info("Starting mesh overlay process...")
    
    # Ensure output directory exists
    ensure_output_directory_exists(MESH_OUTPUT_PATH)
    
    # Plot GeoJSON with mesh overlay
    plot_geojson_with_mesh(GEOJSON_FILE, MESH_OUTPUT_PATH)
    
    logger.info("Mesh overlay process completed.")

if __name__ == "__main__":
    main()
