import time
import fluidsynth as fs
from mingus.containers import Note
import  pygame 
from pygame import mixer

n = 0.09

sounds = "\yamahap45.sf2"
sounds3 = "\drums"
sounds4 = "\R-violin.sf2"
sounds5 = "\TEK bass.sf2"                     
sounds6 = "\pizzicato2.sf2"                   # 45

def piano():
    s = fs.Synth(gain=1.8)
    s.start()
    
    ins = "..\soundfonts"+ sounds
    soundfont = s.sfload(ins)
    s.program_select(0,soundfont,0,0)

    # Initial Sostenuto + opening strings
    opening = [[int(Note("F", 5)),int(Note("Bb", 5)),int(Note("Bb", 5))],[int(Note("F", 6)),int(Note("F", 6)),int(Note("Eb", 6))],
    [int(Note("Db", 6)),int(Note("Db", 6)),int(Note("C", 6))],[int(Note("Bb", 5)),int(Note("A", 5))]]

    opSpeed = [[8,4,2],[2,2,2],[2,2,2],[2,2]]

    # BLACKPINK in ur area 
    barsChants = [[int(Note("Db", 5))],[int(Note("F", 5)),int(Note("C", 5)),int(Note("C", 5))],
    [int(Note("C", 5)),int(Note("C", 5)),int(Note("F", 5))],[int(Note("Ab", 5))],[int(Note("F", 5))]]

    speedChants = [[2],[2,2,2],
    [1,1,14],[2],[12]]

    # Jennie
    bars1 = [[int(Note("Db", 5)),int(Note("Db", 5)),int(Note("Db", 5)),int(Note("Db", 5)),int(Note("Db", 5))],
    [int(Note("Db", 5)),int(Note("Bb", 4)),int(Note("Bb", 4))],[int(Note("C", 5)),int(Note("C", 5)),int(Note("C", 5))],
    [int(Note("F", 5))]]   

    speed1 = [[2,1,1,1,1],
    [2,2,2],[2,2,2],
    [6]]

    bars2 = [[int(Note("Db", 5)),int(Note("Db", 5)),int(Note("Db", 5)),int(Note("Db", 5)),int(Note("Db", 5)),int(Note("Db", 5))],
    [int(Note("F", 5)),int(Note("Eb", 5)),int(Note("Eb", 5))],[int(Note("Eb", 5)),int(Note("Eb", 5)),int(Note("Db", 5))],
    [int(Note("Db", 5)),int(Note("Eb", 5))],[int(Note("Db", 5)),int(Note("Db", 5)),int(Note("Db", 5)),int(Note("F", 4))],
    [int(Note("C", 5)),int(Note("C", 5)),int(Note("C", 5)),int(Note("C", 5))]]

    speed2 = [[1,1,1,1,1,1],
    [2,2,2],[2,2,2],
    [1,5],[1,1,2,8],
    [2,2,2,6]]

    # Lisa 
    bars3 = [[int(Note("Db", 5)),int(Note("Db", 5)),int(Note("Db", 5)),int(Note("Db", 5)),int(Note("Db", 5)),int(Note("Db", 5))],
    [int(Note("F", 5)),int(Note("F", 5)),int(Note("Eb", 5)),int(Note("Eb", 5))],[int(Note("Eb", 5)),int(Note("Eb", 5)),int(Note("Db", 5))],
    [int(Note("Db", 5)),int(Note("Eb", 5))],[int(Note("Db", 5)),int(Note("Db", 5)),int(Note("Db", 5)),int(Note("F", 4))],
    [int(Note("C", 5)),int(Note("C", 5)),int(Note("F", 5)),int(Note("Bb", 4))]]

    speed3 = [[1,1,1,1,1,1],
    [1,1,2,2],[2,2,2],
    [1,5],[1,1,2,8],
    [2,2,2,6]]
  #######################################################################

    # 0:00
    for x in range(len(opening)):
        for y in range(len(opening[x])):

            time.sleep(opSpeed[x][y]*n)
            time.sleep((opSpeed[x][y]/2)*n)

    # BLACKPINK in ur area x2
    for a in range(2):
        for b in range(len(barsChants)):
            for c in range(len(barsChants[b])):

                s.noteon(0,barsChants[b][c],80)
                time.sleep(speedChants[b][c]*n)

                s.noteoff(0,barsChants[b][c])            
                time.sleep((speedChants[b][c]/2)*n)            

    # Jennie first verse
    for d in range(2):
        for e in range(len(bars1)):
            for f in range(len(bars1[e])):

                s.noteon(0,bars1[e][f],80)
                time.sleep(speed1[e][f]*n)

                s.noteoff(0,bars1[e][f])            
                time.sleep((speed1[e][f]/2)*n)

    for g in range(len(bars2)):
        for h in range(len(bars2[g])):
            s.noteon(0,bars2[g][h],80)
            time.sleep(speed2[g][h]*n)

            s.noteoff(0,bars2[g][h])            
            time.sleep((speed2[g][h]/2)*n)

    # Lisa first verse
    for i in range(2):
        for j in range(len(bars1)):
            for k in range(len(bars1[j])):

                s.noteon(0,bars1[j][k],80)
                time.sleep(speed1[j][k]*n)

                s.noteoff(0,bars1[j][k])            
                time.sleep((speed1[j][k]/2)*n)

    for l in range(len(bars3)):
        for m in range(len(bars3[l])):
            s.noteon(0,bars3[l][m],80)
            time.sleep(speed3[l][m]*n)

            s.noteoff(0,bars3[l][m])            
            time.sleep((speed3[l][m]/2)*n)

    s.delete()
    pianoPizzicatos()

