import numpy as np
import matplotlib.pyplot as plt

# Define the region codes
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

# Define the window coordinates
x_min, x_max = 50, 200
y_min, y_max = 50, 200

# Function to compute the region code for a point
def compute_code(x, y):
    code = INSIDE
    if x < x_min:
        code |= LEFT
    elif x > x_max:
        code |= RIGHT
    if y < y_min:
        code |= BOTTOM
    elif y > y_max:
        code |= TOP
    return code

# Function to clip the line using Cohen-Sutherland algorithm
def cohen_sutherland_line_clip(x1, y1, x2, y2):
    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)
    
    accept = False
    
    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break
        elif code1 & code2 != 0:
            break
        else:
            x = 0
            y = 0
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2
                
            if code_out & TOP:
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min
                
            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2)
    
    if accept:
        plt.plot([x1, x2], [y1, y2], 'r')
    else:
        print("Line rejected")

# Define the line coordinates
x1, y1 = 20, 30
x2, y2 = 250, 150

# Plotting the window
plt.plot([x_min, x_max, x_max, x_min, x_min], [y_min, y_min, y_max, y_max, y_min], 'b--')

# Plotting the original line
plt.plot([x1, x2], [y1, y2], 'g')

# Clipping and plotting the line
cohen_sutherland_line_clip(x1, y1, x2, y2)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Cohen-Sutherland Line Clipping')
plt.grid(True)
plt.show()
