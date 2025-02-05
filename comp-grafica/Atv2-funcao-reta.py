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

def funcao_reta_analitico():
  glClear(GL_COLOR_BUFFER_BIT)
  glBegin(GL_LINE_STRIP)
  glColor(1, 1, 1)

  x1, y1 = 2,3
  x2, y2 = 8,6

  x, y, ix, iy = 0,0,0,0
  m, b = 0,0

  if x1 > x2:
      ix = x1
      iy = y1
      x1 = x2
      y1 = y2
      x2 = ix
      y2 = iy

  if x1 == x2:
      while y1 <= y2:
          glVertex2f(x1, y1)
          y1 = y1 + 1

  else:
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    x = x1

    while x <= x2:
        y = math.ceil(m * x) + b
        glVertex2f(x, y)
        x = x + 1
  glEnd()
  glFlush()

def main():
  glutInit()
  glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
  glutInitWindowSize(300, 300)
  glutCreateWindow(b"Rasterizacao reta - analitico")
  init()
  glutDisplayFunc(funcao_reta_analitico) 
  glutMainLoop()

main()