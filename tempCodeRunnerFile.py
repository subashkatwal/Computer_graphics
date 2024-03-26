
import numpy as np
import matplotlib.pyplot as plt

# Define constants
WIDTH = 800
HEIGHT = 600

# Function to initialize the A-buffer
def initialize_abuffer(width, height):
    abuffer = [[[] for _ in range(width)] for _ in range(height)]
    return abuffer

# Function to update A-buffer with a new fragment
def update_abuffer(abuffer, x, y, depth, color):
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        if not abuffer[y][x] or depth < abuffer[y][x][0]:
            abuffer[y][x] = [depth, color]
    return abuffer

# Function to composite final image from A-buffer
def composite_abuffer(abuffer):
    image = np.zeros((HEIGHT, WIDTH, 3))
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if abuffer[y][x]:
                image[y, x] = abuffer[y][x][1]
    return image

# Function to render a simple 2D scene
def render_scene():
    abuffer = initialize_abuffer(WIDTH, HEIGHT)
    
    # Render a red rectangle
    for y in range(200, 400):
        for x in range(200, 400):
            depth = 0.5  # Arbitrary depth value
            color = [0.7, 0.7, 0.7]  # Red color
            abuffer = update_abuffer(abuffer, x, y, depth, color)
    
    # Render a green circle with a white border
    center_x = 400
    center_y = 300
    radius = 100
    border_width = 2
    
    for y in range(HEIGHT):
        for x in range(WIDTH):
            distance_to_center = ((x - center_x) ** 2 + (y - center_y) ** 2) ** 0.5
            if (radius - border_width <= distance_to_center <= radius) and (distance_to_center >= radius - border_width):
                depth = 0.4  # Arbitrary depth value
                if distance_to_center < radius:
                    color = [0.0, 1.0, 0.0]  # Green color for the circle
                else:
                    color = [1.0, 1.0, 1.0]  # White color for the border
                abuffer = update_abuffer(abuffer, x, y, depth, color)
    
    # Composite final image
    image = composite_abuffer(abuffer)
    
    return image

# Main function
def main():
    image = render_scene()
    plt.imshow(image)
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()