def pianoPizzicatos():
    s = fs.Synth(gain=1.8)
    s.start()
    
    ins = "..\soundfonts"+ sounds
    soundfont = s.sfload(ins)
    s.program_select(0,soundfont,0,0)

    # Jisoo
    bars1 = [[int(Note("F", 5)),int(Note("F", 5)),int(Note("F", 5)),int(Note("F", 5)),int(Note("F", 5)),int(Note("F", 5))],
    [int(Note("F", 5)),int(Note("F", 5)),int(Note("F", 5)),int(Note("F", 5)),int(Note("F", 5))],
    [int(Note("Ab", 5)),int(Note("F", 5)),int(Note("F", 5))]]

    speed1 = [[1,1,1,1,1,1],
    [1,1,1,1,2],
    [4,2,6]]

    # Rosé
    bars2 = [[int(Note("F", 5)),int(Note("F", 5)),int(Note("F", 5)),int(Note("F", 5)),int(Note("F", 5))],
    [int(Note("F", 5)),int(Note("F", 5)),int(Note("F", 5)),int(Note("F", 5))],
    [int(Note("Ab", 5)),int(Note("Bb", 5)),int(Note("F", 5))]]

    speed2 = [[1,1,1,1,2],
    [2,1,1,2],
    [4,2,6]]

    bars3 = [[int(Note("F", 5)),int(Note("F", 5)),int(Note("F", 5)),int(Note("F", 5)),int(Note("F", 5)),int(Note("F", 5))],
    [int(Note("F", 5)),int(Note("F", 5)),int(Note("F", 5)),int(Note("F", 5)),int(Note("F", 5))],
    [int(Note("F", 5)),int(Note("Eb", 5)),int(Note("Db", 5))],[int(Note("Bb", 4))]]

    speed3 = [[1,1,1,1,1,1],
    [1,1,1,1,2],
    [2,2,2],[2]]
  #######################################################################

    # Jisoo first verse
    for o in range(2):
        for p in range(len(bars1)):
            for q in range(len(bars1[p])):
                s.noteon(0,bars1[p][q],80)
                time.sleep(speed1[p][q]*n)

                s.noteoff(0,bars1[p][q])            
                time.sleep((speed1[p][q]/2)*n)

    # Rosé first verse
    for r in range(len(bars2)):
        for t in range(len(bars2[r])):
            s.noteon(0,bars2[r][t],80)
            time.sleep(speed2[r][t]*n)

            s.noteoff(0,bars2[r][t])            
            time.sleep((speed2[r][t]/2)*n)

    for u in range(len(bars3)):
        for v in range(len(bars3[u])):
            s.noteon(0,bars3[u][v],80)
            time.sleep(speed3[u][v]*n)

            s.noteoff(0,bars3[u][v])            
            time.sleep((speed3[u][v]/2)*n)

    s.delete()
    pianoChorus()

