#LAB 4
#WAP to implement 2D geometric transformation a) translation b)rotation c) scaling 


# import matplotlib.pyplot as plt 


# x1, y1 = map(int, input("Enter the first coordinate of the line: ").split(" "))
# x2, y2 = map(int, input("Enter the second coordinate of the line: ").split(" "))
# tx, ty = map(int, input("Enter the translated coordinate of the line: ").split(" "))

# var1 = x1 + tx
# var = y1 + ty

# var2 = x2 + tx
# var3 = y2 + ty

# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")

# plt.plot([x1, x2], [y1, y2], label='Original Line')
# plt.plot([var1, var2], [var, var3], label='Translated Line')
# plt.legend()
# plt.show()

#b) rotation 

'''import matplotlib.pyplot as plt
import math
import numpy as np

def calculate_sin_cos(angle_in_degree):
    angle_in_radian = math.radians(angle_in_degree)
    sin = math.sin(angle_in_radian)
    cos = math.cos(angle_in_radian)
    return sin, cos

angle = float(input("Enter the angle in degrees: "))
sin, cos = calculate_sin_cos(angle)

start_x, start_y = map(int, input("Enter the starting coordinates: ").split(" "))
end_x, end_y = map(int, input("Enter the ending coordinates: ").split(" "))

start_vector = np.array([start_x, start_y])
end_vector = np.array([end_x, end_y])

rotation_matrix = np.array([[cos, -sin],
                            [sin, cos]])

print("Matrix before rotation:")
print("Start Vector:\n", start_vector)
print("End Vector:\n", end_vector)

result = np.matmul(start_vector, rotation_matrix)

print("\nMatrix after rotation:")
print("Result Vector:\n", result)



print("Result after rotation:", result)

# Plotting vectors
vectors = [start_vector, end_vector, result]
colors = ['r', 'g', 'b']
labels = ['Start Vector', 'End Vector', 'Result']

for vector, color, label in zip(vectors, colors, labels):
    plt.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color=color, label=label)

plt.xlabel("X-label")
plt.ylabel("Y-label")
plt.legend()
plt.grid()
plt.show()
'''


#c) scaling 
'''import matplotlib.pyplot as plt 
x1, y1 = map(int, input("Enter the first coordinate of the line: ").split(" "))
x2, y2 = map(int, input("Enter the second coordinate of the line: ").split(" "))
tx, ty = map(int, input("Enter the scaling coordinate of the line: ").split(" "))

var1 = x1 * tx
var = y1 * ty

var2 = x2 * tx
var3 = y2 * ty

plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.plot([x1, x2], [y1, y2], label='Original Line')
plt.plot([var1, var2], [var, var3], label='Translated Line')
plt.legend()
plt.title("Subash Katwal")
plt.grid(True)
plt.show()
'''


# import matplotlib.pyplot as plt
# import math
# import numpy as np

# def translation():
#     x1, y1 = map(int, input("Enter the first coordinate of the line: ").split(" "))
#     x2, y2 = map(int, input("Enter the second coordinate of the line: ").split(" "))
#     tx, ty = map(int, input("Enter the translated coordinate of the line: ").split(" "))

#     var1 = x1 + tx
#     var = y1 + ty

#     var2 = x2 + tx
#     var3 = y2 + ty

#     plt.xlabel("X-axis")
#     plt.ylabel("Y-axis")

#     plt.plot([x1, x2], [y1, y2], label='Original Line')
#     plt.plot([var1, var2], [var, var3], label='Translated Line')
#     plt.grid(True)
#     plt.title("Transformation")
#     plt.legend()
#     plt.show()

# def rotation():
#     angle = float(input("Enter the angle in degrees: "))
#     sin = math.sin(math.radians(angle))
#     cos = math.cos(math.radians(angle))

#     start_x, start_y = map(int, input("Enter the starting coordinates: ").split(" "))
#     end_x, end_y = map(int, input("Enter the ending coordinates: ").split(" "))

#     start_vector = np.array([start_x, start_y])
#     end_vector = np.array([end_x, end_y])

#     rotation_matrix = np.array([[cos, -sin],
#                                 [sin, cos]])

#     print("Matrix before rotation:")
#     print("Start Vector:\n", start_vector)
#     print("End Vector:\n", end_vector)

#     result = np.matmul(start_vector, rotation_matrix)

#     print("\nMatrix after rotation:")
#     print("Result Vector:\n", result)

#     print("Result after rotation:", result)

#     # Plotting vectors
#     vectors = [start_vector, end_vector, result]
#     colors = ['r', 'g', 'b']
#     labels = ['Start Vector', 'End Vector', 'Result']

