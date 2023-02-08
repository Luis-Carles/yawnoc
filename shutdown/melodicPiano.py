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
sounds = "\yamahap45.sf2"
n= 0.077

### THREADING APPROACH
def main(states):

 ### Initial declarations and global variables
    cellColor = g.PINK
    name = "Vocal melodies"
    posX = 0
    posY = 0

    ### Big Bang
    universe = [[ 0  for i in range(g.dimXgrid)] for j in range(g.dimYgrid)]
    universe = [[ random.choice([0,0,0,1,1,1]) for i in range(g.dimXgrid)] for j in range(g.dimYgrid)]
    speed=0.18

    # OpenGL actions carried once per universe
    glutInit()
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

 s = fs.Synth(gain=1.8)
 s.start()   
 ins = "..\soundfonts"+ sounds
 soundfont = s.sfload(ins)
 s.program_select(0,soundfont,0,0)


 cellColor = g.PINK
 name = "Vocal melodies"
 posX = 0
 posY = 0

 fileName = './states/vocals/opening piano '
 fileName2 = './states/vocals/melodic chants '
 fileName3 = './states/vocals/jennie1 piano '
 fileName4 = './states/vocals/jennie2 piano '
 fileName5 = './states/vocals/lisa2 piano '
 fileName6 = './states/vocals/jisoo1 piano '
 fileName7 = './states/vocals/rose1 piano '
 fileName8 = './states/vocals/rose2 piano '
 fileName9 = './states/vocals/chorus1 piano '
 fileName10 = './states/vocals/chorus2 piano '
 fileName11 = './states/vocals/chorus3 piano '

 file = fileName
 file2 = fileName2
 file3 = fileName3
 file4 = fileName4
 file5 = fileName5
 file6 = fileName6
 file7 = fileName7
 file8 = fileName8
 file9 = fileName9
 file10 = fileName10
 file11 = fileName11

 opSpeed = [[8,4,2],[2,2,2]]  

 # BLACKPINK in ur area 
 barsChants = [[int(Note("Db", 5))],[int(Note("F", 5)),int(Note("C", 5)),int(Note("C", 5))],
 [int(Note("C", 5)),int(Note("C", 5)),int(Note("F", 5))],[int(Note("Ab", 5)),int(Note("F", 5))]]

 speedChants = [[2],[2,2,2],
 [1,1,14],[2,24]]

 speedChants2 = [[2],[2,2,2],
 [1,1,14],[2,12]]

 # Jennie
 bars1 = [[int(Note("Db", 5)),int(Note("Db", 5))],[int(Note("Db", 5)),int(Note("Db", 5)),int(Note("Db", 5))],
 [int(Note("Db", 5)),int(Note("Bb", 4)),int(Note("Bb", 4))],[int(Note("C", 5)),int(Note("C", 5)),int(Note("C", 5))],
 [int(Note("F", 5))]]   

 speed1 = [[2,1],[1,1,1],
 [2,2,2],[2,2,2],
 [6]]

 bars2 = [[int(Note("Db", 5)),int(Note("Db", 5)),int(Note("Db", 5))],[int(Note("Db", 5)),int(Note("Db", 5)),int(Note("Db", 5))],
 [int(Note("F", 5)),int(Note("Eb", 5)),int(Note("Eb", 5))],[int(Note("Eb", 5)),int(Note("Eb", 5)),int(Note("Db", 5))],
 [int(Note("Db", 5)),int(Note("Eb", 5))],[int(Note("Db", 5)),int(Note("Db", 5)),int(Note("Db", 5))],[int(Note("F", 4))],
 [int(Note("C", 5)),int(Note("C", 5)),int(Note("C", 5))],[int(Note("C", 5))]]

 speed2 = [[1,1,1],[1,1,1],
 [2,2,2],[2,2,2],
 [1,5],[1,1,2],[8],
 [2,2,2],[6]]

 # Lisa 
 bars3 = [[int(Note("Db", 5)),int(Note("Db", 5)),int(Note("Db", 5))],[int(Note("Db", 5)),int(Note("Db", 5)),int(Note("Db", 5))],
 [int(Note("F", 5))],[int(Note("F", 5)),int(Note("Eb", 5)),int(Note("Eb", 5))],[int(Note("Eb", 5)),int(Note("Eb", 5)),int(Note("Db", 5))],
 [int(Note("Db", 5)),int(Note("Eb", 5))],[int(Note("Db", 5)),int(Note("Db", 5)),int(Note("Db", 5))],[int(Note("F", 4))],
 [int(Note("C", 5)),int(Note("C", 5))],[int(Note("F", 5)),int(Note("Bb", 4))]]

 speed3 = [[1,1,1],[1,1,1],
 [1],[1,2,2],[2,2,2],
 [1,5],[1,1,2],[8],
 [2,2],[2,6]]

 # Jisoo
 bars4 = [[int(Note("F", 5)),int(Note("F", 5)),int(Note("F", 5))],[int(Note("F", 5)),int(Note("F", 5)),int(Note("F", 5))],
 [int(Note("F", 5)),int(Note("F", 5))],[int(Note("F", 5)),int(Note("F", 5)),int(Note("F", 5))],
 [int(Note("Ab", 5)),int(Note("F", 5)),int(Note("F", 5))]]

 speed4 = [[1,1,1],[1,1,1],
 [1,1],[1,1,2],
 [4,2,6]]

 # Rosé
 bars5 = [[int(Note("F", 5)),int(Note("F", 5)),int(Note("F", 5))],[int(Note("F", 5)),int(Note("F", 5)),int(Note("F", 5))],
 [int(Note("F", 5)),int(Note("F", 5)),int(Note("F", 5))],
 [int(Note("Ab", 5)),int(Note("Bb", 5)),int(Note("F", 5))]]

 speed5 = [[1,1,1],[1,2,2],
 [1,1,2],
 [4,2,6]]

 bars6 = [[int(Note("F", 5)),int(Note("F", 5)),int(Note("F", 5))],[int(Note("F", 5)),int(Note("F", 5)),int(Note("F", 5))],
 [int(Note("F", 5)),int(Note("F", 5)),int(Note("F", 5))],[int(Note("F", 5)),int(Note("F", 5)),int(Note("F", 5))],
 [int(Note("Eb", 5)),int(Note("Db", 5)),int(Note("Bb", 4))]]

 speed6 = [[1,1,1],[1,1,1],
 [1,1,1],[1,2,2],
 [2,2,2]]

 # Chorus vocal lines
 bars7 = [[int(Note("Bb", 4)),int(Note("Bb", 4)),int(Note("Bb", 4))],[int(Note("Bb", 4)),int(Note("Bb", 4)),int(Note("Bb", 4))],
 [int(Note("Bb", 4))],[int(Note("Db", 5)),int(Note("F", 5)),int(Note("C", 5))]]

 speed7 = [[2,2,2],[2,2,2],
 [2],[2,2,6]]

 # Whip it,Whip it, Whip it version 1
 bars8 = [[int(Note("F", 5)),int(Note("F", 5))],[int(Note("Eb", 5))],[int(Note("Eb", 5)),int(Note("Eb", 5)),int(Note("Eb", 5))],
 [int(Note("F", 5)),int(Note("F", 5))],[int(Note("F", 5)),int(Note("F", 5))],
 [int(Note("Eb", 5))],[int(Note("Eb", 5)),int(Note("Eb", 5)),int(Note("Eb", 5))],
 [int(Note("F", 5)),int(Note("F", 5))],[int(Note("Bb", 4)),int(Note("Bb", 4)),int(Note("Bb", 4))],
 [int(Note("Bb", 4)),int(Note("Bb", 4)),int(Note("Bb", 4))],[int(Note("Db", 5)),int(Note("F", 5)),int(Note("C", 5))]]

 speed8 = [[1,1],[1],[1,1,1],
 [1,5],[1,1],
 [1],[1,1,1],
 [1,3],[2,2,2],
 [2,2,2],[2,2,6]]

 # Whip it, Whip it, Whip it version 2
 bars9 = [[int(Note("F", 5)),int(Note("F", 5))],[int(Note("Eb", 5))],[int(Note("Eb", 5)),int(Note("Eb", 5)),int(Note("Eb", 5))],
 [int(Note("F", 5)),int(Note("F", 5))],[int(Note("F", 5)),int(Note("F", 5))],
 [int(Note("Eb", 5))],[int(Note("Eb", 5)),int(Note("Eb", 5)),int(Note("Eb", 5))],
 [int(Note("F", 5)),int(Note("F", 5)),int(Note("F", 5))],[int(Note("Gb", 5))],
 [int(Note("F", 5)),int(Note("Eb", 5)),int(Note("Db", 5))],[int(Note("C", 5)),int(Note("Bb", 4))]]

 speed9 = [[1,1],[1],[1,1,1],
 [1,5],[1,1],
 [1],[1,1,1],
 [1,5,2],[2],
 [2,2,2],[2,4]]
 #####################################################################################


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


 # vocals sleeping during strings opening
 file = fileName + str(0) + '.txt'
 universe = nm.loadtxt(file, dtype=int)

 for x in range(len(opSpeed)):
      for y in range(len(opSpeed[x])):
       #glutSetWindow(glutGetWindow())                     
       glClear(GL_COLOR_BUFFER_BIT)
       g.drawLivings(cellColor,universe)

       universe = a.nextState(universe)

       time.sleep(opSpeed[x][y]*0.063)
       time.sleep((opSpeed[x][y]/2)*0.063)

 # Looping through Blackpink in ur area x2
 for x in range(len(speedChants)):
    file2 = fileName2 + str(x) + '.txt'
    universe = nm.loadtxt(file2, dtype=int)

    for y in range(len(speedChants[x])):
       #glutSetWindow(glutGetWindow())                     
       glClear(GL_COLOR_BUFFER_BIT)
       g.drawLivings(cellColor,universe)

       universe = a.nextState(universe)
            
       s.noteon(0,barsChants[x][y],80)

       time.sleep(speedChants[x][y]*n)

       s.noteoff(0,barsChants[x][y])

       time.sleep((speedChants[x][y]/2)*n)

 for x in range(len(speedChants2)):
    file2 = fileName2 + str(x) + '.txt'
    universe = nm.loadtxt(file2, dtype=int)

    for y in range(len(speedChants2[x])):
       #glutSetWindow(glutGetWindow())                     
       glClear(GL_COLOR_BUFFER_BIT)
       g.drawLivings(cellColor,universe)

       universe = a.nextState(universe)
            
       s.noteon(0,barsChants[x][y],80)

       time.sleep(speedChants2[x][y]*n)

       s.noteoff(0,barsChants[x][y])

       time.sleep((speedChants2[x][y]/2)*n)

 # Jennie first verse
 for z in range(2):
    for x in range(len(bars1)):
       file3 = fileName3 + str(x) + '.txt'
       universe = nm.loadtxt(file3, dtype=int)

       for y in range(len(bars1[x])):
          #glutSetWindow(glutGetWindow())                     
          glClear(GL_COLOR_BUFFER_BIT)
          g.drawLivings(cellColor,universe)

          s.noteon(0,bars1[x][y],80)
          time.sleep(speed1[x][y]*n)

          s.noteoff(0,bars1[x][y])            
          time.sleep((speed1[x][y]/2)*n)

 for x in range(len(bars2)):
    file4 = fileName4 + str(x) + '.txt'
    universe = nm.loadtxt(file4, dtype=int)

    for y in range(len(bars2[x])):
       #glutSetWindow(glutGetWindow())                     
       glClear(GL_COLOR_BUFFER_BIT)
       g.drawLivings(cellColor,universe)

       s.noteon(0,bars2[x][y],80)
       time.sleep(speed2[x][y]*n)

       s.noteoff(0,bars2[x][y])            
       time.sleep((speed2[x][y]/2)*n)


 # Lisa first verse
 for z in range(2):
    for x in range(len(bars1)):
       file3 = fileName3 + str(x) + '.txt'
       universe = nm.loadtxt(file3, dtype=int)

       for y in range(len(bars1[x])):
          #glutSetWindow(glutGetWindow())                     
          glClear(GL_COLOR_BUFFER_BIT)
          g.drawLivings(cellColor,universe)

          s.noteon(0,bars1[x][y],80)
          time.sleep(speed1[x][y]*n)

          s.noteoff(0,bars1[x][y])            
          time.sleep((speed1[x][y]/2)*n)

 for x in range(len(bars3)):
    file5 = fileName5 + str(x) + '.txt'
    universe = nm.loadtxt(file5, dtype=int)

    for y in range(len(bars3[x])):
       #glutSetWindow(glutGetWindow())                     
       glClear(GL_COLOR_BUFFER_BIT)
       g.drawLivings(cellColor,universe)

       s.noteon(0,bars3[x][y],80)
       time.sleep(speed3[x][y]*n)

       s.noteoff(0,bars3[x][y])            
       time.sleep((speed3[x][y]/2)*n)


 # Jisoo first verse
 for o in range(2):
      for x in range(len(bars4)):
         file6 = fileName6 + str(x) + '.txt'
         universe = nm.loadtxt(file6, dtype=int)

         for y in range(len(bars4[x])):
            #glutSetWindow(glutGetWindow())                     
            glClear(GL_COLOR_BUFFER_BIT)
            g.drawLivings(cellColor,universe)

            s.noteon(0,bars4[x][y],80)
            time.sleep(speed4[x][y]*n)

            s.noteoff(0,bars4[x][y])            
            time.sleep((speed4[x][y]/2)*n)

 # Rose first verse
 for x in range(len(bars5)):
    file7 = fileName7 + str(x) + '.txt'
    universe = nm.loadtxt(file7, dtype=int)

    for y in range(len(bars5[x])):
       #glutSetWindow(glutGetWindow())                     
       glClear(GL_COLOR_BUFFER_BIT)
       g.drawLivings(cellColor,universe)

       s.noteon(0,bars5[x][y],80)
       time.sleep(speed5[x][y]*n)

       s.noteoff(0,bars5[x][y])            
       time.sleep((speed5[x][y]/2)*n)

 for x in range(len(bars6)):
    file8 = fileName8 + str(x) + '.txt'
    universe = nm.loadtxt(file8, dtype=int)

    for y in range(len(bars6[x])):
       #glutSetWindow(glutGetWindow())                     
       glClear(GL_COLOR_BUFFER_BIT)
       g.drawLivings(cellColor,universe)

       s.noteon(0,bars6[x][y],80)
       time.sleep(speed6[x][y]*n)

       s.noteoff(0,bars6[x][y])            
       time.sleep((speed6[x][y]/2)*n)


 # Chorus melodies x2
 for z in range(2):
    for x in range(len(bars7)):
       file9 = fileName9 + str(x) + '.txt'
       universe = nm.loadtxt(file9, dtype=int)

       for y in range(len(bars7[x])):
          #glutSetWindow(glutGetWindow())                     
          glClear(GL_COLOR_BUFFER_BIT)
          g.drawLivings(cellColor,universe)

          s.noteon(0,bars7[x][y],80)
          time.sleep(speed7[x][y]*n)

          s.noteoff(0,bars7[x][y])            
          time.sleep((speed7[x][y]/2)*n)

 # Whip it, Whip it, Whip it x2
 time.sleep(speed8[0][0]*n)
 time.sleep((speed8[0][0]/2)*n)
 time.sleep(speed8[0][0]*n)
 time.sleep((speed8[0][0]/2)*n)

 for x in range(len(bars8)):
    file10 = fileName10 + str(x) + '.txt'
    universe = nm.loadtxt(file10, dtype=int)

    for y in range(len(bars8[x])):
       #glutSetWindow(glutGetWindow())                     
       glClear(GL_COLOR_BUFFER_BIT)
       g.drawLivings(cellColor,universe)

       s.noteon(0,bars8[x][y],80)
       time.sleep(speed8[x][y]*n)

       s.noteoff(0,bars8[x][y])            
       time.sleep((speed8[x][y]/2)*n)

 # Chorus melodies x2
 for z in range(2):
    for x in range(len(bars7)):
       file9 = fileName9 + str(x) + '.txt'
       universe = nm.loadtxt(file9, dtype=int)

       for y in range(len(bars7[x])):
          #glutSetWindow(glutGetWindow())                     
          glClear(GL_COLOR_BUFFER_BIT)
          g.drawLivings(cellColor,universe)

          s.noteon(0,bars7[x][y],80)
          time.sleep(speed7[x][y]*n)

          s.noteoff(0,bars7[x][y])            
          time.sleep((speed7[x][y]/2)*n)

 # Whip it, Whip it, Whip it version2 x2
 time.sleep(speed9[0][0]*n)
 time.sleep((speed9[0][0]/2)*n)
 time.sleep(speed9[0][0]*n)
 time.sleep((speed9[0][0]/2)*n)

 for x in range(len(bars9)):
    file11 = fileName11 + str(x) + '.txt'
    universe = nm.loadtxt(file11, dtype=int)

    for y in range(len(bars9[x])):
       #glutSetWindow(glutGetWindow())                     
       glClear(GL_COLOR_BUFFER_BIT)
       g.drawLivings(cellColor,universe)

       s.noteon(0,bars9[x][y],80)
       time.sleep(speed9[x][y]*n)

       s.noteoff(0,bars9[x][y])            
       time.sleep((speed9[x][y]/2)*n)

 #glutSetWindow(glutGetWindow())                     
 glClear(GL_COLOR_BUFFER_BIT)
 g.drawDead()

 time.sleep(speed8[0][0]*n)
 time.sleep((speed8[0][0]/2)*n)
 time.sleep(speed8[0][0]*n)
 time.sleep((speed8[0][0]/2)*n)

 s.delete()
