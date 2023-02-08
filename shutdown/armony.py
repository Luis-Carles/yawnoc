import graphs as g
import actualize as a
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
import time

def main(states):

 ### Initial declarations and global variables
    cellColor = g.ORANGE
    name = "Armonic"
    posX = 2* g.dimXwindow
    posY = 0

    ### Big Bang
    universe = [[ 0  for i in range(g.dimXgrid)] for j in range(g.dimYgrid)]
    universe = [[ random.choice([0,0,0,1,1,1]) for i in range(g.dimXgrid)] for j in range(g.dimYgrid)]

    speed=0.30

    # OpenGL actions carried once per universe
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB) 
    glutInitWindowPosition(posX,posY)
    glutInitWindowSize(g.dimXwindow,g.dimYwindow)
    glutCreateWindow(name)

    g.init()
    g.grid()

    # Loop
  
    for x in range(states):
     #glutSetWindow(glutGetWindow())                   
     glClear(GL_COLOR_BUFFER_BIT)

     g.drawLivings(cellColor,universe)
     time.sleep(speed)

     universe = a.nextState(universe)