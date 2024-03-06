#LAB 01
# WAP that prompts the user to enter the co ordinates for points and then display them
"""import matplotlib.pyplot as plt
x1, y1=map(float,input("Enter the first coordinates : \n").split(" "))
print(f"Point 1 coordinates is :({x1},{y1})")
x2, y2=map(float,input("Enter the second co ordinates : \n").split(" "))
print(f"Point 1 coordinates is :({x2},{y2})")

plt.plot([x1,x2],[y1,y2],'-bo')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.title("Subash Katwal ")
plt.grid(True)
plt.show()
"""
# WAP to implement DDA algorithm
'''
import matplotlib.pyplot as plt

x1, x2 = map(int, input(" Enter x coordinates of a line :").split())
y1, y2 = map(int, input("Enter y coordinates of a line ").split())
print(f"The x coordinates are{x1,x2} and y coordinates are{y1,y2}")

dx = x2 - x1
dy = y2 - y1

x = x1
y = y1
M = (y2 - y1) / (x2 - x1)


if abs(dx) > abs(y) or M < 1:
    steps = abs(dx)
else:
    steps = abs(dy)


X_incr = dx / float(steps)
Y_incr = dy / float(steps)
xs = [x]
ys = [y]
print("Step\tX\tY\tRounded X\tRounded Y")
print("-" * 50)
for i in range(steps):
    if i < steps:
        x += X_incr
        y += Y_incr
        xs.append(x)
        ys.append(y)
        
        round_x = round(x)
        round_y = round(y)

        print(f"{i + 1}\t{x:.2f}\t{y:.2f}\t{round_x}\t\t{round_y}")

plt.plot(xs, ys,'bo-')
plt.title("Subash Katwal")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
'''


"""
import math
import matplotlib.pyplot as plt

x1 = float(input("Enter starting co-ordinate x1:"))
y1 = float(input("Enter starting co-ordinate y1:"))
x2 = float(input("Enter ending co-ordinate x2:"))
y2 = float(input("Enter ending co-ordinate y2:"))

plt.plot([x1, x2], [y1, y2])

dx = x2 - x1
dy = y2 - y1
m = dy / dx
xk = x1
yk = y1
plt.scatter(xk, yk)

print(f"{'Step':<5}\t{'xk':<5}\t{'yk':<5}\t{'pk':<5}\t{'xk+1':<7}\t{'yk+1':<7}\t")
print("-" * 45)

if abs(m) < 1:
    i = 1
    po = 2 * dy - dx
    pk = po
    steps = dx
    while i <= steps:
        if pk < 0:
            xk += 1
            pk = pk + 2 * dy
        else:
            xk += 1
            yk += 1
            pk = pk + 2 * dy - 2 * dx
        i = i + 1
        print(f"{i:<5}\t{xk:<5}\t{yk:<5}\t{pk:<5}\t{xk+1:<7}\t{yk+1:<7}\t")
        plt.scatter(xk, yk)
        plt.grid(True)
        plt.title("Subash Katwal")
    plt.show()

else:
    i = 1
    po = 2 * dx - dy
    pk = po
    steps = dy
    while i <= steps:
        if pk < 0:
            yk += 1
            pk = pk + 2 * dy
        else:
            xk += 1
            yk += 1
            pk = pk + 2 * dx - 2 * dy
        i = i + 1
        print(f"{i:<5}\t{xk:<5}\t{yk:<5}\t{pk:<5}\t{xk+1:<7}\t{yk+1:<7}\t")
        plt.scatter(xk, yk)
        plt.title("Subash Katwal")
    plt.grid(True)
    plt.title("Subash Katwal")
    plt.show()

"""


# import matplotlib.pyplot as plt

# def draw_circle(radius, h, k):
#     x, y = radius, 0
#     P = 1 - radius

#     print(f"Steps\tXk+1\tYk+1\tPk\t(x,y)\t(-x,y)\t(x,-y)\t(-x,-y)\t(y,x)\t(-y,x)\t(y,-x)\t(-y,-x)\t")

#     while x <= y:
#         print(f"{x}\t{h + x}\t{k + y}\t{P}\t"
#               f"({x + h},{y + k})\t({-x + h},{y + k})\t"
#               f"({x + h},{-y + k})\t({-x + h},{-y + k})\t"
#               f"({y + h},{x + k})\t({-y + h},{x + k})\t"
#               f"({y + h},{-x + k})\t({-y + h},{-x + k})\t")

#         plt.scatter(x + h, y + k, )
#         plt.scatter(-x + h, y + k,)
#         plt.scatter(x + h, -y + k,)
#         plt.scatter(-x + h, -y + k)
#         plt.scatter(y + h, x + k, )
#         plt.scatter(-y + h, x + k,)
#         plt.scatter(y + h, -x + k,)
#         plt.scatter(-y + h, -x + k)