def pianoChorus():
    s = fs.Synth(gain=1.8)
    s.start()
    
    ins = "..\soundfonts"+ sounds
    soundfont = s.sfload(ins)
    s.program_select(0,soundfont,0,0)

    # Chorus vocal lines
    bars1 = [[int(Note("Bb", 4)),int(Note("Bb", 4))],[int(Note("Bb", 4)),int(Note("Bb", 4)),int(Note("Bb", 4))],
    [int(Note("Bb", 4)),int(Note("Bb", 4)),int(Note("Db", 5))],[int(Note("F", 5)),int(Note("C", 5))]]

    speed1 = [[2,2],[2,2,2],
    [2,2,2],[2,6]]

    # Whip it,Whip it, Whip it version 1
    bars2 = [[int(Note("F", 5)),int(Note("F", 5)),int(Note("Eb", 5)),int(Note("Eb", 5)),int(Note("Eb", 5)),int(Note("Eb", 5))],
    [int(Note("F", 5)),int(Note("F", 5))],
    [int(Note("F", 5)),int(Note("F", 5)),int(Note("Eb", 5)),int(Note("Eb", 5)),int(Note("Eb", 5)),int(Note("Eb", 5))],
    [int(Note("F", 5)),int(Note("F", 5)),int(Note("Bb", 4)),int(Note("Bb", 4)),int(Note("Bb", 4))],
    [int(Note("Bb", 4)),int(Note("Bb", 4)),int(Note("Bb", 4))],[int(Note("Db", 5)),int(Note("F", 5)),int(Note("C", 5))]]

    speed2 = [[1,1,1,1,1,1],
    [1,5],
    [1,1,1,1,1,1],
    [1,3,2,2,2],
    [2,2,2],[2,2,6]]

    # Whip it, Whip it, Whip it version 2
    bars3 = [[int(Note("F", 5)),int(Note("F", 5)),int(Note("Eb", 5)),int(Note("Eb", 5)),int(Note("Eb", 5)),int(Note("Eb", 5))],
    [int(Note("F", 5)),int(Note("F", 5))],
    [int(Note("F", 5)),int(Note("F", 5)),int(Note("Eb", 5)),int(Note("Eb", 5)),int(Note("Eb", 5)),int(Note("Eb", 5))],
    [int(Note("F", 5)),int(Note("F", 5)),int(Note("F", 5)),int(Note("Gb", 5))],
    [int(Note("F", 5)),int(Note("Eb", 5)),int(Note("Db", 5)),int(Note("C", 5)),int(Note("Bb", 4))]]

    speed3 = [[1,1,1,1,1,1],
    [1,5],
    [1,1,1,1,1,1],
    [1,5,2,2,2],
    [2,2,2,2,4]]

   #######################################################################

   # vocal melodies x2
    for a in range(2):
        for b in range(len(bars1)):
            for c in range(len(bars1[b])):
                s.noteon(0,bars1[b][c],80)
                time.sleep(speed1[b][c]*n)

                s.noteoff(0,bars1[b][c])            
                time.sleep((speed1[b][c]/2)*n)

    # Whip it, Whip it, Whip it x2
    time.sleep(speed1[0][0]*n)
    time.sleep((speed1[0][0]/2)*n)
    time.sleep(speed1[0][0]*n)
    time.sleep((speed1[0][0]/2)*n)

    for d in range(len(bars2)):
        for e in range(len(bars2[d])):
            s.noteon(0,bars2[d][e],80)
            time.sleep(speed2[d][e]*n)

            s.noteoff(0,bars2[d][e])            
            time.sleep((speed2[d][e]/2)*n)            

    # vocal melodies x2
    for f in range(2):
        for g in range(len(bars1)):
            for h in range(len(bars1[g])):
                s.noteon(0,bars1[g][h],80)
                time.sleep(speed1[g][h]*n)

                s.noteoff(0,bars1[g][h])            
                time.sleep((speed1[g][h]/2)*n)

    # Whip it, Whip it, Whip it x2 & chorus termination
    time.sleep(speed1[0][0]*n)
    time.sleep((speed1[0][0]/2)*n)
    time.sleep(speed1[0][0]*n)
    time.sleep((speed1[0][0]/2)*n)

    for i in range(len(bars3)):
        for j in range(len(bars3[i])):
            s.noteon(0,bars3[i][j],80)
            time.sleep(speed3[i][j]*n)

            s.noteoff(0,bars3[i][j])            
            time.sleep((speed3[i][j]/2)*n)

    time.sleep(speed1[0][0]*n)
    time.sleep((speed1[0][0]/2)*n)
    time.sleep(speed1[0][0]*n)
    time.sleep((speed1[0][0]/2)*n)

    s.delete()
 
