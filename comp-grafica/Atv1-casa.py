from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window_height = 300
window_width = 300
window_title = b"Renderizar ponto com OpenGL"

telhado = [
    [-0.3,0],
    [0, 0.4],
    [0.3,0],
    ]
chao = [
    [-0.3,0],
    [0.3,0],
    [0.3, -0.5],
    [-0.3, -0.5],
    ]
porta = [
    [-0.2, -0.5],
    [-0.2, -0.2],
    [0,-0.2],
    [0, -0.5],
    ]
janela = [
    [0.1, -0.4],
    [0.1, -0.2],
    [0.2, -0.2],
    [0.2, -0.4],
    ]


def init():
    glClearColor(0, 0, 0, 1)
    glPointSize(5)

def render():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.0, 0.9)
    
    
    glBegin(GL_LINE_LOOP)
    for v in telhado:
        glVertex2fv(v)
    glEnd()

    glBegin(GL_LINE_LOOP)
    for v in chao:
        glVertex2fv(v)
    glEnd()

    glBegin(GL_LINE_LOOP)
    for v in porta:
        glVertex2fv(v)
    glEnd()

    glBegin(GL_LINE_LOOP)
    for v in janela:
        glVertex2fv(v)
    glEnd()

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(window_width, window_height)
    glutCreateWindow(window_title)
    init()
    glutDisplayFunc(render)
    glutMainLoop()

main()