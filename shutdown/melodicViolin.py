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
sounds4 = "\R-violin.sf2"
sounds6 = "\pizzicato2.sf2"
n= 0.063

### THREADING APPROACH
def main(states):

 ### Initial declarations and global variables
    cellColor = g.WHITE
    name = "Violin Instrumental"
    posX = 0
    posY = g.dimYwindow +30

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

 s = fs.Synth(gain=0.1)
 s.start()
 ins = "..\soundfonts"+ sounds4
 soundfont = s.sfload(ins)
 s.program_select(0,soundfont,0,0)


 cellColor = g.WHITE
 name = "Violin Instrumental"
 posX = 0
 posY = g.dimYwindow +30
    
 fileName = './states/violin/melodic violin '
 fileName2 = './states/violin/opening violin '
 fileName3 = './states/violin/pizzicatos '
 fileName4 = './states/violin/outro violin '
 fileName5 = './states/violin/opening chorus '
 file = fileName
 file2 = fileName2
 file3 = fileName3
 file4 = fileName4
 file5 = fileName5

 opening = [[int(Note("F", 5)),int(Note("Bb", 5)),int(Note("Bb", 5))],[int(Note("F", 6)),int(Note("F", 6)),int(Note("Eb", 6))]]                          

 speedsOpening = [[8,4,2],[2,2,2]]

 openingChorus = [[int(Note("Bb", 5)),int(Note("Bb", 5))],[int(Note("F", 6)),int(Note("F", 6)),int(Note("Eb", 6))]]

 speedsOpeningChorus = [[4,2],[2,2,2]]

 pattern1 = [[int(Note("Db", 6)),int(Note("Db", 6)),int(Note("C", 6))],[int(Note("Bb", 5)),int(Note("A", 5)),int(Note("Bb", 5))],
 [int(Note("C", 6)),int(Note("F", 5)),int(Note("F", 5))],[int(Note("Gb", 5)),int(Note("F", 5)),int(Note("Eb", 5))]]

 speeds1 = [[2,2,2],[2,2,2],[2,2,2],[2,2,2]]

 pattern2 = [[int(Note("Bb", 4)),int(Note("Bb", 4)),int(Note("Db", 5))],[int(Note("F", 5)),int(Note("Db", 5)),int(Note("Bb", 4))],
 [int(Note("A", 4)),int(Note("Ab", 4)),int(Note("C", 5))],[int(Note("F", 5)),int(Note("C", 5)),int(Note("Ab", 4))]]

 speeds2 = [[2,2,2],[2,2,2],[2,2,2],[2,2,2]]

 outro = [[int(Note("F", 5))],[int(Note("Bb", 5)),int(Note("Db", 6)),int(Note("F", 6))],
 [int(Note("F", 5))],[int(Note("A", 5)),int(Note("C", 6)),int(Note("F", 6))],               
 [int(Note("Bb", 4)),int(Note("Db", 5)),int(Note("F", 5))]]

 speedsOutro = [[3],[1,1,1],[3],[1,1,1],[8,8,8]]


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

 ### Intro and verse
 
   # Looping through opening strings states
 for x in range(len(opening)):
    file2 = fileName2 + str(x) + '.txt'
    universe = nm.loadtxt(file2, dtype=int)

    for y in range(len(speedsOpening[x])):
       #glutSetWindow(glutGetWindow())                     
       glClear(GL_COLOR_BUFFER_BIT)
       g.drawLivings(cellColor,universe)

       universe = a.nextState(universe)
       
       s.noteon(0,opening[x][y],80)

       time.sleep(speedsOpening[x][y]*n)

       s.noteoff(0,opening[x][y])

       time.sleep((speedsOpening[x][y]/2)*n)


 # Looping through leitmotiv states
 for z in range(12):
      for x in range(len(speeds1)):
         file = fileName + str(x) + '.txt'
         universe = nm.loadtxt(file, dtype=int)

         for y in range(len(pattern1[x])):
            #glutSetWindow(glutGetWindow())                     
            glClear(GL_COLOR_BUFFER_BIT)
            g.drawLivings(cellColor,universe)

            universe = a.nextState(universe)
            
            s.noteon(0,pattern1[x][y],80)

            time.sleep(speeds1[x][y]*n)

            s.noteoff(0,pattern1[x][y])

            time.sleep((speeds1[x][y]/2)*n)

 s.delete()
 
 ###Pizzicatos

 s = fs.Synth(gain=0.3)
 s.start()
 ins = "..\soundfonts"+ sounds6         
 soundfont = s.sfload(ins)
 s.program_select(0,soundfont,0,45)


  # Looping through pizzicato states
 for i in range(4):
      for x in range(len(speeds2)):
         file3 = fileName3 + str(x) + '.txt'
         universe = nm.loadtxt(file3, dtype=int)

         for y in range(len(speeds2[x])):
            #glutSetWindow(glutGetWindow())                     
            glClear(GL_COLOR_BUFFER_BIT)
            g.drawLivings(cellColor,universe)

            universe = a.nextState(universe)
            
            s.noteon(0,pattern2[x][y],80)

            time.sleep(speeds2[x][y]*n)

            s.noteoff(0,pattern2[x][y])

            time.sleep((speeds2[x][y]/2)*n)        
 
 s.delete()

 ### Chorus

 s = fs.Synth(gain=0.1)
 s.start()
 ins = "..\soundfonts"+ sounds4
 soundfont = s.sfload(ins)
 s.program_select(0,soundfont,0,0)
 

  # loopong through opening strings
 for x in range(len(openingChorus)):
    file5 = fileName5 + str(x) + '.txt'
    universe = nm.loadtxt(file5, dtype=int)

    for y in range(len(speedsOpeningChorus[x])):
       #glutSetWindow(glutGetWindow())                     
       glClear(GL_COLOR_BUFFER_BIT)
       g.drawLivings(cellColor,universe)

       universe = a.nextState(universe)
       
       s.noteon(0,openingChorus[x][y],80)  

       time.sleep(speedsOpeningChorus[x][y]*n)

       s.noteoff(0,openingChorus[x][y])

       time.sleep((speedsOpeningChorus[x][y]/2)*n)       


  # Looping through chorus states
 for j in range(7):
      for x in range(len(speeds1)):
         file = fileName + str(x) + '.txt'
         universe = nm.loadtxt(file, dtype=int)

         for y in range(len(speeds1[x])):
            #glutSetWindow(glutGetWindow())                     
            glClear(GL_COLOR_BUFFER_BIT)
            g.drawLivings(cellColor,universe)

            universe = a.nextState(universe)
            
            s.noteon(0,pattern1[x][y],80)

            time.sleep(speeds1[x][y]*n)

            s.noteoff(0,pattern1[x][y])

            time.sleep((speeds1[x][y]/2)*n)

 # Chorus Outro featuring i-V-i 
 for l in range(len(outro)-1):
      file4 = fileName4 + str(x) + '.txt'
      universe = nm.loadtxt(file4, dtype=int)

      for m in range(len(outro[l])):

       s.noteon(0,outro[l][m],80)

       time.sleep(speedsOutro[l][m]*n)

       s.noteoff(0,outro[l][m])

       time.sleep((speedsOutro[l][m]/2)*n)

 file4 = fileName4 + str(5) + '.txt'
 universe = nm.loadtxt(file4, dtype=int)
 #glutSetWindow(glutGetWindow())                     
 glClear(GL_COLOR_BUFFER_BIT)
 g.drawLivings(cellColor,universe)

 s.noteon(0,outro[4][0],80)
 s.noteon(0,outro[4][1],80)
 s.noteon(0,outro[4][2],80)

 time.sleep(speedsOutro[4][0]*n)

 s.noteoff(0,outro[4][0])
 s.noteoff(0,outro[4][1])
 s.noteoff(0,outro[4][2])

 time.sleep((speedsOutro[4][0]/2)*n)

 s.delete() 