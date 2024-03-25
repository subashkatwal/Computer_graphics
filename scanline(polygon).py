
import matplotlib.pyplot as plt

def draw_polygon(vertices):
    x = [v[0] for v in vertices]
    y = [v[1] for v in vertices]
    plt.plot(x + [x[0]], y + [y[0]], color='black')

def edge_table(vertices):
    edges = []
    for i in range(len(vertices)):
        p1 = vertices[i]
        p2 = vertices[(i + 1) % len(vertices)]
        if p1[1] > p2[1]:
            p1, p2 = p2, p1
        edges.append((p1[1], p1[0], p2[1], p2[0]))
    edges.sort()
    return edges

def scanline_fill(vertices):
    et = edge_table(vertices)
    scanlines = []
    for edge in et:
        scanlines += list(range(edge[0], edge[2] + 1))
    ymin = min(et, key=lambda x: x[0])[0]
    ymax = max(et, key=lambda x: x[2])[2]
    for y in range(ymin, ymax + 1):
        intersections = []
        for edge in et:
            if edge[0] <= y < edge[2]:
                x = edge[1] + (edge[3] - edge[1]) * (y - edge[0]) / (edge[2] - edge[0])
                intersections.append(x)
        intersections.sort()
        for i in range(0, len(intersections), 2):
            x1 = int(intersections[i])
            x2 = int(intersections[i + 1])
            plt.plot(range(x1, x2 + 1), [y] * (x2 - x1 + 1), color='black')

# Example usage
vertices = [(50, 50), (200, 150), (150, 250), (100, 200)]
draw_polygon(vertices)
scanline_fill(vertices)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Scan Line Polygon fill Algorithm")
plt.show()