def violin():
    s = fs.Synth(gain=0.1)
    s.start()
    
    ins = "..\soundfonts"+ sounds4
    soundfont = s.sfload(ins)
    s.program_select(0,soundfont,0,0)

    # Initial Sostenuto + opening strings
    opening = [[int(Note("F", 5)),int(Note("Bb", 5)),int(Note("Bb", 5))],[int(Note("F", 6)),int(Note("F", 6)),int(Note("Eb", 6))]]

    opSpeed = [[8,4,2],[2,2,2]]

    # Leitmotiv: "La Campanella"
    bars = [[int(Note("Db", 6)),int(Note("Db", 6)),int(Note("C", 6))],[int(Note("Bb", 5)),int(Note("A", 5)),int(Note("Bb", 5))],
    [int(Note("C", 6)),int(Note("F", 5)),int(Note("F", 5))],[int(Note("Gb", 5)),int(Note("F", 5)),int(Note("Eb", 5))]]

    speed = [[2,2,2],[2,2,2],[2,2,2],[2,2,2]]
  #######################################################################

    # 0:00
    for x in range(len(opening)):
        for y in range(len(opening[x])):

            s.noteon(0,opening[x][y],80)

            time.sleep(opSpeed[x][y]*n)

            s.noteoff(0,opening[x][y])

            time.sleep((opSpeed[x][y]/2)*n)

    # Obstinato x12
    for a in range(12):
        for b in range(len(bars)):
            for c in range(len(bars[b])):

                s.noteon(0,bars[b][c],80)

                time.sleep(speed[b][c]*n)

                s.noteoff(0,bars[b][c])

                time.sleep((speed[b][c]/2)*n)

    s.delete()

    violinPizzicatos()

def violinPizzicatos():

    s = fs.Synth(gain=0.3)
    s.start()
    
    ins = "..\soundfonts"+ sounds6         
    soundfont = s.sfload(ins)
    s.program_select(0,soundfont,0,45)

    # Paganini's Pizzicatos
    bars1 = [[int(Note("Bb", 4)),int(Note("Bb", 4)),int(Note("Db", 5))],[int(Note("F", 5)),int(Note("Db", 5)),int(Note("Bb", 4))]]
    
    bars2 = [[int(Note("A", 4)),int(Note("Ab", 4)),int(Note("C", 5))],[int(Note("F", 5)),int(Note("C", 5)),int(Note("Ab", 4))]]

    speed = [[2,2,2],[2,2,2]]
  #######################################################################

    # Pizzicatos x3
    for d in range(3):
        for e in range(len(bars1)):
            for f in range(len(bars1[e])):

                s.noteon(0,bars1[e][f],80)

                time.sleep(speed[e][f]*n)

                s.noteoff(0,bars1[e][f])

                time.sleep((speed[e][f]/2)*n)

        for o in range(len(bars2)):
            for p in range(len(bars2[o])):

                s.noteon(0,bars2[o][p],80)

                time.sleep(speed[o][p]*n)

                s.noteoff(0,bars2[o][p])

                time.sleep((speed[o][p]/2)*n)

    # Pizzicatos first-bar
    for q in range(len(bars1)):
        for r in range(len(bars1[q])):

            s.noteon(0,bars1[q][r],80)

            time.sleep(speed[q][r]*n)

            s.noteoff(0,bars1[q][r])

            time.sleep((speed[q][r]/2)*n)

    s.delete()

    violinChorus()

