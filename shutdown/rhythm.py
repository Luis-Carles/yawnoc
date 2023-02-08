import graphs as g
import actualize as a
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
import time
import numpy as nm

import  pygame 
from pygame import mixer
sounds3 = "\drums"
n= 0.062

### THREADING APPROACH
def main(states):

 ### Initial declarations and global variables
    cellColor = g.YELLOW
    name = "Rhytmic Base"
    posX = g.dimXwindow
    posY = 0
    
    ### Big Bang
    universe = [[ 0  for i in range(g.dimXgrid)] for j in range(g.dimYgrid)]
    universe = [[ random.choice([0,0,0,1,1,1]) for i in range(g.dimXgrid)] for j in range(g.dimYgrid)]

    speed=0.18

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

### NO-THREADING APPROACH   
def main2():
 ### Initial declarations and global variables

 pygame.init()
    
 ins = "..\soundfonts"+ sounds3
 bassDrum = mixer.Sound(ins+"\BassDrum.WAV")
 bassDrum.set_volume(0.5)
 snareDrum = mixer.Sound(ins+"\SnareDrum.WAV")
 snareDrum.set_volume(0.5)
 hihat = mixer.Sound(ins+"\Hihat.WAV")
 hihat.set_volume(0.5)
 finalDrum = mixer.Sound(ins+"\FinalDrum.WAV")
 finalDrum.set_volume(0.5)


 cellColor = g.YELLOW
 name = "Rhytmic Drums Base"
 posX = g.dimXwindow
 posY = 0
    
 fileName = './states/drums/drums '
 file = fileName

 pattern = [[12,6,3,3,3,3],
 [bassDrum,hihat,hihat],[snareDrum,hihat,hihat],[hihat,hihat,bassDrum],[bassDrum,snareDrum,hihat],[bassDrum,hihat,hihat],
 [bassDrum,hihat,hihat],[snareDrum,hihat,hihat],[hihat,bassDrum,hihat],[bassDrum,snareDrum,hihat,snareDrum],
 [bassDrum,hihat,hihat],[snareDrum,hihat,hihat],[hihat,hihat,bassDrum],[bassDrum,snareDrum,hihat],[bassDrum,hihat,hihat],
 [bassDrum,hihat,hihat],[snareDrum,hihat,hihat],[hihat,bassDrum,hihat],[bassDrum,snareDrum,hihat,snareDrum],
 [bassDrum,hihat,hihat],[snareDrum,hihat,hihat],[hihat,hihat,bassDrum],[bassDrum,snareDrum,hihat],[bassDrum,hihat,hihat],
 [bassDrum,hihat,hihat],[snareDrum,hihat,hihat],[hihat,bassDrum,hihat],[bassDrum,snareDrum,hihat,snareDrum],
 [bassDrum,hihat,hihat],[snareDrum,hihat,hihat],[hihat,hihat,bassDrum],[bassDrum,snareDrum,hihat],[bassDrum,hihat,hihat],
 [bassDrum,hihat,hihat],[finalDrum,hihat,hihat],[hihat,bassDrum,hihat],[bassDrum,snareDrum,hihat,snareDrum],
 [bassDrum,hihat,hihat],[snareDrum,hihat,hihat],[hihat,hihat,bassDrum],[bassDrum,snareDrum,hihat],[bassDrum,hihat,hihat],
 [bassDrum,hihat,hihat],[snareDrum,hihat,hihat],[hihat,bassDrum,hihat],[bassDrum,snareDrum,hihat,snareDrum],
 [bassDrum,hihat,hihat],[snareDrum,hihat,hihat],[hihat,hihat,bassDrum],[bassDrum,snareDrum,hihat],[bassDrum,hihat,hihat],
 [bassDrum,hihat,hihat],[finalDrum,hihat,hihat],[hihat,bassDrum,hihat],[bassDrum,snareDrum,hihat,snareDrum],             
 [hihat,hihat,hihat],[snareDrum,hihat,hihat],[hihat,hihat,hihat],[snareDrum,hihat,hihat],[hihat,hihat],                    
 [hihat,hihat,hihat],[snareDrum,hihat,hihat],[hihat,hihat,hihat],[hihat,snareDrum,hihat,snareDrum],    
 [hihat,hihat,hihat],[snareDrum,hihat,hihat],[hihat,hihat,hihat],[snareDrum,hihat,hihat],[hihat,hihat], 
 [hihat,hihat,hihat],[snareDrum,hihat,hihat],   
 [6,3,3,3,3,3,3,3,3,3,1], 
 [bassDrum,hihat,hihat],[snareDrum,hihat,hihat],[bassDrum,bassDrum,finalDrum],[hihat,bassDrum,hihat,hihat], 
 [bassDrum,hihat,hihat],[snareDrum,hihat,bassDrum],[hihat,bassDrum,finalDrum],[hihat,snareDrum],            
 [bassDrum,hihat,hihat],[snareDrum,hihat,hihat],[hihat,hihat,bassDrum],[bassDrum,snareDrum],[hihat,bassDrum,hihat], 
 [bassDrum,hihat,hihat],[snareDrum,hihat,hihat],[hihat,bassDrum,hihat],[bassDrum,snareDrum,hihat,snareDrum],  
 [bassDrum,hihat,hihat],[snareDrum,hihat,hihat],[bassDrum,bassDrum,finalDrum],[hihat,bassDrum,hihat,hihat], 
 [bassDrum,hihat,hihat],[snareDrum,hihat,hihat],[bassDrum,hihat,bassDrum],[finalDrum,hihat,snareDrum],      
 [bassDrum,hihat,hihat],[snareDrum,hihat,hihat],[hihat,hihat,bassDrum],[bassDrum,snareDrum,hihat],[bassDrum,hihat,hihat],
 [4.5,2,2,2,4.5,2,2,2,12,6,1],[finalDrum]]                          

 speeds = [[12,6,3,3,3,3],                                                   # Intro and verse
 [3,3,3],[3,3,1],[1,4,3],[3,3,3],[1,1,1],[3,3,3],[3,3,3],[3,1,2],[3,3,3,3],  
 [3,3,3],[3,3,1],[1,4,3],[3,3,3],[1,1,1],[3,3,3],[3,3,3],[3,1,2],[3,3,3,3],
 [3,3,3],[3,3,1],[1,4,3],[3,3,3],[1,1,1],[3,3,3],[3,3,3],[3,1,2],[3,3,3,3],
 [3,3,3],[3,3,1],[1,4,3],[3,3,3],[1,1,1],[3,3,3],[3,3,3],[3,1,2],[3,3,3,3],
 [3,3,3],[3,3,1],[1,4,3],[3,3,3],[1,1,1],[3,3,3],[3,3,3],[3,1,2],[3,3,3,3],
 [3,3,3],[3,3,1],[1,4,3],[3,3,3],[1,1,1],[3,3,3],[3,3,3],[3,1,2],[3,3,3,3],            
 [3,3,3],[3,3,2],[4,3,3],[3,3,1],[1,1],                                      # Pizzicatos
 [3,3,3],[3,3,3],[3,1,2],[3,3,3,3],                                              
 [3,3,3],[3,3,2],[4,3,3],[3,3,1],[1,1],
 [3,3,3],[3,3,3],
 [6,3,3,3,3,3,3,3,3,3,3],                                                                # Chorus
 [3,3,3],[3,3,6],[3,3,3],[3,1,1,1],
 [3,3,3],[6,6,1],[2,3,3],[3,3],
 [3,3,3],[3,3,1],[1,4,3],[3,3],[3,2,1],
 [3,3,3],[3,3,3],[3,1,2],[3,3,3,3],
 [3,3,3],[3,3,6],[3,3,3],[3,1,1,1],
 [3,3,3],[3,3,6],[1,2,3],[3,3,3],
 [3,3,3],[3,3,1],[1,4,3],[3,3,3],[1,1,1],
 [4.5,2,2,2,4.5,2,2,2,12,6,1],[3]]                                         # i-V-i

 ### Big Bang
 universe = [[ 0  for i in range(g.dimXgrid)] for j in range(g.dimYgrid)]
    
 # OpenGL actions carried once per universe
 glutInit(sys.argv)
 glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB) 
 glutInitWindowPosition(posX,posY)
 glutInitWindowSize(g.dimXwindow,g.dimYwindow)
 glutCreateWindow(name)

 g.init()
 g.grid()

 # Looping through states
 for x in range(len(speeds)):
    file = fileName + str(x) + '.txt'
    universe = nm.loadtxt(file, dtype=int)

    for y in range(len(speeds[x])):
       #glutSetWindow(glutGetWindow())                     
       glClear(GL_COLOR_BUFFER_BIT)
       g.drawLivings(cellColor,universe)

       universe = a.nextState(universe)
       
       if(x!=0)and(x!=71)and(x!=102):
          pattern[x][y].play()

       if(x!=0)and(x!=102):
          time.sleep(speeds[x][y]*n)
       else:
          time.sleep(speeds[x][y]*0.063)