#         if P < 0:
#             x+=1
#             P = P + 2 * x + 1
#         else:
#             P = P + 2 * x +1-2 * y
#             y -= 1

#     plt.xlabel('X-axis')
#     plt.ylabel('Y-axis')
#     plt.grid(True)
#     plt.axis('equal')
#     plt.show()

# def main():
#     radius = int(input("Enter the radius: "))
#     h, k = map(int, input("Enter the h and k: ").split(" "))
#     draw_circle(radius, h, k)

# if __name__ == "__main__":
#     main()

# radius 10 h and k 2 3 
import matplotlib.pyplot as plt

def draw_circle(radius, h, k):
    x, y = 0, radius
    P = 1 - radius

    print(f"Steps\tXk+1\tYk+1\tPk\t(x,y)\t(-x,y)\t(x,-y)\t(-x,-y)\t(y,x)\t(-y,x)\t(y,-x)\t(-y,-x)\t")

    while x <= y:
        print(f"{x}\t{h + x}\t{k + y}\t{P}\t"
              f"({x + h},{y + k})\t({-x + h},{y + k})\t"
              f"({x + h},{-y + k})\t({-x + h},{-y + k})\t"
              f"({y + h},{x + k})\t({-y + h},{x + k})\t"
              f"({y + h},{-x + k})\t({-y + h},{-x + k})\t")

        plt.scatter(x + h, y + k, )
        plt.scatter(-x + h, y + k,)
        plt.scatter(x + h, -y + k,)
        plt.scatter(-x + h, -y + k)
        plt.scatter(y + h, x + k, )
        plt.scatter(-y + h, x + k,)
        plt.scatter(y + h, -x + k,)
        plt.scatter(-y + h, -x + k)

        if P <= 0:
            P = P + 2 * x + 3
        else:
            P = P + 2 * x - 2 * y + 5
            y -= 1

        x += 1

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.axis('equal')
    plt.show()

def main():
    radius = int(input("Enter the radius: "))
    h, k = map(int, input("Enter the h and k: ").split(" "))
    draw_circle(radius, h, k)

if __name__ == "__main__":
    main()





# WAP to find implement scan-line polygon fill algorithm



# import turtle

# def draw_polygon(vertices):
#     turtle.penup()
#     turtle.goto(vertices[0])
#     turtle.pendown()

#     for vertex in vertices:
#         turtle.goto(vertex)

#     turtle.goto(vertices[0])

# def scanline_fill(vertices):
#     vertices_count = len(vertices)

#     for i in range(vertices_count):
#         x1, y1 = vertices[i]
#         x2, y2 = vertices[(i + 1) % vertices_count]


# Wand is used to find read the image from the user ie checks the height width from file name
# flip() ;image.clone()


# WAP to find implement secondary  fill algorithm



# WAP to find implement flood  fill algorithm



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




#c) scaling 
# import matplotlib.pyplot as plt 
# x1, y1 = map(int, input("Enter the first coordinate of the line: ").split(" "))
# x2, y2 = map(int, input("Enter the second coordinate of the line: ").split(" "))
# tx, ty = map(int, input("Enter the scaling coordinate of the line: ").split(" "))

# var1 = x1 * tx
# var = y1 * ty

# var2 = x2 * tx
# var3 = y2 * ty

# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")

# plt.plot([x1, x2], [y1, y2], label='Original Line')
# plt.plot([var1, var2], [var, var3], label='Translated Line')
# plt.legend()
# plt.title("Subash Katwal")
# plt.grid(True)
# plt.show()





# import matplotlib.pyplot as plt 
# def forLine(x1,y1,x2,y2,tx,ty):
#     x1, y1 = map(int, input("Enter the first coordinate of the line: ").split(" "))
#     x2, y2 = map(int, input("Enter the second coordinate of the line: ").split(" "))
#     tx, ty = map(int, input("Enter the scaling coordinate of the line: ").split(" "))

#     var1 = x1 * tx
#     var = y1 * ty

#     var2 = x2 * tx
#     var3 = y2 * ty
#     return forLine
#     # plt.xlabel("X-axis")
#     # plt.ylabel("Y-axis")

#     # plt.plot([x1, x2], [y1, y2], label='Original Line')
#     # plt.plot([var1, var2], [var, var3], label='Translated Line')
    
# def forFigure(x1,y1,x2,tx,ty):
#         x1, y1 = map(int, input("Enter the first coordinate of the line: ").split(" "))
#         x2, y2 = map(int, input("Enter the second coordinate of the line: ").split(" "))
#         tx, ty = map(int, input("Enter the scaling coordinate of the line: ").split(" "))
        
    
# plt.legend()
# plt.show()


# import matplotlib.pyplot as plt 
# import numpy as np 

