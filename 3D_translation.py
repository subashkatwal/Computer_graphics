import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def translate_3d(points, dx, dy, dz):
    translation_matrix = np.array([
        [1, 0, 0, dx],
        [0, 1, 0, dy],
        [0, 0, 1, dz],
        [0, 0, 0, 1]
    ])
    # Convert points to homogeneous coordinates
    homogeneous_points = np.hstack((points, np.ones((len(points), 1))))
    # Apply translation
    translated_points = np.dot(homogeneous_points, translation_matrix.T)
    return translated_points[:, :3]  # Convert back to 3D coordinates

# Take input from the user for the coordinates of 3D points
num_points = int(input("Enter the number of 3D points: "))
points = np.zeros((num_points, 3))
for i in range(num_points):
    points[i] = list(map(float, input(f"Enter coordinates for point {i+1} (x y z): ").split()))

# Take input from the user for the translation amounts along each axis
dx = float(input("Enter the translation amount along the x-axis: "))
dy = float(input("Enter the translation amount along the y-axis: "))
dz = float(input("Enter the translation amount along the z-axis: "))

# Apply translation
translated_points = translate_3d(points, dx, dy, dz)
print("Original Points:\n", points)
print("\nTranslated Points:\n", translated_points)

# Plot original points
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(points[:,0], points[:,1], points[:,2], c='b', label='Original Points')

# Plot translated points
ax.scatter(translated_points[:,0], translated_points[:,1], translated_points[:,2], c='r', label='Translated Points')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Translation')
ax.legend()

plt.show()
