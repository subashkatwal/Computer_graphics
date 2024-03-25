import matplotlib.pyplot as plt
import numpy as np

def flood_fill(image, x, y, target_color, replacement_color):
    if image[x][y] != target_color:
        return

    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        if 0 <= x < image.shape[0] and 0 <= y < image.shape[1] and image[x][y] == target_color:
            image[x][y] = replacement_color
            stack.append((x + 1, y))  # Right
            stack.append((x - 1, y))  # Left
            stack.append((x, y + 1))  # Down
            stack.append((x, y - 1))  # Up
            # Visualization of flood fill process
            plt.imshow(image, cmap='gray', interpolation='nearest')
            plt.axis('off')
            plt.pause(0.01)  # Pause for visualization
            plt.clf()  # Clear previous plot

# Create a test image
image = np.zeros((100, 100))
image[40:60, 40:60] = 1  # Draw a square in the middle

# Set the starting point for flood fill
start_x, start_y = 50, 50

# Define the target and replacement colors
target_color = 0
replacement_color = 0.5

# Display the original image
plt.imshow(image, cmap='gray', interpolation='nearest')
plt.axis('off')
plt.show()

# Perform flood fill
flood_fill(image, start_x, start_y, target_color, replacement_color)

# Display the filled image
plt.imshow(image, cmap='gray', interpolation='nearest')
plt.axis('off')
plt.title("Flood Fill Algorithm")
plt.show()
