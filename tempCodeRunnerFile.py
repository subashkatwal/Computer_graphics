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
