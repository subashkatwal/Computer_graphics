
import glfw
from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np

# Window dimensions
window_width = 800
window_height = 600

# Vertices of the cube
cube_vertices = np.array([
    [-0.5, -0.5, 0.5], [0.5, -0.5, 0.5], [0.5, 0.5, 0.5], [-0.5, 0.5, 0.5],  # Front face
    [-0.5, -0.5, -0.5], [-0.5, 0.5, -0.5], [0.5, 0.5, -0.5], [0.5, -0.5, -0.5],  # Back face
    [-0.5, 0.5, -0.5], [-0.5, 0.5, 0.5], [0.5, 0.5, 0.5], [0.5, 0.5, -0.5],  # Top face
    [-0.5, -0.5, -0.5], [0.5, -0.5, -0.5], [0.5, -0.5, 0.5], [-0.5, -0.5, 0.5],  # Bottom face
    [0.5, -0.5, -0.5], [0.5, 0.5, -0.5], [0.5, 0.5, 0.5], [0.5, -0.5, 0.5],  # Right face
    [-0.5, -0.5, -0.5], [-0.5, -0.5, 0.5], [-0.5, 0.5, 0.5], [-0.5, 0.5, -0.5]  # Left face
], dtype=np.float32)

# Indices of vertices forming each face of the cube
cube_indices = np.array([
    0, 1, 2, 3,  # Front face
    4, 5, 6, 7,  # Back face
    8, 9, 10, 11,  # Top face
    12, 13, 14, 15,  # Bottom face
    16, 17, 18, 19,  # Right face
    20, 21, 22, 23,  # Left face
], dtype=np.uint32)

# Vertices of the window (simple rectangle)
window_vertices = np.array([
    [-0.5, -0.5, 0.0], [0.5, -0.5, 0.0], [0.5, 0.5, 0.0], [-0.5, 0.5, 0.0]
], dtype=np.float32)

# Indices of vertices forming the window rectangle
window_indices = np.array([0, 1, 2, 3], dtype=np.uint32)

# Initialize OpenGL
def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set clear color to white
    glEnable(GL_DEPTH_TEST)  # Enable depth testing

# Display function for cube
def display_cube():
    # Draw the cube
    glBegin(GL_QUADS)
    for i in range(0, len(cube_indices), 4):
        for j in range(4):
            glVertex3fv(cube_vertices[cube_indices[i + j]])
    glEnd()

# Display function for window (rectangle)
def display_window():
    # Draw the window
    glBegin(GL_QUADS)
    for i in range(len(window_indices)):
        glVertex3fv(window_vertices[window_indices[i]])
    glEnd()
import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

# Window dimensions
window_width = 800
window_height = 600

# Vertices of the cube
cube_vertices = np.array([
    [-0.5, -0.5, 0.5], [0.5, -0.5, 0.5], [0.5, 0.5, 0.5], [-0.5, 0.5, 0.5],  # Front face
    [-0.5, -0.5, -0.5], [-0.5, 0.5, -0.5], [0.5, 0.5, -0.5], [0.5, -0.5, -0.5],  # Back face
    [-0.5, 0.5, -0.5], [-0.5, 0.5, 0.5], [0.5, 0.5, 0.5], [0.5, 0.5, -0.5],  # Top face
    [-0.5, -0.5, -0.5], [0.5, -0.5, -0.5], [0.5, -0.5, 0.5], [-0.5, -0.5, 0.5],  # Bottom face
    [0.5, -0.5, -0.5], [0.5, 0.5, -0.5], [0.5, 0.5, 0.5], [0.5, -0.5, 0.5],  # Right face
    [-0.5, -0.5, -0.5], [-0.5, -0.5, 0.5], [-0.5, 0.5, 0.5], [-0.5, 0.5, -0.5]  # Left face
], dtype=np.float32)

# Indices of vertices forming each face of the cube
cube_indices = np.array([
    0, 1, 2, 3,  # Front face
    4, 5, 6, 7,  # Back face
    8, 9, 10, 11,  # Top face
    12, 13, 14, 15,  # Bottom face
    16, 17, 18, 19,  # Right face
    20, 21, 22, 23,  # Left face
], dtype=np.uint32)

# Vertices of the window (simple rectangle)
window_vertices = np.array([
    [-0.5, -0.5, 0.0], [0.5, -0.5, 0.0], [0.5, 0.5, 0.0], [-0.5, 0.5, 0.0]
], dtype=np.float32)

# Indices of vertices forming the window rectangle
window_indices = np.array([0, 1, 2, 3], dtype=np.uint32)

# Initialize OpenGL
def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set clear color to white
    glEnable(GL_DEPTH_TEST)  # Enable depth testing

# Display function for cube
def display_cube():
    # Draw the cube
    glBegin(GL_QUADS)
    for i in range(0, len(cube_indices), 4):
        for j in range(4):
            glVertex3fv(cube_vertices[cube_indices[i + j]])
    glEnd()

# Display function for window (rectangle)
def display_window():
    # Draw the window
    glBegin(GL_QUADS)
    for i in range(len(window_indices)):
        glVertex3fv(window_vertices[window_indices[i]])
    glEnd()

# Main function
def main():
    # Initialize GLFW
    if not glfw.init():
        return

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(window_width, window_height, "OpenGL Window", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    # Set up OpenGL
    init()

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Poll for and process events
        glfw.poll_events()

        # Set up view and projection matrices
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, window_width / window_height, 0.1, 100)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(3, 3, 3, 0, 0, 0, 0, 1, 0)

        # Draw the cube
        glColor3f(1.0, 0.0, 0.0)  # Red color for cube
        display_cube()

        # Draw the window
        glColor3f(0.0, 0.0, 1.0)  # Blue color for window
        display_window()

        # Swap front and back buffers
        glfw.swap_buffers(window)

    # Terminate GLFW
    glfw.terminate()

if __name__ == "__main__":
    main()
