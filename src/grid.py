import json
import pyproj
import numpy as np
from shapely.geometry import LineString, Point, Polygon
from shapely.ops import transform
import logging
from tqdm import tqdm

# Configure the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width), dtype=int)
        self.proj = None
        self.min_x = 0
        self.min_y = 0

    def load_obstacles_from_geojson(self, filename):
        logger.info(f"Loading obstacles from GeoJSON file: {filename}")
        with open(filename, 'r') as file:
            data = json.load(file)

        # Read CRS from GeoJSON
        crs_info = data.get('crs', None)
        if crs_info and 'properties' in crs_info:
            crs_name = crs_info['properties'].get('name', 'EPSG:4326')  # Default WGS84
            self.proj = pyproj.Transformer.from_proj(
                pyproj.Proj(crs_name),  # CRS from GeoJSON
                pyproj.Proj(proj='utm', zone=33, datum='WGS84')  # Assuming UTM zone 33N for the grid
            )
        else:
            # Default CRS if not provided
            self.proj = pyproj.Transformer.from_proj(
                pyproj.Proj('epsg:4326'),  # WGS84
                pyproj.Proj(proj='utm', zone=33, datum='WGS84')  # Assuming UTM zone 33N
            )

        # Calculate bounds of all features to adjust grid size
        min_x, min_y, max_x, max_y = float('inf'), float('inf'), float('-inf'), float('-inf')

        for feature in tqdm(data['features'], desc="Processing features"):
            geom_type = feature['geometry']['type']
            coordinates = feature['geometry']['coordinates']

            if geom_type == 'LineString':
                coords = self._convert_coordinates(coordinates)
                min_x, min_y, max_x, max_y = self._update_bounds(coords, min_x, min_y, max_x, max_y)
            elif geom_type == 'Polygon':
                coords = self._convert_coordinates(coordinates[0])  # Assuming the first ring is relevant
                min_x, min_y, max_x, max_y = self._update_bounds(coords, min_x, min_y, max_x, max_y)

        # Adjust grid size based on coordinate range
        self.min_x = min_x
        self.min_y = min_y
        self.width = int(round(max_x - min_x + 1))
        self.height = int(round(max_y - min_y + 1))
        self.grid = np.zeros((self.height, self.width), dtype=int)

        # Add obstacles to the grid
        for feature in tqdm(data['features'], desc="Adding obstacles"):
            geom_type = feature['geometry']['type']
            coordinates = feature['geometry']['coordinates']

            if geom_type == 'LineString':
                coords = self._convert_coordinates(coordinates)
                self._add_line_obstacles(coords)
            elif geom_type == 'Polygon':
                coords = self._convert_coordinates(coordinates[0])  # Assuming the first ring is relevant
                self._add_polygon_obstacles(coords)

    def _convert_coordinates(self, coordinates):
        """Convert coordinates from GeoJSON CRS to grid CRS"""
        logger.info("Converting coordinates to grid CRS")
        converted_coords = []
        for lon, lat in coordinates:
            x, y = self.proj.transform(lon, lat)
            converted_coords.append((x - self.min_x, y - self.min_y))  # Adjust based on min_x and min_y
        return converted_coords

    def _update_bounds(self, coords, min_x, min_y, max_x, max_y):
        """Update bounds based on coordinates"""
        for x, y in coords:
            if x < min_x:
                min_x = x
            if y < min_y:
                min_y = y
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
        return min_x, min_y, max_x, max_y

    def _add_line_obstacles(self, coordinates):
        """Add linear obstacles to the grid"""
        logger.info("Adding line obstacles to the grid")
        line = LineString(coordinates)
        num_points = int(np.ceil(line.length))  # Number of points to interpolate
        for i in range(num_points):
            point = line.interpolate(i).coords[0]  # Get the interpolated point
            x, y = point
            cell_x = int(round(x))
            cell_y = int(round(y))
            if 0 <= cell_x < self.width and 0 <= cell_y < self.height:
                self.grid[self.height - cell_y - 1, cell_x] = 1

    def _add_polygon_obstacles(self, coordinates):
        """Add polygonal obstacles to the grid"""
        logger.info("Adding polygon obstacles to the grid")
        polygon = Polygon(coordinates)
        for x in tqdm(range(self.width), desc="Processing grid cells", unit="cell"):
            for y in range(self.height):
                if polygon.contains(Point(x + 0.5, y + 0.5)):  # Points are placed at the center of cells
                    self.grid[self.height - y - 1, x] = 1
