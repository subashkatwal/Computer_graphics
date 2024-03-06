# WAP to find implement scan-line polygon fill algorithm
'''import matplotlib.pyplot as plt

def draw_polygon(vertices):
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % len(vertices)]
        plt.plot([x1, x2], [y1, y2], color='black')

def scanline_fill(vertices, fill_color):
    ymin = int(min(v[1] for v in vertices))
    ymax = int(max(v[1] for v in vertices))

    edges = []
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % len(vertices)]
        if y1 != y2:
            edges.append((min(y1, y2), max(y1, y2), x1, y1, (y2 - y1) / (x2 - x1)))

    edges.sort(key=lambda edge: edge[0])

    active_edges = []
    for y in range(ymin, ymax + 1):
        active_edges = [edge for edge in active_edges if edge[1] > y]
        active_edges.extend(edge for edge in edges if edge[0] == y)

        active_edges.sort(key=lambda edge: edge[2])

        fill = False
        for i in range(0, len(active_edges), 2):
            x1 = int(active_edges[i][2])
            x2 = int(active_edges[i + 1][2])
            plt.plot(range(x1, x2 + 1), [y] * (x2 - x1 + 1), color=fill_color)
            fill = not fill

        for i in range(len(active_edges)):
            active_edges[i] = (active_edges[i][0], active_edges[i][1], active_edges[i][2] + active_edges[i][4]) if len(active_edges[i]) > 4 else active_edges[i]

def main():
    plt.figure()

    # Ask the user to enter polygon vertices
    vertices = []
    num_vertices = int(input("Enter the number of vertices: "))
    for i in range(num_vertices):
        x, y = map(float, input(f"Enter the coordinates for vertex {i + 1} (x y): ").split())
        vertices.append((x, y))

    # Draw the polygon
    draw_polygon(vertices)

    # Fill the polygon using scan-line algorithm with color 'green'
    scanline_fill(vertices, fill_color='black')

    plt.title("Scan-Line Polygon Fill")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
'''


# WAP to find implement secondary  fill algorithm
# import matplotlib.pyplot as plt

# image = [[0] * 100 for _ in range(100)]
# col1, col2 = map(int, input("Enter the pixel colors(col1  col2 ) ").split(" "))
# x, y = map(int, input("Enter value for coordinate of pixel").split(" "))
# if not (0 <= col1 <= 255) or not (0<=  col2 <=255):
#     print("RGB format exceed ! ")
#     exit()

# if not (0<= x<len(image))or not(0<=y<len(image[0])):
#     print("Negative coordinate is invalid ! ")
#     exit()


# def fill(x, y, col1, col2):
#     if 0 <= x < len(image) and 0 <= y < len(image[0])and image[x][y] == col1:
#         image[x][y] = col2
#         fill(x + 1, y, col1, col2)
#         fill(x - 1, y, col1, col2)
#         fill(x, y + 1, col1, col2)
#         fill(x, y - 1, col1, col2)


# fill(x, y, image[x][y], col2)
# filled_pixels =[(i, j)for i in range(len(image))for j in range(len(image[0]))if image[i][j] == col2]
# x_values, y_values = zip(*filled_pixels)

# plt.scatter(x_values, y_values, c="black", marker=".")
# plt.plot(x, y,marker='o',color='red')
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.show()



# import matplotlib.pyplot as plt
# import numpy as np

# def fill(x,y,fill_color,boundary_color):
#     x_color=fill_color
#     y_color=fill_color

#     if(x_color!= fill_color ) and(y_color != fill_color)and (x_color != boundary_color and  y_color!=fill_color):
#         x_color=fill_color
#         y_color=fill_color
        
#         fill(x + 1, y, fill_color, boundary_color) 
#         fill(x, y + 1, fill_color, boundary_color)  
#         fill(x - 1, y, fill_color, boundary_color)
#         fill(x, y - 1, fill_color, boundary_color)


# x,y=map(int,input("Enter the coordinates inside the object : "))
# fill_color=int (input("enter the color to be filled "))
# boundary_color=int(input("Enter the boundary color if the object"))


# WAP to find implement flood  fill algorithm