def violinChorus():
    s = fs.Synth(gain=0.1)
    s.start()
    
    ins = "..\soundfonts"+ sounds4
    soundfont = s.sfload(ins)
    s.program_select(0,soundfont,0,0)

    # Opening Strings without sostenuto
    openingChorus = [[int(Note("Bb", 5)),int(Note("Bb", 5))],[int(Note("F", 6)),int(Note("F", 6)),int(Note("Eb", 6))]]

    opChorusSpeed = [[4,2],[2,2,2]]

    # Leitmotiv: "La Campanella"
    bars = [[int(Note("Db", 6)),int(Note("Db", 6)),int(Note("C", 6))],[int(Note("Bb", 5)),int(Note("A", 5)),int(Note("Bb", 5))],
    [int(Note("C", 6)),int(Note("F", 5)),int(Note("F", 5))],[int(Note("Gb", 5)),int(Note("F", 5)),int(Note("Eb", 5))]]

    speed = [[2,2,2],[2,2,2],[2,2,2],[2,2,2]]

    #  Termination: i-V-i (V in second inversion)
    outro = [[int(Note("F", 5)),int(Note("Bb", 5)),int(Note("Db", 6)),int(Note("F", 6))],
    [int(Note("F", 5)),int(Note("A", 5)),int(Note("C", 6)),int(Note("F", 6))],               
    [int(Note("Bb", 4)),int(Note("Db", 5)),int(Note("F", 5))]]

    ouSpeed =  [[3,1,1,1],[3,1,1,1],[8,8,8]]
  #######################################################################

    # Chorus entrance
    for g in range(len(openingChorus)):
        for h in range(len(openingChorus[g])):

            s.noteon(0,openingChorus[g][h],80)

            time.sleep(opChorusSpeed[g][h]*n)

            s.noteoff(0,openingChorus[g][h])

            time.sleep((opChorusSpeed[g][h]/2)*n)            

    # Leitmotiv x7
    for i in range(7):
        for j in range(len(bars)):
            for k in range(len(bars[j])):

                s.noteon(0,bars[j][k],80)

                time.sleep(speed[j][k]*n)

                s.noteoff(0,bars[j][k])

                time.sleep((speed[j][k]/2)*n)

    # Chorus Outro featuring i-V-i 
    for l in range(len(outro)-1):
        for m in range(len(outro[l])):

            s.noteon(0,outro[l][m],80)

            time.sleep(ouSpeed[l][m]*n)

            s.noteoff(0,outro[l][m])

            time.sleep((ouSpeed[l][m]/2)*n)

    s.noteon(0,outro[2][0],80)
    s.noteon(0,outro[2][1],80)
    s.noteon(0,outro[2][2],80)

    time.sleep(ouSpeed[2][0]*n)

    s.noteoff(0,outro[2][0])
    s.noteoff(0,outro[2][1])
    s.noteoff(0,outro[2][2])

    time.sleep((ouSpeed[2][0]/2)*n)

    s.delete()

def drums():
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

    # Initial Sostenuto + opening strings
    opening = [[int(Note("F", 5)),int(Note("Bb", 5)),int(Note("Bb", 5))],[int(Note("F", 6)),int(Note("F", 6)),int(Note("Eb", 6))]]
    opSpeed = [[8,4,2],[2,2,2]]

    # Standard rhytmic pattern 
    pattern = [[bassDrum,hihat,hihat,snareDrum,hihat,hihat,hihat,hihat,bassDrum,bassDrum,snareDrum,hihat,bassDrum,hihat,hihat],
    [bassDrum,hihat,hihat,snareDrum,hihat,hihat,hihat,bassDrum,hihat,bassDrum,snareDrum,hihat,snareDrum]]

    # TUM rhytmic pattern
    patternTum =[[bassDrum,hihat,hihat,snareDrum,hihat,hihat,hihat,hihat,bassDrum,bassDrum,snareDrum,hihat,bassDrum,hihat,hihat],
    [bassDrum,hihat,hihat,finalDrum,hihat,hihat,hihat,bassDrum,hihat,bassDrum,snareDrum,hihat,snareDrum]]

    speed = [[3,3,3,3,3,1,1,4,3,3,3,3,1,1,1],
    [3,3,3,3,3,3,3,1,2,3,3,3,3]]
  #######################################################################

    #0:00
    for x in range(len(opening)):
        for y in range(len(opening[x])):

            time.sleep(opSpeed[x][y]*n)
            time.sleep((opSpeed[x][y]/2)*n)

    # Standard pattern x3
    for a in range(3):
        for b in range(len(pattern)):
            for c in range (len(pattern[b])):

                pattern[b][c].play()
                time.sleep(speed[b][c]*n)

    # TUM pattern 
    for d in range(len(patternTum)):
        for e in range(len(patternTum[d])):

            patternTum[d][e].play()
            time.sleep(speed[d][e]*n)

    # Standard x1 + TUM x1 (changing sections)
    for f in range(len(pattern)):
        for g in range (len(pattern[f])):

            pattern[f][g].play()
            time.sleep(speed[f][g]*n)
               
    for h in range(len(patternTum)):
        for i in range(len(patternTum[h])):

            patternTum[h][i].play()
            time.sleep(speed[h][i]*n)
    
    drumsPizzicatos()
    
