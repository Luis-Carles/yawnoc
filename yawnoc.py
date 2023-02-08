import actualize as a
import music as m
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time
import random

###Parameters Input Control

if len(sys.argv) != 4:
    print("\nERROR: wrong parameters, usage: \n\npython yawnoc.py"
    + "\n\t[musical Approach] "
    + "\n\t[window's Dimension] "
    + "\n\t[universe's Dimension]")
    exit(-1)

if (int(sys.argv[1])<0) or (int(sys.argv[1])>5):
    print("\nERROR: wrong musical approach, \n\nmust use a"
    +"\n\tnumber between 0-5 for:"
    +"\n\t[musical approach]"
    + "\n\t0: Casual (No Music)"
    + "\n\t1: Melodic Piano"
    + "\n\t2: Armonic Piano"
    + "\n\t3: Rhytmic & Drums"
    + "\n\t4: Melodic Violin"
    + "\n\t5: Melodic Bass")
    exit(-1)

if ((int(sys.argv[2])%10)!=0) or ((int(sys.argv[3])%10)!=0):
    print("\nERROR: wrong dimensions, \n\nmust use a"
    +"\n\tmultiple of 10 for:"
    +"\n\t[window's Dimension] "
    +"\n\t[universe's Dimension]")
    exit(-1)



### Initial declarations and global variables

speed= 0.5         #Standard speed for music approaches   
stop = True
paintGrid = True

mApproach = int(sys.argv[1])

if(mApproach==0):  #Standard speed for casual approach
    speed = 0.1

# Window dimensions     
dimXwindow = int(sys.argv[2])    #standard: 800
dimYwindow = int(sys.argv[2])

# Universe dimensions   
dimXgrid = int(sys.argv[3])      #standard: 100
dimYgrid = int(sys.argv[3])

# Cell dimensions
cellSize = dimYwindow / dimYgrid

# Colors
ORANGE = [1.0, 0.50, 1.0]
BLUE = [0.0, 0.0, 1.0]
GREEN = [0.0, 1.0, 0.0]
RED = [1.0, 0.0, 0.0]
YELLOW = [1.0, 1.0, 0.0]
BLACK = [0.0, 0.0, 0.0]
WHITE = [1.0, 1.0, 1.0]
GRAY = [0.15, 0.15, 0.15]
PINK = [1.0, 0.0, 1.0]
PURPLE = [0.5, 0.0, 1.0]
BROWN = [0.50,0.25,0]

winColor = BLACK
gridColor = GRAY

if(mApproach==1) or (mApproach==0) : #Melodic Piano Approach / Casual
 cellColor = PINK

if(mApproach==2):     #Armonic Approach
 cellColor = ORANGE

if(mApproach==3):     #Rhytmic Approach
 cellColor = YELLOW

if(mApproach==4):     #Melodic Violin Approach
 cellColor = WHITE

if(mApproach==5):     #Bass Approach
 cellColor = BROWN



### Big Bang

universe = [[ 0  for i in range(dimXgrid)] for j in range(dimYgrid)]

# Gridding the universe              
def grid():
    global paintGrid

    glColor3fv(gridColor)
    glLineWidth(0.001)
    glBegin(GL_LINES)

    xFrac = dimXwindow / dimXgrid
    yFrac = - dimYwindow / dimYgrid

    i = 0
    while i <= dimXwindow:
        glVertex2f(i,0)
        glVertex2f(i,-dimYwindow)
        i += xFrac

    j = 0
    while j >= -dimYwindow:
        glVertex2f(0,j)
        glVertex2f(dimXwindow,j)
        j += yFrac
    
    glEnd()

# Creating the window
def init():
    global winColor
    glClearColor(winColor[0], winColor[1], winColor[2], 1)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D( 0, dimXwindow, -dimYwindow, 0 )    



###  Drawing actions

# Cell's position
def getCell(posX, posY):
    x = int(posX / (dimXwindow / dimXgrid))
    y = int(posY / (dimYwindow / dimYgrid))
    return x,y

# Inverts the y axis maintaining consistency with openGL behaviour
def getCellonScreen(xCell, yCell):
    x = int(xCell * (dimXwindow / dimXgrid))
    y = -1 * int(yCell * (dimYwindow / dimYgrid))
    return x,y

def drawSquare(xPos, yPos):
    global cellColor

    glColor3fv(cellColor)
    glBegin(GL_POLYGON)
    glVertex2f(xPos, yPos)
    glVertex2f(xPos + cellSize, yPos)
    glVertex2f(xPos + cellSize, yPos - cellSize)
    glVertex2f(xPos, yPos - cellSize)
    glEnd()

# Draw alive cells in the universe
def drawLivings():
    for j in range(dimYgrid):
        for i in range(dimXgrid):
            if universe[j][i] == 1:
                x,y = getCellonScreen(i,j)
                drawSquare(x,y)
    glFlush()




### Runtime actions:     
    
def standardKeyboard(key, x, y):
    global stop
    global paintGrid
    global universe
    global winColor
    global cellColor

    # Clear "c"
    if key == b'c' or key == b'C':
        universe = [[ 0  for i in range(dimXgrid)] for j in range(dimYgrid)]
    
    # Draw/Undraw the grid "g"
    elif key == b'g':
        paintGrid = not paintGrid

    # Blizzard " " 
    elif key == b' ':
        stop = not stop

    # Randomize "r"
    elif key == b'r' or key == b'R': 
        universe = [[ random.choice([0,0,0,1,1,1]) for i in range(dimXgrid)] for j in range(dimYgrid)]
    
    
def aditionalKeyboard(key, x, y):
    global speed
    global universe

    # Next state  "⇨"
    if key == GLUT_KEY_RIGHT and stop:
        universe = a.nextState(universe)

    # Accelerate "⇧"
    if key == GLUT_KEY_UP:
        speed -= speed * 0.5
    
    # Decelerate "⇩"
    if key == GLUT_KEY_DOWN:
        speed += speed * 0.5
    
    glutPostRedisplay()

def standardMouse(button, state, x, y):
    global universe
    global stop

    # Playing God: creating life or destroying it
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN :
        xCell, yCell = getCell(x, y)
        previousState = universe[yCell][xCell]
        universe[yCell][xCell] = 1 if previousState == 0 else 0



### Main body of the game of life's loopeable execution
 
def main():
    global universe
    global stop

    glClear(GL_COLOR_BUFFER_BIT)

    if paintGrid:
        grid()

    drawLivings()

    # If music is on
    if(mApproach!=0):                                
     m.music(universe,mApproach,speed,mode,key)               

    if not stop:
        if(mApproach==0):
         time.sleep(speed) 

        universe = a.nextState(universe)
        glutPostRedisplay()

# OpenGL actions carried once
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB) 
glutInitWindowPosition(400,10)
glutInitWindowSize(dimXwindow,dimYwindow)
glutCreateWindow(b'Conways Game of Life')

init()
mode = random.randint(0,1)   ##-----> mode and key random for Armonic Approaches, can be forced 
key = random.randint(0,11)
# OpenGL loop for main() function and runtime actions
glutDisplayFunc(main) 
glutKeyboardFunc(standardKeyboard)
glutSpecialFunc(aditionalKeyboard)
glutMouseFunc(standardMouse)
glutMainLoop()







