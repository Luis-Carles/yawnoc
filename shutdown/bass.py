import graphs as g
import actualize as a
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
import time
import numpy as nm

import fluidsynth as fs
from mingus.containers import Note
sounds5 = "\TEK bass.sf2"
n= 0.080

### THREADING APPROACH
def main(states):

 ### Initial declarations and global variables
    cellColor = g.BROWN
    name = "808 Bass Instrumental"
    posX = g.dimXwindow
    posY = g.dimYwindow + 30

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

 s = fs.Synth(gain=0.8)
 s.start()
 ins = "..\soundfonts"+ sounds5
 soundfont = s.sfload(ins)
 s.program_select(0,soundfont,0,0)


 cellColor = g.BROWN
 name = "808 Bass Instrumental"
 posX = g.dimXwindow
 posY = g.dimYwindow + 30
    
 fileName = './states/bass/armonic bass '
 fileName2 = './states/bass/opening bass '
 file = fileName
 file2 = fileName2


 opSpeed = [[8,4,2],[2,2,2]]

 speeds2 = [[2,2,2],[2,2,2],[2,2,2],[2,2,2]]

 speedsOpeningChorus = [[4,2],[2,2,2]]

 ouSpeed =  [[3,1,1,1],[3,1,1,1],[8,8,8]]

 # Trap bass chords
 BbmChord = [int(Note("Bb", 2)),int(Note("Db", 3)),int(Note("F", 3))]
 FChord = [int(Note("F", 3)),int(Note("Ab", 3)),int(Note("C", 4))]

 bars = [[BbmChord,[0,0,0]],[FChord],[FChord],[FChord],[BbmChord,[0,0,0]],[FChord],[FChord,FChord,FChord]]

 speed = [[6,6],[2],[8],[2],[6,6],[2],[6,2,2]]


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


 # Bass sleeping during strings opening
 file2 = fileName2 + str(0) + '.txt'
 universe = nm.loadtxt(file2, dtype=int)

 for x in range(len(opSpeed)):
      for y in range(len(opSpeed[x])):
       #glutSetWindow(glutGetWindow())                     
       glClear(GL_COLOR_BUFFER_BIT)
       g.drawLivings(cellColor,universe)

       universe = a.nextState(universe)

       time.sleep(opSpeed[x][y]*0.063)
       time.sleep((opSpeed[x][y]/2)*0.063)

 # Looping through bass verse states
 for z in range(6):
      for x in range(len(bars)):
         file = fileName + str(x) + '.txt'
         universe = nm.loadtxt(file, dtype=int)

         for y in range(len(speed[x])):
            #glutSetWindow(glutGetWindow())                     
            glClear(GL_COLOR_BUFFER_BIT)
            g.drawLivings(cellColor,universe)

            universe = a.nextState(universe)

            if(int(bars[x][y][0])>0):      
               s.noteon(0,bars[x][y][0],80)
               s.noteon(0,bars[x][y][1],80)
               s.noteon(0,bars[x][y][2],80)

            time.sleep(speed[x][y]*n)

            if(int(bars[x][y][0])>0): 
               s.noteoff(0,bars[x][y][0])
               s.noteoff(0,bars[x][y][1])
               s.noteoff(0,bars[x][y][2])

            time.sleep((speed[x][y]/2)*n)

  # Sleeping through pizzicato states
 file2 = fileName2 + str(0) + '.txt'
 universe = nm.loadtxt(file2, dtype=int)

 #glutSetWindow(glutGetWindow())                     
 glClear(GL_COLOR_BUFFER_BIT)
 g.drawDead()

 for i in range(4):
      for x in range(len(speeds2)):
         for y in range(len(speeds2[x])):
            #glutSetWindow(glutGetWindow())                     
            glClear(GL_COLOR_BUFFER_BIT)
            g.drawLivings(cellColor,universe)

            universe = a.nextState(universe)

            time.sleep(speeds2[x][y]*0.063)

            time.sleep((speeds2[x][y]/2)*0.063)

  # Sleeping through chorus opening strings
 for x in range(len(speedsOpeningChorus)):
    for y in range(len(speedsOpeningChorus[x])):
       #glutSetWindow(glutGetWindow())                     
       glClear(GL_COLOR_BUFFER_BIT)
       g.drawLivings(cellColor,universe)

       universe = a.nextState(universe) 

       time.sleep(speedsOpeningChorus[x][y]*0.063)

       time.sleep((speedsOpeningChorus[x][y]/2)*0.063)


  # Looping through bass chorus states
 for z in range(3):
      for x in range(len(bars)):
         file = fileName + str(x) + '.txt'
         universe = nm.loadtxt(file, dtype=int)

         for y in range(len(speed[x])):
            #glutSetWindow(glutGetWindow())                     
            glClear(GL_COLOR_BUFFER_BIT)
            g.drawLivings(cellColor,universe)

            universe = a.nextState(universe)

            if(int(bars[x][y][0])>0):      
               s.noteon(0,bars[x][y][0],80)
               s.noteon(0,bars[x][y][1],80)
               s.noteon(0,bars[x][y][2],80)

            time.sleep(speed[x][y]*n)

            if(int(bars[x][y][0])>0): 
               s.noteoff(0,bars[x][y][0])
               s.noteoff(0,bars[x][y][1])
               s.noteoff(0,bars[x][y][2])

            time.sleep((speed[x][y]/2)*n)

 # Last bass pattern cut in half (changing sections)
 for x in range(2):
    file = fileName + str(x) + '.txt'
    universe = nm.loadtxt(file, dtype=int)

    for y in range(len(bars[x])):
       #glutSetWindow(glutGetWindow())                     
       glClear(GL_COLOR_BUFFER_BIT)
       g.drawLivings(cellColor,universe)

       universe = a.nextState(universe)

       if(int(bars[x][y][0])>0):      
          s.noteon(0,bars[x][y][0],80)
          s.noteon(0,bars[x][y][1],80)
          s.noteon(0,bars[x][y][2],80)

       time.sleep(speed[x][y]*n)

       if(int(bars[x][y][0])>0): 
          s.noteoff(0,bars[x][y][0])
          s.noteoff(0,bars[x][y][1])
          s.noteoff(0,bars[x][y][2])

       time.sleep((speed[x][y]/2)*n)

 # Bass sleeping during chorus outro
 file2 = fileName2 + str(0) + '.txt'
 universe = nm.loadtxt(file2, dtype=int)

 #glutSetWindow(glutGetWindow())                     
 glClear(GL_COLOR_BUFFER_BIT)
 g.drawDead()

 for x in range(len(ouSpeed)):
      for y in range(len(ouSpeed[x])):
       #glutSetWindow(glutGetWindow())                     
       glClear(GL_COLOR_BUFFER_BIT)
       g.drawLivings(cellColor,universe)

       universe = a.nextState(universe)

       time.sleep(ouSpeed[x][y]*0.063)
       time.sleep((ouSpeed[x][y]/2)*0.063)

 time.sleep(ouSpeed[2][0]*0.063)

 time.sleep((ouSpeed[2][0]/2)*0.063)

 s.delete()