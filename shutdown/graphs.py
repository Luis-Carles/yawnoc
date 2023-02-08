import actualize as a
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *



# Window dimensions     
dimXwindow = 400   #standard: 400
dimYwindow = 400

# Universe dimensions   
dimXgrid = 100      #standard: 100
dimYgrid = 100

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

# Gridding the universe              
def grid():

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

def drawSquare(xPos, yPos,cellColor):

    glColor3fv(cellColor)
    glBegin(GL_POLYGON)
    glVertex2f(xPos, yPos)
    glVertex2f(xPos + cellSize, yPos)
    glVertex2f(xPos + cellSize, yPos - cellSize)
    glVertex2f(xPos, yPos - cellSize)
    glEnd()

# Draw alive cells in the universe
def drawLivings(cellColor,universe):
    for j in range(dimYgrid):
        for i in range(dimXgrid):
            if universe[j][i] == 1:
                x,y = getCellonScreen(i,j)
                drawSquare(x,y,cellColor)
    glFlush()

# Draw dead Cells for void universe
def drawDead():
    for j in range(dimYgrid):
        for i in range(dimXgrid):
                x,y = getCellonScreen(i,j)
                drawSquare(x,y,BLACK)
    glFlush()





    




