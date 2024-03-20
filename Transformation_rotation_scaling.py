#LAB 4
#WAP to implement 2D geometric transformation a) translation b)rotation c) scaling 


import matplotlib.pyplot as plt
import math

def translation():
    x1, y1 = map(int, input("Enter the first coordinate of the line: ").split(" "))
    x2, y2 = map(int, input("Enter the second coordinate of the line: ").split(" "))
    tx, ty = map(int, input("Enter the translated coordinate of the line: ").split(" "))

    var1 = x1 + tx
    var = y1 + ty

    var2 = x2 + tx
    var3 = y2 + ty

    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")

    plt.plot([x1, x2], [y1, y2], label='Original Line')
    plt.plot([var1, var2], [var, var3], label='Translated Line')
    plt.grid(True)
    plt.title("Transformation")
    plt.legend()
    plt.show()


def rotation(x1, y1, x2, y2, angle):
    # Calculate sine and cosine of the angle
    c = math.cos(math.radians(angle))
    s = math.sin(math.radians(angle))

    # Perform rotation
    x1_new = x1 * c + y1 * s
    y1_new = -x1 * s + y1 * c
    x2_new = x2 * c + y2 * s
    y2_new = -x2 * s + y2 * c
    
    print("Point before rotation:")
    print("[{}, {}]".format(x1, y1))
    print("[{}, {}]".format(x2, y2))

    print("\nPoint after rotation:")
    print("[{:.2f}, {:.2f}]".format(x1_new, y1_new))
    print("[{:.2f}, {:.2f}]".format(x2_new, y2_new))

    # Initialize the graphics window
    plt.figure()
    plt.axis('equal')

    # Draw the original line
    plt.plot([x1, x2], [y1, y2], color='red', label='Original Line')

    # Draw the rotated line
    plt.plot([x1_new, x2_new], [y1_new, y2_new], color='blue', label='Rotated Line')

    # Set labels and title
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Rotation of a line')

    # Show legend
    plt.legend()

    # Show plot
    plt.grid(True)
    plt.show()


def scaling():
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
    plt.plot([var1, var2], [var, var3], label='Scaled Line')
    plt.legend()
    plt.title("Scaling")
    plt.grid(True)
    plt.show()

while True:
    print("\n1. Translation\n2. Rotation\n3. Scaling\n4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        translation()
    elif choice == '2':
        x1, y1 = map(int, input("Enter the coordinates of the starting point of the line: ").split(" "))
        x2, y2 = map(int, input("Enter the coordinates of the ending point of the line: ").split(" "))
        angle = float(input("Enter the rotation angle in degrees: "))
        rotation(x1, y1, x2, y2, angle)
    elif choice == '3':
        scaling()
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
