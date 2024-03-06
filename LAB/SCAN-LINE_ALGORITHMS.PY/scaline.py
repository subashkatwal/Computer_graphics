import matplotlib.pyplot as plt

def scan_line_algorithm(vertices):
    edges = []
    for i in range(len(vertices)):
        p1 = vertices[i]
        p2 = vertices[(i + 1) % len(vertices)]
        if p1[1] != p2[1]:
            edges.append((min(p1[1], p2[1]), max(p1[1], p2[1]), p1[0], (p2[0] - p1[0]) / (p2[1] - p1[1])))
    edges.sort(key=lambda x: x[0])
    active_edges = []
    for y in range(edges[0][0], edges[-1][1] + 1):
        for edge in edges:
            if edge[0] == y:
                active_edges.append(edge)
        active_edges.sort(key=lambda x: x[2])
        i = 0
        while i < len(active_edges):
            if i + 1 < len(active_edges):
                for x in range(int(active_edges[i][2]), int(active_edges[i + 1][2]) + 1):
                    plt.plot(x, y, '-bo')
            i += 2
        for edge in active_edges:
            if edge[1] == y:
                active_edges.remove(edge)
        for i in range(len(active_edges)):
            active_edges[i] = (active_edges[i][0], active_edges[i][1], active_edges[i][2] + active_edges[i][3], active_edges[i][3])

def flood_fill(image, x, y, old_color, new_color):
    if x < 0 or x >= len(image[0]) or y < 0 or y >= len(image) or image[y][x] == new_color or image[y][x] == old_color:
        return
    image[y][x] = new_color
    flood_fill(image, x + 1, y, old_color, new_color)
    flood_fill(image, x - 1, y, old_color, new_color)
    flood_fill(image, x, y + 1, old_color, new_color)
    flood_fill(image, x, y - 1, old_color, new_color)

def main():
    while True:
        choice = int(input("Choose an algorithm:\n1. Scan Line Algorithm\n2. Flood Fill Algorithm\n3. Exit\nEnter your choice: "))
        
        if choice == 1:
            vertices = []
            num_vertices = int(input("Enter the number of vertices: "))
            for i in range(num_vertices):
                x, y = map(int, input(f"Enter vertex {i+1} (x, y): ").split())
                vertices.append((x, y))
            scan_line_algorithm(vertices)
            plt.title('Subash Katwal')  # Set the plot title
            plt.show()
            
        elif choice == 2:
            num_vertices = int(input("Enter the number of vertices: "))
            vertices = []
            for i in range(num_vertices):
                while True:
                    try:
                        x, y = map(int, input(f"Enter vertex {i+1} (x, y): ").split())
                        vertices.append((x, y))
                        break
                    except ValueError:
                        print("Invalid input. Please enter integers for x and y coordinates.")
            image = [[0] * (max(x for x, _ in vertices) + 1) for _ in range(max(y for _, y in vertices) + 1)]
            for j in range(num_vertices - 1):
                plt.plot([vertices[j][0], vertices[j+1][0]], [vertices[j][1], vertices[j+1][1]], color='black')
            plt.plot([vertices[-1][0], vertices[0][0]], [vertices[-1][1], vertices[0][1]], color='black')
            plt.show()
            x, y = map(int, input("Enter the starting point (x, y): ").split())
            flood_fill(image, x, y, 0, 1)
            plt.imshow(image, cmap='hot', interpolation='nearest')
            plt.show()
        elif choice == 3:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
