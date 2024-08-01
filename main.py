from src.plotGeoJSON import plot_geojson
from datetime import datetime
import os

def main():
    # Define file paths
    data_path = 'data/map.geojson'
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_path = f'images/{timestamp}_map_uah.svg'
    
    # Create images directory if it doesn't exist
    if not os.path.exists('images'):
        os.makedirs('images')
    
    # Plot and save the GeoJSON file
    plot_geojson(data_path, output_path)
    print(f"Saved SVG to {output_path}")

if __name__ == "__main__":
    main()
