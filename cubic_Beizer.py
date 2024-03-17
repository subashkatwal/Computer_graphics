import numpy as np
import matplotlib.pyplot as plt

def cubic_bezier(P0, P1, P2, P3, num_points=100):
    t = np.linspace(0, 1, num_points)
    bezier_curve = np.array([(1-t)**3 * P0[i] + 3*(1-t)**2 * t * P1[i] + 3*(1-t) * t**2 * P2[i] + t**3 * P3[i] for i in range(2)])
    return bezier_curve

# Example control points
P0 = np.array([0, 0])
P1 = np.array([1, 2])
P2 = np.array([3, 4])
P3 = np.array([5, 2])

# Generate cubic Bezier curve
curve = cubic_bezier(P0, P1, P2, P3)

# Plot control points and curve
plt.plot([P0[0], P1[0], P2[0], P3[0]], [P0[1], P1[1], P2[1], P3[1]], 'bo--', label='Control Points')
plt.plot(curve[0], curve[1], 'r-', label='Cubic Bezier Curve')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Cubic Bezier Curve')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
