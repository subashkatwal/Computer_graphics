# Import the code from geometry.py
import geometry

# Example data
vertices = [
    geometry.Vertex(1, 0, 0, 0),
    geometry.Vertex(2, 1, 0, 0),
    geometry.Vertex(3, 1, 1, 0),
    geometry.Vertex(4, 0, 1, 0)
]

edges = [
    geometry.Edge(1, 1, 2),
    geometry.Edge(2, 2, 3),
    geometry.Edge(3, 3, 4),
    geometry.Edge(4, 4, 1)
]

polygons = [
    geometry.Polygon(1, [1, 2, 3, 4])
]

# Create tables
vertex_table = geometry.create_vertex_table(vertices)
edge_table = geometry.create_edge_table(edges)
polygon_table = geometry.create_polygon_table(polygons)

# Print tables
print("Vertex Table:")
for vertex in vertex_table:
    print(vertex)
print("\nEdge Table:")
for edge in edge_table:
    print(edge)
print("\nPolygon Table:")
for polygon in polygon_table:
    print(polygon)