#     for vector, color, label in zip(vectors, colors, labels):
#         plt.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color=color, label=label)

#     plt.xlabel("X-label" )
#     plt.ylabel("Y-label" )
#     plt.title("Rotation")
#     plt.legend(loc='upper left')
#     plt.grid(True)
#     plt.show()

# def scaling():
#     x1, y1 = map(int, input("Enter the first coordinate of the line: ").split(" "))
#     x2, y2 = map(int, input("Enter the second coordinate of the line: ").split(" "))
#     tx, ty = map(int, input("Enter the scaling coordinate of the line: ").split(" "))

#     var1 = x1 * tx
#     var = y1 * ty

#     var2 = x2 * tx
#     var3 = y2 * ty

#     plt.xlabel("X-axis")
#     plt.ylabel("Y-axis")

#     plt.plot([x1, x2], [y1, y2], label='Original Line')
#     plt.plot([var1, var2], [var, var3], label='Scaled Line')
#     plt.legend()
#     plt.title("Scaling")
#     plt.grid(True)
#     plt.show()

# while True:
#     print("\n1. Translation\n2. Rotation\n3. Scaling\n4. Exit")
#     choice = input("Enter your choice (1-4): ")

#     if choice == '1':
#         translation()
#     elif choice == '2':
#         rotation()
#     elif choice == '3':
#         scaling()
#     elif choice == '4':
#         print("Exiting the program.")
#         break
#     else:
#         print("Invalid choice. Please enter a valid option.")



#with rotation of point only 
# import matplotlib.pyplot as plt
# import math
# import numpy as np

# def translation():
#     x1, y1 = map(int, input("Enter the first coordinate of the line: ").split(" "))
#     x2, y2 = map(int, input("Enter the second coordinate of the line: ").split(" "))
#     tx, ty = map(int, input("Enter the translated coordinate of the line: ").split(" "))

#     var1 = x1 + tx
#     var = y1 + ty

#     var2 = x2 + tx
#     var3 = y2 + ty

#     plt.xlabel("X-axis")
#     plt.ylabel("Y-axis")

#     plt.plot([x1, x2], [y1, y2], label='Original Line')
#     plt.plot([var1, var2], [var, var3], label='Translated Line')
#     plt.grid(True)
#     plt.title("Transformation")
#     plt.legend()
#     plt.show()

# def rotation():
#     angle = float(input("Enter the angle in degrees: "))
#     sin = math.sin(math.radians(angle))
#     cos = math.cos(math.radians(angle))

#     x, y = map(int, input("Enter the coordinates of the point: ").split(" "))

#     point = np.array([x, y])

#     rotation_matrix = np.array([[cos, -sin],
#                                 [sin, cos]])

#     print("Point before rotation:", point)

#     result = np.matmul(rotation_matrix, point)

#     print("\nPoint after rotation:", result)

#     # Plotting vectors
#     vectors = [point, result]
#     colors = ['r', 'b']
#     labels = ['Original Point', 'Rotated Point']

#     for vector, color, label in zip(vectors, colors, labels):
#         plt.plot(vector[0], vector[1], 'o', color=color, label=label)

#     plt.xlabel("X-label")
#     plt.ylabel("Y-label")
#     plt.title("Rotation")
#     plt.legend(loc='upper right')
#     plt.grid(True)
#     plt.show()


# def scaling():
#     x1, y1 = map(int, input("Enter the first coordinate of the line: ").split(" "))
#     x2, y2 = map(int, input("Enter the second coordinate of the line: ").split(" "))
#     tx, ty = map(int, input("Enter the scaling coordinate of the line: ").split(" "))

#     var1 = x1 * tx
#     var = y1 * ty

#     var2 = x2 * tx
#     var3 = y2 * ty

#     plt.xlabel("X-axis")
#     plt.ylabel("Y-axis")

#     plt.plot([x1, x2], [y1, y2], label='Original Line')
#     plt.plot([var1, var2], [var, var3], label='Scaled Line')
#     plt.legend()
#     plt.title("Scaling")
#     plt.grid(True)
#     plt.show()

# while True:
#     print("\n1. Translation\n2. Rotation\n3. Scaling\n4. Exit")
#     choice = input("Enter your choice (1-4): ")

#     if choice == '1':
#         translation()
#     elif choice == '2':
#         rotation()
#     elif choice == '3':
#         scaling()
#     elif choice == '4':
#         print("Exiting the program.")
#         break
#     else:
#         print("Invalid choice. Please enter a valid option.")
