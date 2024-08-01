import geopandas as gpd
import matplotlib.pyplot as plt
from datetime import datetime
import os

def plot_geojson(input_file, output_file):
    # Read the GeoJSON file
    gdf = gpd.read_file(input_file)
    
    # Plot the data
    ax = gdf.plot(figsize=(10, 10), edgecolor='black')
    
    # Save the plot as SVG
    plt.savefig(output_file, format='svg')
    plt.close()

if __name__ == "__main__":
    # Define file paths
    data_path = '../data/map.geojson'
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_path = f'../images/{timestamp}_map_uah.svg'
    
    # Create images directory if it doesn't exist
    if not os.path.exists('../images'):
        os.makedirs('../images')
    
    # Plot and save the GeoJSON file
    plot_geojson(data_path, output_path)
    print(f"Saved SVG to {output_path}")
