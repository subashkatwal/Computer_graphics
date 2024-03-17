import numpy as np
import matplotlib.pyplot as plt

def apply_horizontal_shear(points, shear_factor):
    shear_matrix = np.array([
        [1, shear_factor],
        [0, 1]
    ])
    return np.dot(points, shear_matrix)

def apply_vertical_shear(points, shear_factor):
    shear_matrix = np.array([
        [1, 0],
        [shear_factor, 1]
    ])
    return np.dot(points, shear_matrix)

# Define the original coordinates of the square
original_square = np.array([
    [0, 0],
    [1, 0],
    [1, 1],
    [0, 1],
    [0, 0]  # Closing point to complete the square
])

# Take input from the user for horizontal shear factor
horizontal_shear_factor = float(input("Enter the horizontal shear factor: "))

# Take input from the user for vertical shear factor
vertical_shear_factor = float(input("Enter the vertical shear factor: "))

# Apply horizontal shear
sheared_square_horizontal = apply_horizontal_shear(original_square, horizontal_shear_factor)

# Apply vertical shear
sheared_square_vertical = apply_vertical_shear(original_square, vertical_shear_factor)

# Plot the original square
plt.plot(original_square[:, 0], original_square[:, 1], 'b-', label='Original Square')

# Plot the horizontally sheared square
plt.plot(sheared_square_horizontal[:, 0], sheared_square_horizontal[:, 1], 'r-', label='Horizontal Shear')

# Plot the vertically sheared square
plt.plot(sheared_square_vertical[:, 0], sheared_square_vertical[:, 1], 'g-', label='Vertical Shear')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Shearing Transformation')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