def drumsPizzicatos():
    pygame.init()
    
    ins = "..\soundfonts"+ sounds3
    snareDrum = mixer.Sound(ins+"\SnareDrum.WAV")
    snareDrum.set_volume(0.5)
    hihat = mixer.Sound(ins+"\Hihat.WAV")
    hihat.set_volume(0.5)

    # Standard pattern during pizzicatos (bassDrum OUT/ hihat IN)
    pattern = [[hihat,hihat,hihat,snareDrum,hihat,hihat,hihat,hihat,hihat,snareDrum,hihat,hihat,hihat,hihat],
    [hihat,hihat,hihat,snareDrum,hihat,hihat,hihat,hihat,hihat,hihat,snareDrum,hihat,snareDrum],
    [hihat,hihat,hihat,snareDrum,hihat,hihat,hihat,hihat,hihat,snareDrum,hihat,hihat,hihat,hihat],
    [hihat,hihat,hihat,snareDrum,hihat,hihat]]

    speed = [[3,3,3,3,3,2,4,3,3,3,3,1,1,1],
    [3,3,3,3,3,3,3,1,2,3,3,3,3],
    [3,3,3,3,3,2,4,3,3,3,3,1,1,1],
    [3,3,3,3,3,3]]
  #######################################################################
   
    # pizzicatos pattern x3.5
    for j in range(len(pattern)-1):
        for k in range(len(pattern[j])):

            pattern[j][k].play()
            time.sleep(speed[j][k]*n)

    # final pattern cut in half (changing sections)
    for l in range(len (speed[3])):
        time.sleep(speed[3][l]*n)

    drumsChorus()

