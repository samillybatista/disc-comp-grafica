import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    glClearColor(0, 0, 0, 1) 
    glPointSize(5)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 10, 0, 10 )


def funcao_reta_bresenham():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_LINE_STRIP)
    glColor(1, 1, 1)
    
    x1, y1 = 2,3
    x2, y2 = 8,6
    dx, dy, p, yend, xend, xx, yy = 0,0,0,0,0,0,0
    const1, const2, directy, directx = 0,0,0,0

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    if dx > dy:
        p = 2*dy - dx
        const1 = 2*dy
        const2 = 2*(dy - dx)
        
        if x1 > x2:
            xx, yy = x2, y2
            xend = x1
            if y1 < y2:
                directy = -1
            else:
                directy = 1

        else:
            xx, yy = x1, y1
            xend = x2
            if y1 < y2:
                directy = 1
            else:
                directy = -1
        glVertex2f(xx, yy)
        while xx < xend:
            xx = xx +1
            if p < 0:
                p = p + const1
            else:
                yy = yy + directy
                p = p + const2                        
            glVertex2f(xx, yy)      
    else:
        p = 2*dx - dy
        const1 = 2*dx
        const2 = 2*(dx - dy)
        if y1 > y2:
            xx, yy = x2, y2
            yend = y1
            if x1 < x2:
                directx = -1
            else:
                directx = 1
        else:
            xx, yy = x1, y1
            yend = y2
            if x1 < x2:
                directx = 1
            else:
                directx = -1
            glVertex2f(xx, yy)
            while yy < yend:
                yy = yy + 1
                if p < 0:
                    p = p + const1
                else:
                    xx = xx + directx
                    p = p + const2
                glVertex2f(xx, yy)
    glEnd()
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(300, 300)
    glutCreateWindow(b"Rasterizacao reta - bresenham")
    init()
    glutDisplayFunc(funcao_reta_bresenham)
    glutMainLoop()
    
main()