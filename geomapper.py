import geopandas as gpd
import matplotlib.pyplot as plt

# Load the GeoJSON file
geojson_file = "maps/UAH-EPS.geojson"
gdf = gpd.read_file(geojson_file)

# Plot the GeoJSON data
fig, ax = plt.subplots(figsize=(20, 20))
gdf.plot(ax=ax, color='blue', edgecolor='black')

# Customize the plot
plt.title('UAH', fontsize=15)
plt.xlabel('Longitude', fontsize=12)
plt.ylabel('Latitude', fontsize=12)

# Save the plot to SVG file
output_file_svg = 'img/UAH-EPS.svg'
plt.savefig(output_file_svg, format='svg')
print(f"Plot saved to {output_file_svg}")
