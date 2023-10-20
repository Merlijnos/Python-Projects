import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

vertices = (
    (1, -1, -1),  # 0
    (1, 1, -1),  # 1
    (-1, 1, -1),  # 2
    (-1, -1, -1),  # 3
    (1, -1, 1),  # 4
    (1, 1, 1),  # 5
    (-1, -1, 1),  # 6
    (-1, 1, 1),  # 7
)

edges = (
    (0, 1),
    (1, 5),
    (5, 4),
    (4, 0),
    (1, 2),
    (6, 3),
    (2, 3),
    (2, 7),
    (7, 6),
    (0, 3),
    (4, 6),
    (5, 7),
    (0, 4),
    (1, 2),
    (5, 4),
    (6, 7),
)

colors = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 1),
    (0, 1, 1),
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 0, 0),
    (1, 1, 1),
    (0, 1, 1),
)

surfaces = (
    (0, 1, 5, 4),
    (1, 2, 7, 5),
    (7, 6, 3, 2),
    (4, 5, 7, 6),
    (0, 4, 6, 3),
    (0, 3, 2, 1),
)


def draw_cube():
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x += 1
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
    glEnd()

    glColor3fv((0, 0, 0))
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def set_projection(display):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (display[0] / display[1]), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0.0, 0.0, -5)


def calculate_rpm(prev_time, rotation_angle):
    current_time = pygame.time.get_ticks()
    time_elapsed = current_time - prev_time
    if time_elapsed > 0:
        rpm = (rotation_angle / 360.0) * (1000.0 / time_elapsed) * 60.0
        return rpm
    else:
        return 0


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glEnable(GL_DEPTH_TEST)
    set_projection(display)

    rotation_angle = 0
    rotation_speed = 2  # Set initial rotation speed

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        rotation_angle = (rotation_angle + rotation_speed) % 360  # Rotate automatically

        glLoadIdentity()  # Reset the rotation
        glTranslatef(0.0, 0.0, -5)  # Move the cube back to its original position
        glRotatef(rotation_angle, 3, 1, 1)  # Apply the new rotation around the y-axis

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_cube()

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
