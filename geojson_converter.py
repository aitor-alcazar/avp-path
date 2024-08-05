import os
import geopandas as gpd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()
GEOJSON_FILE = os.getenv('GEOJSON_FILE')
MAP_GEOJSON_FILE = os.getenv('MAP_GEOJSON_FILE')

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def ensure_output_directory_exists(output_path):
    """Ensure the output directory exists."""
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        logger.info(f"Created directory: {output_dir}")

def convert_geojson_to_vector_image(input_path, output_path):
    """Convert GeoJSON to a vector image (SVG)."""
    logger.info(f"Reading GeoJSON file: {input_path}")
    gdf = gpd.read_file(input_path)
    
    # Prepare the plot
    logger.info("Creating vector image...")
    fig, ax = plt.subplots(figsize=(10, 10))
    gdf.plot(ax=ax, edgecolor='black')
    
    # Save the plot as SVG
    plt.axis('off')
    plt.savefig(output_path, format='svg', bbox_inches='tight', pad_inches=0)
    plt.close(fig)
    logger.info(f"Vector image saved to: {output_path}")

def main():
    logger.info("Starting conversion process...")
    
    # Ensure output directory exists
    ensure_output_directory_exists(MAP_GEOJSON_FILE)
    
    # Convert GeoJSON to vector image
    convert_geojson_to_vector_image(GEOJSON_FILE, MAP_GEOJSON_FILE)
    
    logger.info("Conversion process completed.")

if __name__ == "__main__":
    main()
