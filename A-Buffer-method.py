# import numpy as np
# import matplotlib.pyplot as plt

# class ABuffer:
#     def __init__(self):
#         self.buffer = []  # Initialize an empty buffer

#     def add_pixel(self, x, y, depth, color):
#         """
#         Add a pixel to the A-buffer.
#         :param x: X-coordinate of the pixel
#         :param y: Y-coordinate of the pixel
#         :param depth: Depth value of the pixel
#         :param color: Color of the pixel
#         """
#         # Check if the pixel is already in the buffer
#         for i, (px, py, pdepth, pcolor) in enumerate(self.buffer):
#             if px == x and py == y:
#                 # Compare depths and update if necessary
#                 if depth < pdepth:
#                     self.buffer[i] = (x, y, depth, color)
#                 return

#         # If not found, add the pixel to the buffer
#         self.buffer.append((x, y, depth, color))

#     def get_pixel(self, x, y):
#         """
#         Get the pixel with the minimum depth at the specified coordinates.
#         :param x: X-coordinate
#         :param y: Y-coordinate
#         :return: (depth, color) of the pixel
#         """
#         min_depth = float('inf')
#         min_color = None

#         for px, py, depth, color in self.buffer:
#             if px == x and py == y:
#                 if depth < min_depth:
#                     min_depth = depth
#                     min_color = color

#         return min_depth, min_color

#     def plot_buffer(self):
#         """
#         Plot the pixels stored in the A-buffer.
#         """
#         # Create an empty image with white background
#         image = np.ones((100, 100, 3)) * 255

#         # Iterate through pixels in the buffer and set their color in the image
#         for x, y, _, color in self.buffer:
#             image[y, x] = color  # Note: In numpy arrays, the first dimension is y (rows), second is x (columns)

#         # Plot the image
#         plt.imshow(image.astype(np.uint8))
#         plt.title("A-Buffer Visualization")
#         plt.axis('off')
#         plt.show()

# # Example usage
# abuffer = ABuffer()
# abuffer.add_pixel(10, 20, 0.5, (255, 0, 0))  # Add a red pixel
# abuffer.add_pixel(10, 20, 0.3, (0, 255, 0))  # Update with a green pixel (lower depth)
# abuffer.add_pixel(15, 25, 0.8, (0, 0, 255))  # Add another pixel
# abuffer.add_pixel(10, 20, 0.2, (255, 255, 0))  # Update with a yellow pixel (even lower depth)

# # Plot the A-buffer
# abuffer.plot_buffer()


import numpy as np
import matplotlib.pyplot as plt

class ABufferRenderer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.color_buffer = np.zeros((height, width, 3))  # RGB color buffer
        self.depth_buffer = np.full((height, width), np.inf)  # Depth buffer initialized with infinity

    def clear_buffers(self):
        self.color_buffer.fill(0)  # Clear color buffer
        self.depth_buffer.fill(np.inf)  # Clear depth buffer

    def set_fragment(self, x, y, depth, color):
        if 0 <= x < self.width and 0 <= y < self.height:
            if depth < self.depth_buffer[y, x]:
                self.depth_buffer[y, x] = depth
                self.color_buffer[y, x] = color

    def render(self):
        # Check if depth buffer contains valid values
        if np.isnan(np.min(self.depth_buffer)) or np.isnan(np.max(self.depth_buffer)):
            print("Invalid depth values in the depth buffer. Rendering aborted.")
            return

        plt.imshow(self.color_buffer, origin='lower')
        plt.title("A-Buffer Rendering")
        plt.axis('off')
        plt.show()

# Example usage
renderer = ABufferRenderer(400, 300)
renderer.clear_buffers()

# Draw a triangle with varying depths
renderer.set_fragment(100, 100, 0.5, [1, 0, 0])  # Red
renderer.set_fragment(200, 200, 0.3, [0, 1, 0])  # Green
renderer.set_fragment(300, 100, 0.7, [0, 0, 1])  # Blue

# Render the image
renderer.render()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

class ABufferRenderer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.color_buffer = np.zeros((height, width, 3))  # RGB color buffer
        self.depth_buffer = np.full((height, width), np.inf)  # Depth buffer initialized with infinity

    def clear_buffers(self):
        self.color_buffer.fill(0)  # Clear color buffer
        self.depth_buffer.fill(np.inf)  # Clear depth buffer

    def set_fragment(self, x, y, depth, color):
        if 0 <= x < self.width and 0 <= y < self.height:
            if depth < self.depth_buffer[y, x]:
                self.depth_buffer[y, x] = depth
                self.color_buffer[y, x] = color

    def render(self):
        fig, ax = plt.subplots()
        ax.imshow(self.color_buffer, origin='lower')
        plt.title("A-Buffer Rendering")
        plt.axis('off')

        # Draw the triangles with white fill and black borders
        red_triangle = Polygon([(100, 100), (200, 100), (150, 200)], closed=True, facecolor='white', edgecolor='black')
        ax.add_patch(red_triangle)

        blue_triangle = Polygon([(150, 150), (250, 150), (200, 250)], closed=True, facecolor='white', edgecolor='black')
        ax.add_patch(blue_triangle)

        # Annotate overlapping fragments inside the triangles
        for y in range(self.height):
            for x in range(self.width):
                if self.color_buffer[y, x].any() != 0:
                    plt.text(x, y, "Overlap", color='black', fontsize=8, ha='center', va='center')

        plt.show()

# Example usage
renderer = ABufferRenderer(400, 300)
renderer.clear_buffers()

# Draw two overlapping triangles
for y in range(100, 200):
    for x in range(100, 200):
        renderer.set_fragment(x, y, 0.3, [1, 0, 0])  # Red triangle

for y in range(150, 250):
    for x in range(150, 250):
        renderer.set_fragment(x, y, 0.5, [0, 0, 1])  # Blue triangle

# Render the image
renderer.render()
