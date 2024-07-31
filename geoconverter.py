import geojson
from pyproj import Transformer

# Initialize the transformer to convert from EPSG:3857 to EPSG:4326
transformer = Transformer.from_crs("epsg:3857", "epsg:4326", always_xy=True)

# Load the GeoJSON file
with open('input.geojson', 'r') as f:
    data = geojson.load(f)

def transform_coordinates(feature):
    geom_type = feature['geometry']['type']
    coords = feature['geometry']['coordinates']
    
    if geom_type == 'Point':
        feature['geometry']['coordinates'] = list(transformer.transform(*coords))
    
    elif geom_type == 'MultiPoint':
        feature['geometry']['coordinates'] = [list(transformer.transform(*coord)) for coord in coords]
    
    elif geom_type == 'LineString':
        feature['geometry']['coordinates'] = [list(transformer.transform(*coord)) for coord in coords]
    
    elif geom_type == 'MultiLineString':
        feature['geometry']['coordinates'] = [[list(transformer.transform(*coord)) for coord in line] for line in coords]
    
    elif geom_type == 'Polygon':
        feature['geometry']['coordinates'] = [[list(transformer.transform(*coord)) for coord in ring] for ring in coords]
    
    elif geom_type == 'MultiPolygon':
        feature['geometry']['coordinates'] = [[[list(transformer.transform(*coord)) for coord in ring] for ring in poly] for poly in coords]
    
    return feature

# Apply transformation to each feature
transformed_features = [transform_coordinates(feature) for feature in data['features']]
data['features'] = transformed_features

# Save the transformed GeoJSON data
with open('output.geojson', 'w') as f:
    geojson.dump(data, f, indent=2)

print("Conversion complete. Output saved to 'output.geojson'.")
