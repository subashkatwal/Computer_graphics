import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def shear_x(matrix, shear_amount):
    shear_matrix = np.array([
        [1, shear_amount, 0],
        [0, 1, 0],
        [0, 0, 1]
    ])
    return np.dot(shear_matrix, matrix)

def shear_y(matrix, shear_amount):
    shear_matrix = np.array([
        [1, 0, 0],
        [shear_amount, 1, 0],
        [0, 0, 1]
    ])
    return np.dot(shear_matrix, matrix)

# Define the original matrix (example)
matrix = np.array([
    [1, 2, 1],
    [3, 4, 1],
    [1, 1, 1]
])

# Get user input for shear amount
shear_amount_x = float(input("Enter shear amount for x-axis: "))
shear_amount_y = float(input("Enter shear amount for y-axis: "))

# Shear along x-axis
result_x = shear_x(matrix, shear_amount_x)

# Shear along y-axis
result_y = shear_y(matrix, shear_amount_y)

# Plotting the original and transformed matrices
fig = plt.figure(figsize=(15, 5))

# Original matrix
ax1 = fig.add_subplot(1, 3, 1, projection='3d')
ax1.set_title('Original Matrix')
X, Y = np.meshgrid(range(matrix.shape[0]), range(matrix.shape[1]))
ax1.plot_surface(X, Y, matrix, color='b', alpha=0.6)

# Sheared along x-axis
ax2 = fig.add_subplot(1, 3, 2, projection='3d')
ax2.set_title('Sheared along x-axis')
X, Y = np.meshgrid(range(result_x.shape[0]), range(result_x.shape[1]))
ax2.plot_surface(X, Y, result_x, color='r', alpha=0.6)

# Sheared along y-axis
ax3 = fig.add_subplot(1, 3, 3, projection='3d')
ax3.set_title('Sheared along y-axis')
X, Y = np.meshgrid(range(result_y.shape[0]), range(result_y.shape[1]))
ax3.plot_surface(X, Y, result_y, color='g', alpha=0.6)

plt.tight_layout()
plt.show()