# x1,y1=map(int, input("enter the coordinates of x1 and y1 ").split(" "))
# x2,y2=map(int, input("enter the coordinates of x1 and y1 ").split(" "))
# tx,ty=map(int,input("Enter the scaling factor ").split(" "))

# x=x1*tx
# y=y1*ty 


# xy_changed=np.array([[1,0,-x1],
#                      [0,1,-y1],
#                      [0,0,1]])
# tx_ty_changed=np.array([tx,ty,1])
# plt.plot(tx_ty_changed)
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.show()
# print(f"Point back to origin {xy_changed}")
# print("point after scaling is : ")
# result=np.dot(xy_changed,tx_ty_changed)
# print(result)

# result=np.array([[1,0,-x1],
#                      [0,1,-y1],
#                      [0,0,1]])
# plt.plot(result)
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.show()


# #b rotation 

# import matplotlib.pyplot as plt 
# import math
# import numpy as np 

# def calculate_sin_cos(angle_in_degree):
#     angle_in_radian=math.radians(angle_in_degree)
    
#     sin=math.sin(angle_in_radian)
#     cos=math.cos(angle_in_radian)
    
#     return sin,cos 
# sin_angle,cos_angle=map(int,input("Enter the angle for sin and cos respectively : ").split(" "))
# x,y=map (int ,input("Enter the coordinates : ").split(" "))
# sin,cos=calculate_sin_cos(sin_angle)

# matrix_1=np.array([x,y])
# # calculate_sin_cos(sin_angle,cos_angle)
# matrix2=np.array([[cos*cos_angle, -sin*sin_angle],
#                     [sin *sin_angle, cos*cos_angle]])

# result=np.dot(matrix_1,matrix2)
# print(result)
# vectors = [matrix_1, matrix2[:, 0], matrix2[:, 1]]
# colors = ['r', 'b', 'g']
# labels = ['Matrix_1', 'Matrix_2_col1', 'Matrix_2_col2']

# # Plotting vectors
# # plt.plot(vectors, colors, labels)

# plt.xlabel("X-label")
# plt.ylabel("Y-label")
# plt.show()



#rotation
# import matplotlib.pyplot as plt
# import math
# import numpy as np

# def calculate_sin_cos(angle_in_degree):
#     angle_in_radian = math.radians(angle_in_degree)
#     sin = math.sin(angle_in_radian)
#     cos = math.cos(angle_in_radian)
#     return sin, cos

# angle = float(input("Enter the angle in degrees: "))
# sin, cos = calculate_sin_cos(angle)

# x, y = map(int, input("Enter the coordinates: ").split(" "))
# matrix_1 = np.array([x, y])

# matrix2 = np.array([[cos, -sin],
#                     [sin, cos]])

# result = np.matmul(matrix_1, matrix2)

# print("Result after rotation:", result)

# # Plotting vectors
# vectors = [matrix_1, result]
# colors = ['r', 'b']
# labels = ['Matrix_1', 'Result']

# for vector, color, label in zip(vectors, colors, labels):
#     plt.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color=color, label=label)

# plt.xlabel("X-label")
# plt.ylabel("Y-label")
# plt.title("Subash Katwal")
# plt.legend()
# plt.grid()
# plt.show()

#b rotation
# import matplotlib.pyplot as plt
# import math
# import numpy as np

# def calculate_sin_cos(angle_in_degree):
#     angle_in_radian = math.radians(angle_in_degree)
#     sin = math.sin(angle_in_radian)
#     cos = math.cos(angle_in_radian)
#     return sin, cos

# angle = float(input("Enter the angle in degrees: "))
# sin, cos = calculate_sin_cos(angle)

# start_x, start_y = map(int, input("Enter the starting coordinates: ").split(" "))
# end_x, end_y = map(int, input("Enter the ending coordinates: ").split(" "))

# start_vector = np.array([start_x, start_y])
# end_vector = np.array([end_x, end_y])

# rotation_matrix = np.array([[cos, -sin],
#                             [sin, cos]])

# print("Matrix before rotation:")
# print("Start Vector:\n", start_vector)
# print("End Vector:\n", end_vector)

# result = np.matmul(start_vector, rotation_matrix)

# print("\nMatrix after rotation:")
# print("Result Vector:\n", result)



# print("Result after rotation:", result)

# # Plotting vectors
# vectors = [start_vector, end_vector, result]
# colors = ['r', 'g', 'b']
# labels = ['Start Vector', 'End Vector', 'Result']

# for vector, color, label in zip(vectors, colors, labels):
#     plt.quiver(0, 0, vector[0], vector[1], angles='xy', scale_units='xy', scale=1, color=color, label=label)

# plt.xlabel("X-label")
# plt.ylabel("Y-label")
# plt.legend()
# plt.grid()
# plt.show()



