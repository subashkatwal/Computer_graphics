import numpy as np
import matplotlib.pyplot as plt

def boundary_fill(image, x, y, fill_color, boundary_color):
    stack = [(x, y)]
    boundary_color = np.array(boundary_color)
    fill_color = np.array(fill_color)

    while stack:
        x, y = stack.pop()

        if not np.array_equal(image[y, x], boundary_color) and not np.array_equal(image[y, x], fill_color):
            image[y, x] = fill_color

            # Check top pixel
            if y - 1 >= 0:
                stack.append((x, y - 1))
            # Check bottom pixel
            if y + 1 < image.shape[0]:
                stack.append((x, y + 1))
            # Check left pixel
            if x - 1 >= 0:
                stack.append((x - 1, y))
            # Check right pixel
            if x + 1 < image.shape[1]:
                stack.append((x + 1, y))

def main():
    # Get user input for image dimensions
    width = int(input("Enter the width of the image: "))
    height = int(input("Enter the height of the image: "))

    # Create an image with all pixels initialized to white
    image = np.full((height, width, 3), 255, dtype=np.uint8)

    # Get user input for seed point
    seed_x = int(input("Enter the x-coordinate of the seed point: "))
    seed_y = int(input("Enter the y-coordinate of the seed point: "))

    # Set seed point color to black
    image[seed_y, seed_x] = (0, 0, 0)

    # Get user input for fill color
    fill_color = tuple(map(int, input("Enter the fill color (R G B): ").split()))

    # Get user input for boundary color
    boundary_color = tuple(map(int, input("Enter the boundary color (R G B): ").split()))

    # Add an extra dot to represent the seed point
    extra_dot_x = seed_x + 1
    extra_dot_y = seed_y + 1
    if extra_dot_x < width and extra_dot_y < height:
        image[extra_dot_y, extra_dot_x] = (0, 0, 0)
    plt.text(extra_dot_x, extra_dot_y, "Seed", fontsize=10, color='black', ha='left', va='bottom')
    boundary_fill(image, seed_x, seed_y, fill_color, boundary_color)

    plt.imshow(image)
    plt.title("Boundary Fill Algorithm")
    plt.show()

if __name__ == "__main__":
    main()