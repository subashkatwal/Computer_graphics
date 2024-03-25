
# import numpy as np
# import matplotlib.pyplot as plt

# class Polygon:
#     def __init__(self, vertices, color):
#         self.vertices = vertices
#         self.color = color

# def is_point_inside_polygon(x, y, polygon):
#     # Implement point-in-polygon test
#     pass

# def calculate_depth(x, y, polygon):
#     # Calculate depth (z-value) of the polygon at pixel (x, y)
#     pass

# def depth_buffer_method(polygons, width, height):
#     framebuffer = np.zeros((height, width, 3))  # Initialize framebuffer
#     depth_buffer = np.full((height, width), float('inf'))  # Initialize depth buffer

#     for polygon in polygons:
#         for x in range(width):
#             for y in range(height):
#                 if is_point_inside_polygon(x, y, polygon):
#                     depth = calculate_depth(x, y, polygon)
#                     if depth < depth_buffer[y, x]:
#                         depth_buffer[y, x] = depth
#                         framebuffer[y, x] = polygon.color

#     return framebuffer

# # Function to input vertices of a polygon from the user
# def input_polygon_vertices():
#     vertices = []
#     num_vertices = int(input("Enter the number of vertices for the polygon: "))
#     for i in range(num_vertices):
#         x = float(input(f"Enter x-coordinate for vertex {i+1}: "))
#         y = float(input(f"Enter y-coordinate for vertex {i+1}: "))
#         z = float(input(f"Enter z-coordinate for vertex {i+1}: "))
#         vertices.append((x, y, z))
#     return vertices

# # Function to input color of a polygon from the user
# def input_polygon_color():
#     r = int(input("Enter the red component (0-255): "))
#     g = int(input("Enter the green component (0-255): "))
#     b = int(input("Enter the blue component (0-255): "))
#     return (r, g, b)

# # Function to input number of polygons and their details from the user
# def input_polygons():
#     polygons = []
#     num_polygons = int(input("Enter the number of polygons: "))
#     for i in range(num_polygons):
#         print(f"Polygon {i+1}:")
#         vertices = input_polygon_vertices()
#         color = input_polygon_color()
#         polygons.append(Polygon(vertices, color))
#     return polygons

# # Get user input for framebuffer size
# width = int(input("Enter the width of the framebuffer: "))
# height = int(input("Enter the height of the framebuffer: "))

# # Get user input for defining polygons
# polygons = input_polygons()

# # Perform rendering using depth buffer method
# rendered_image = depth_buffer_method(polygons, width, height)

# # Display the rendered image using Matplotlib with white background
# plt.figure(facecolor='white')
# plt.imshow(rendered_image)
# plt.axis('off')  # Turn off axis
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

#simple primitive class to represent triangles
class Primitive:
    def __init__(self, vertices, color):
        self.vertices = vertices
        self.color = color

# Check if a point (x, y) is inside a triangle defined by its vertices
def is_pixel_inside_triangle(x, y, v0, v1, v2):
    def sign(p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

    b1 = sign((x, y), v0, v1) < 0.0
    b2 = sign((x, y), v1, v2) < 0.0
    b3 = sign((x, y), v2, v0) < 0.0

    return (b1 == b2 == b3)

# Calculate the depth (z-coordinate) of a point (x, y) in a triangle
def calculate_depth(x, y, v0, v1, v2):
    a = (v1[1] - v2[1]) * (x - v2[0]) + (v2[0] - v1[0]) * (y - v2[1])
    b = (v2[1] - v0[1]) * (x - v2[0]) + (v0[0] - v2[0]) * (y - v2[1])
    c = -((x - v2[0]) * (v0[1] - v1[1]) - (v0[0] - v1[0]) * (y - v2[1]))

    total_area = (v1[1] - v2[1]) * (v0[0] - v2[0]) + (v2[0] - v1[0]) * (v0[1] - v2[1])

    alpha = a / total_area
    beta = b / total_area
    gamma = c / total_area

    return alpha * v0[2] + beta * v1[2] + gamma * v2[2]


def depth_buffer_method(primitives, width, height):
    color_buffer = np.zeros((height, width, 3)) 
    depth_buffer = np.full((height, width), float('inf')) 

    for primitive in primitives:
        v0, v1, v2 = primitive.vertices
        color = primitive.color

        for x in range(width):
            for y in range(height):
                if is_pixel_inside_triangle(x, y, v0, v1, v2):
                    depth = calculate_depth(x, y, v0, v1, v2)
                    if depth < depth_buffer[y, x]:
                        depth_buffer[y, x] = depth
                        color_buffer[y, x] = color

    return color_buffer

# Main function
def main():
    
    primitives = [
        Primitive([(100, 100, 1), (200, 300, 2), (300, 100, 3)], (1, 0, 0)), 
        Primitive([(200, 200, 4), (400, 400, 5), (100, 400, 6)], (0, 1, 0)),  
        Primitive([(300, 300, 7), (500, 100, 8), (600, 300, 9)], (0, 0, 1))  
    ]

    
    width, height = 800, 600


    rendered_image = depth_buffer_method(primitives, width, height)
    
    plt.imshow(rendered_image)
    plt.axis('off')
    plt.title('Depth Buffer Algorithm')
    plt.show()

if __name__ == "__main__":
    main()
