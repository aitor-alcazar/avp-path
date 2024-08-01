import geopandas as gpd
import networkx as nx
import heapq
from shapely.geometry import LineString

def distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

def heuristic(a, b):
    """Heuristic function for A* (Euclidean distance)."""
    return distance(a, b)

def astar(graph, start, goal):
    """Perform A* search to find the shortest path in the graph."""
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    g_costs = {start: 0}
    f_costs = {start: heuristic(start, goal)}
    came_from = {}
    
    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        
        for neighbor in graph.neighbors(current):
            tentative_g_cost = g_costs[current] + graph[current][neighbor]['weight']
            
            if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                came_from[neighbor] = current
                g_costs[neighbor] = tentative_g_cost
                f_costs[neighbor] = tentative_g_cost + heuristic(neighbor, goal)
                if neighbor not in [i[1] for i in open_set]:
                    heapq.heappush(open_set, (f_costs[neighbor], neighbor))
    
    return None

def main():
    # Load the GeoJSON file
    gdf = gpd.read_file('PlantaBajaGeo.geojson')
    
    # Initialize the graph
    G = nx.Graph()
    
    # Add nodes and edges to the graph
    for _, row in gdf.iterrows():
        coords = list(row['geometry'].coords)
        for i in range(len(coords) - 1):
            start, end = coords[i], coords[i + 1]
            if not G.has_node(start):
                G.add_node(start)
            if not G.has_node(end):
                G.add_node(end)
            # Add edge with the distance as weight
            G.add_edge(start, end, weight=distance(start, end))
    
    # Define start and goal points (example coordinates)
    start_point = (-3.168777446011473, 40.635870747224757)
    goal_point = (-3.168712307519646, 40.635779576371945)
    
    # Find the path using A* algorithm
    path = astar(G, start_point, goal_point)
    
    # Print the result
    if path:
        print("Path found:")
        for point in path:
            print(point)
    else:
        print("No path found")

if __name__ == '__main__':
    main()
