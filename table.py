
import numpy as np

def vertex_table(vertices):
    return np.array(vertices)

def edge_table(vertices):
    edges = []
    for i in range(len(vertices)):
        p1 = vertices[i]
        p2 = vertices[(i + 1) % len(vertices)]
        edges.append((f"E{i+1}", i+1, (i+1)%len(vertices)+1))
    return edges

def polygon_surface_table(vertices):
    surfaces = []
    for i in range(len(vertices)):
        p1 = vertices[i]
        p2 = vertices[(i + 1) % len(vertices)]
        p3 = vertices[(i + 2) % len(vertices)]
        surfaces.append((f"S{i+1}", i+1, (i+1)%len(vertices)+1, (i+2)%len(vertices)+1))
    return surfaces
#input vertices from user
def input_vertices():
    vertices = []
    num_vertices = int(input("Enter the number of vertices: "))
    for i in range(num_vertices):
        x = float(input(f"Enter x-coordinate for vertex {i+1}: "))
        y = float(input(f"Enter y-coordinate for vertex {i+1}: "))
        z = float(input(f"Enter z-coordinate for vertex {i+1}: "))
        vertices.append((x, y, z))
    return vertices

# Get vertices from user
vertices = input_vertices()

vertex_tab = vertex_table(vertices)
edge_tab = edge_table(vertices)
surface_tab = polygon_surface_table(vertices)


print("\nVertex Table:")
for i, vertex in enumerate(vertices):
    print(f"v{i+1}: {vertex}")

print("\nEdge Table:")
for i, edge in enumerate(edge_tab):
    print(f"{edge[0]}: {vertices[edge[1]-1]}, {vertices[edge[2]-1]} (Edge {i+1})")

print("\nPolygon Surface Table:")
for i, surface in enumerate(surface_tab):
    print(f"{surface[0]}: {', '.join(map(str, [vertices[v-1] for v in surface[1:]]))} (Polygon {i+1})")
