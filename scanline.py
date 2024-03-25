
import numpy as np
import matplotlib.pyplot as plt

class Edge:
    def __init__(self, ymin, ymax, x, slope):
        self.ymin = ymin
        self.ymax = ymax
        self.x = x
        self.slope = slope

def scanline_fill(vertices, color):
    # Find the top and bottom y-coordinates of the polygon
    ymin = min(vertices, key=lambda vertex: vertex[1])[1]
    ymax = max(vertices, key=lambda vertex: vertex[1])[1]

    # Create edges table
    edges = []
    for i in range(len(vertices)):
        p1 = vertices[i]
        p2 = vertices[(i + 1) % len(vertices)]
        if p1[1] != p2[1]:  # Ignore horizontal edges
            if p1[1] < p2[1]:
                ymin, ymax = p1[1], p2[1]
                xmin = p1[0]
            else:
                ymin, ymax = p2[1], p1[1]
                xmin = p2[0]
            slope = (p2[0] - p1[0]) / (p2[1] - p1[1])
            edges.append(Edge(ymin, ymax, xmin, slope))

    # Initialize the active edge table
    active_edges = []

    # Initialize the scanline buffer
    scanline_buffer = np.zeros((ymax - ymin + 1, ymax - ymin + 1))

    # Fill the polygon using scanline algorithm
    for y in range(ymin, ymax + 1):
        # Remove edges from active edge table whose ymax = y
        active_edges = [edge for edge in active_edges if edge.ymax != y]

        # Add edges from edges table whose ymin = y
        for edge in edges:
            if edge.ymin == y:
                active_edges.append(edge)

        # Sort active edges by x-coordinate
        active_edges.sort(key=lambda edge: edge.x)

        # Fill scanline buffer with intersection points
        intersections = []
        for i in range(0, len(active_edges), 2):
            x1 = int(round(active_edges[i].x))
            x2 = int(round(active_edges[i + 1].x))
            x1 = max(0, min(x1, ymax - ymin))  # Clip x1 to buffer bounds
            x2 = max(0, min(x2, ymax - ymin))  # Clip x2 to buffer bounds
            intersections.extend(range(x1, x2 + 1))

        # Append a placeholder value if the number of intersections is odd
        if len(intersections) % 2 != 0:
            intersections.append(ymax - ymin)

        # Fill pixels between pairs of intersection points
        for i in range(0, len(intersections), 2):
            x1 = intersections[i]
            x2 = intersections[i + 1]
            scanline_buffer[y - ymin, x1:x2 + 1] = 1

        # Update x-coordinate of active edges
        for edge in active_edges:
            edge.x += edge.slope

    # Plot the filled polygon
    plt.imshow(scanline_buffer, cmap='gray', origin='lower')
    plt.title('Scanline Fill Algorithm')
    plt.axis('off')
    plt.show()

# Example usage:
vertices = [(50, 50), (200, 150), (100, 250)]
color = 'blue'
scanline_fill(vertices, color)