def drumsChorus():

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

    # Opening Strings without sostenuto
    openingChorus = [[int(Note("Bb", 5)),int(Note("Bb", 5))],[int(Note("F", 6)),int(Note("F", 6)),int(Note("Eb", 6))]]

    opChorusSpeed = [[4,2],[2,2,2]]

    #  Termination: i-V-i (V in second inversion)        
    outro = [[int(Note("F", 5)),int(Note("Bb", 5)),int(Note("Db", 6)),int(Note("F", 6))],
    [int(Note("F", 5)),int(Note("A", 5)),int(Note("C", 6)),int(Note("F", 6))],               
    [int(Note("Bb", 4)),int(Note("Db", 5)),int(Note("F", 5))]]

    ouSpeed =  [[3,1,1,1],[3,1,1,1],[8,8,8]]

    # Standard Chorus rhytmic pattern
    pattern = [[bassDrum,hihat,hihat,snareDrum,hihat,hihat,bassDrum,bassDrum,finalDrum,hihat,bassDrum,hihat,hihat],
    [bassDrum,hihat,hihat,snareDrum,hihat,bassDrum,hihat,bassDrum,finalDrum,hihat,snareDrum],
    [bassDrum,hihat,hihat,snareDrum,hihat,hihat,hihat,hihat,bassDrum,bassDrum,snareDrum,hihat,bassDrum,hihat],
    [bassDrum,hihat,hihat,snareDrum,hihat,hihat,hihat,bassDrum,hihat,bassDrum,snareDrum,hihat,snareDrum],
    [bassDrum,hihat,hihat,snareDrum,hihat,hihat,bassDrum,bassDrum,finalDrum,hihat,bassDrum,hihat,hihat],
    [bassDrum,hihat,hihat,snareDrum,hihat,hihat,bassDrum,hihat,bassDrum,finalDrum,hihat,snareDrum],
    [bassDrum,hihat,hihat,snareDrum,hihat,hihat,hihat,hihat,bassDrum,bassDrum,snareDrum,hihat,bassDrum,hihat,hihat]]

    speed = [[3,3,3,3,3,6,3,3,3,3,1,1,1],
    [3,3,3,6,6,1,2,3,3,3,3],
    [3,3,3,3,3,1,1,4,3,3,3,3,2,1],
    [3,3,3,3,3,3,3,1,2,3,3,3,3],
    [3,3,3,3,3,6,3,3,3,3,1,1,1],
    [3,3,3,3,3,6,1,2,3,3,3,3],
    [3,3,3,3,3,1,1,4,3,3,3,3,1,1,1]]
  #######################################################################

    # Chorus entrance
    for r in range(len(openingChorus)):
        for t in range(len(openingChorus[r])):

            time.sleep(opChorusSpeed[r][r]*n)

            time.sleep((opChorusSpeed[r][t]/2)*n)  

    # chorus pattern
    for m in range(len(pattern)):
        for o in range(len(pattern[m])):

            pattern[m][o].play()
            time.sleep(speed[m][o]*n)

    # Chorus Outro featuring i-V-i 
    for p in range(len(outro)-1):
        for q in range(len(outro[p])):

            time.sleep(ouSpeed[p][q]*n)
            time.sleep((ouSpeed[p][q]/2)*n)

    time.sleep(ouSpeed[2][0]*n)

    # extra TUM for termination (back to verses)
    finalDrum.play()

    time.sleep(int(ouSpeed[2][0]/2)*n)

def bassFS ():
    s = fs.Synth(gain=0.8)
    s.start()
    
    ins = "..\soundfonts"+ sounds5
    soundfont = s.sfload(ins)
    s.program_select(0,soundfont,0,0)

    # Initial Sostenuto + opening strings
    opening = [[int(Note("F", 5)),int(Note("Bb", 5)),int(Note("Bb", 5))],[int(Note("F", 6)),int(Note("F", 6)),int(Note("Eb", 6))]]

    opSpeed = [[8,4,2],[2,2,2]]

    # Trap bass chords
    BbmChord = [int(Note("Bb", 2)),int(Note("Db", 3)),int(Note("F", 3))]
    FChord = [int(Note("F", 3)),int(Note("Ab", 3)),int(Note("C", 4))]

    bars = [BbmChord,[0,0,0],FChord,FChord,FChord,BbmChord,[0,0,0],FChord,FChord]

    speed = [6,6,2,8,2,6,6,2,10]
  #######################################################################

    # 0:00
    for x in range(len(opening)):
        for y in range(len(opening[x])):

            time.sleep(opSpeed[x][y]*n)
            time.sleep((opSpeed[x][y]/2)*n)

    # bass pattern x 6
    for a in range(6):
        for b in range(len(bars)):
            if(int(bars[b][0])>0):
             s.noteon(0,bars[b][0],80)
             s.noteon(0,bars[b][1],80)
             s.noteon(0,bars[b][2],80)

            time.sleep(speed[b]*n)

            if(int(bars[b][0])>0):
             s.noteoff(0,bars[b][0])
             s.noteoff(0,bars[b][1])
             s.noteoff(0,bars[b][2])

            time.sleep((speed[b]/2)*n) 

    s.delete()

    bassFSPizzicatos()

def bassFSPizzicatos():
    s = fs.Synth(gain=0.8)
    s.start()
    
    ins = "..\soundfonts"+ sounds5
    soundfont = s.sfload(ins)
    s.program_select(0,soundfont,0,0)

    # Violin pizzicatos bars
    bars1 = [[int(Note("Bb", 4)),int(Note("Bb", 4)),int(Note("Db", 5))],[int(Note("F", 5)),int(Note("Db", 5)),int(Note("Bb", 4))]]
    
    bars2 = [[int(Note("A", 4)),int(Note("Ab", 4)),int(Note("C", 5))],[int(Note("F", 5)),int(Note("C", 5)),int(Note("Ab", 4))]]

    speed = [[2,2,2],[2,2,2]]
  #######################################################################

    # bass go sleeping during pizzicatos section x3
    for c in range(3):
        for d in range(len(bars1)):
            for e in range(len(bars1[d])):

                time.sleep(speed[d][e]*n)

                time.sleep((speed[d][e]/2)*n)

        for f in range(len(bars2)):
            for g in range(len(bars2[f])):

                time.sleep(speed[f][g]*n)

                time.sleep((speed[f][g]/2)*n)

    # sleeping x1 (chaging sections)
    for q in range(len(bars1)):
        for r in range(len(bars1[q])):

            time.sleep(speed[q][r]*n)

            time.sleep((speed[q][r]/2)*n)

    s.delete()

    bassFSChorus()

def bassFSChorus():
    s = fs.Synth(gain=0.8)
    s.start()
    
    ins = "..\soundfonts"+ sounds5
    soundfont = s.sfload(ins)
    s.program_select(0,soundfont,0,0)

    # Opening Strings without sostenuto
    openingChorus = [[int(Note("Bb", 5)),int(Note("Bb", 5))],[int(Note("F", 6)),int(Note("F", 6)),int(Note("Eb", 6))]]

    opChorusSpeed = [[4,2],[2,2,2]]

    #  Termination: i-V-i (V in second inversion)
    outro = [[int(Note("F", 5)),int(Note("Bb", 5)),int(Note("Db", 6)),int(Note("F", 6))],
    [int(Note("F", 5)),int(Note("A", 5)),int(Note("C", 6)),int(Note("F", 6))],
    [int(Note("Bb", 4)),int(Note("Db", 5)),int(Note("F", 5))]]

    ouSpeed =  [[3,1,1,1],[3,1,1,1],[8,8,8]]

    # trap bass chords
    BbmChord = [int(Note("Bb", 2)),int(Note("Db", 3)),int(Note("F", 3))]
    FChord = [int(Note("F", 3)),int(Note("Ab", 3)),int(Note("C", 4))]

    bars = [BbmChord,[0,0,0],FChord,FChord,FChord,BbmChord,[0,0,0],FChord,FChord]

    speed = [6,6,2,8,2,6,6,2,10]
  #######################################################################

    # Chorus entrance, bass sleeping
    for r in range(len(openingChorus)):
        for t in range(len(openingChorus[r])):

            time.sleep(opChorusSpeed[r][r]*n)

            time.sleep((opChorusSpeed[r][t]/2)*n)    

    # bass pattern x3
    for h in range(3):
        for i in range(len(bars)):
            if(int(bars[i][0])>0):
             s.noteon(0,bars[i][0],80)
             s.noteon(0,bars[i][1],80)
             s.noteon(0,bars[i][2],80)

            time.sleep(speed[i]*n)

            if(int(bars[i][0])>0):
             s.noteoff(0,bars[i][0])
             s.noteoff(0,bars[i][1])
             s.noteoff(0,bars[i][2])

            time.sleep((speed[i]/2)*n)

    # Last bass pattern cut in half (changing sections)
    for j in range(5):
        if(int(bars[j][0])>0):
            s.noteon(0,bars[j][0],80)
            s.noteon(0,bars[j][1],80)
            s.noteon(0,bars[j][2],80)

        time.sleep(speed[j]*n)

        if(int(bars[j][0])>0):
         s.noteoff(0,bars[j][0])
         s.noteoff(0,bars[j][1])
         s.noteoff(0,bars[j][2])

        time.sleep((speed[j]/2)*n)

    # Chorus Outro featuring i-V-i, bass sleeping   
    for k in range(len(outro)-1):
        for l in range(len(outro[k])):

            time.sleep(ouSpeed[k][l]*n)
            time.sleep((ouSpeed[k][l]/2)*n)

    time.sleep(ouSpeed[2][0]*n)

    time.sleep((ouSpeed[2][0]/2)*n)

    s.delete()   

