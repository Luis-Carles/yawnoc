import maths as mat
import time
import fluidsynth as fs
from mingus.containers import Note
import pygame
from pygame import mixer

### Initial declarations and global variables

# The keyboard can be rearranged to add complexity to the association function
notes2octavesDown = [0,Note("C", 2),Note("C#", 2),Note("D", 2),Note("D#", 2),Note("E", 2),Note("F", 2),
Note("F#", 2),Note("G", 2),Note("G#", 2),Note("A", 2),Note("A#", 2),Note("B", 2),Note("C", 3),
Note("C#", 3),Note("D", 3),Note("D#", 3),Note("E", 3),Note("F", 3),Note("F#", 3),Note("G", 3),
Note("G#", 3),Note("A", 3),Note("A#", 3),Note("B", 3)]

notes2octaves = [0,Note("C", 4),Note("C#", 4),Note("D", 4),Note("D#", 4),Note("E", 4),Note("F", 4),
Note("F#", 4),Note("G", 4),Note("G#", 4),Note("A", 4),Note("A#", 4),Note("B", 4),Note("C", 5),
Note("C#", 5),Note("D", 5),Note("D#", 5),Note("E", 5),Note("F", 5),Note("F#", 5),Note("G", 5),
Note("G#", 5),Note("A", 5),Note("A#", 5),Note("B", 5)]

notes2octavesUp = [0,Note("C", 5),Note("C#", 5),Note("D", 5),Note("D#", 5),Note("E", 5),Note("F", 5),
Note("F#", 5),Note("G", 5),Note("G#", 5),Note("A", 5),Note("A#", 5),Note("B", 5),Note("C", 6),
Note("C#", 6),Note("D", 6),Note("D#", 6),Note("E", 6),Note("F", 6),Note("F#", 6),Note("G", 6),
Note("G#", 6),Note("A", 6),Note("A#", 6),Note("B", 6)]

# Chords progressions for Major and Minor Tonalities
chordsMajor = [[[0, 0, 0], [Note('C',3),Note('E',3),Note('G',3)], [Note('D',3),Note('F',3),Note('A',3)], [Note('E',3),Note('G',3),Note('B',3)], [Note('F',3),Note('A',3),Note('C',4)], [Note('G',3),Note('B',3),Note('D',4)], [Note('A',3),Note('C',4),Note('E',4)], [Note('B',3),Note('D',4),Note('F',4)]], 
[[0, 0, 0], [Note('C#',3),Note('F',3),Note('G#',3)], [Note('D#',3),Note('F#',3),Note('A#',3)], [Note('F',3),Note('G#',3),Note('C',4)], [Note('F#',3),Note('A#',3),Note('C#',4)], [Note('G#',3),Note('C',4),Note('D#',4)], [Note('A#',3),Note('C#',4),Note('F',4)], [Note('C',4),Note('D#',4),Note('F#',4)]], 
[[0, 0, 0], [Note('D',3),Note('F#',3),Note('A',3)], [Note('E',3),Note('G',3),Note('B',3)], [Note('F#',3),Note('A',3),Note('C#',4)], [Note('G',3),Note('B',3),Note('D',4)], [Note('A',3),Note('C#',4),Note('E',4)], [Note('B',3),Note('D',4),Note('F#',4)], [Note('C#',3),Note('E',3),Note('G',3)]], 
[[0, 0, 0], [Note('Eb',3),Note('G',3),Note('Bb',3)], [Note('F',3),Note('Ab',3),Note('C',4)], [Note('G',3),Note('Bb',3),Note('D',4)], [Note('Ab',3),Note('C',4),Note('Eb',4)], [Note('Bb',3),Note('D',4),Note('F',4)], [Note('C',3),Note('Eb',3),Note('G',3)], [Note('D',3),Note('F',4),Note('Ab',4)]], 
[[0, 0, 0], [Note('E',3),Note('G#',3),Note('B',3)], [Note('F#',3),Note('A',3),Note('C#',4)], [Note('G#',3),Note('B',3),Note('D#',4)], [Note('A',3),Note('C#',4),Note('E',4)], [Note('B',3),Note('D#',4),Note('F#',4)], [Note('C#',3),Note('E',4),Note('G#',3)], [Note('D#',3),Note('F#',3),Note('A',3)]], 
[[0, 0, 0], [Note('F',3),Note('A',3),Note('C',4)], [Note('G',3),Note('Bb',3),Note('D',4)], [Note('A',3),Note('C',4),Note('E',4)], [Note('Bb',3),Note('D',4),Note('F',4)], [Note('C',3),Note('E',3),Note('G',3)], [Note('D',3),Note('F',4),Note('A',3)], [Note('E',3),Note('G',3),Note('Bb',3)]], 
[[0, 0, 0], [Note('F#',3),Note('A#',3),Note('C#',4)], [Note('G#',3),Note('B',3),Note('D#',4)], [Note('A#',3),Note('C#',4),Note('E#',4)], [Note('B',3),Note('D#',4),Note('F#',4)], [Note('C#',3),Note('E#',3),Note('G#',3)], [Note('D#',3),Note('F#',3),Note('A',3)], [Note('F',3),Note('G#',3),Note('B',3)]], 
[[0, 0, 0], [Note('G',3),Note('B',3),Note('D',4)], [Note('A',3),Note('C',4),Note('E',4)], [Note('B',3),Note('D',4),Note('F#',4)], [Note('C',3),Note('E',3),Note('G',3)], [Note('D',3),Note('F#',3),Note('A',3)], [Note('E',3),Note('G',3),Note('B',3)], [Note('F#',3),Note('A',3),Note('C',4)]], 
[[0, 0, 0], [Note('Ab',3),Note('C',4),Note('Eb',4)], [Note('Bb',3),Note('Db',4),Note('F',4)], [Note('C',3),Note('Eb',4),Note('G',3)], [Note('Db',3),Note('F',4),Note('Ab',4)], [Note('Eb',3),Note('G',3),Note('Bb',3)], [Note('F',3),Note('Ab',4),Note('C',4)], [Note('G',3),Note('Bb',3),Note('Db',4)]], 
[[0, 0, 0], [Note('A',3),Note('C#',4),Note('E',4)], [Note('B',3),Note('D',4),Note('F#',4)], [Note('C#',3),Note('E',3),Note('G#',3)], [Note('D',3),Note('F#',3),Note('A',3)], [Note('E',3),Note('G#',3),Note('B',3)], [Note('F#',3),Note('A',3),Note('C#',4)], [Note('G#',3),Note('B',3),Note('D',4)]], 
[[0, 0, 0], [Note('Bb',3),Note('D',4),Note('F',4)], [Note('C',3),Note('Eb',4),Note('G',3)], [Note('D',3),Note('F',3),Note('A',3)], [Note('Eb',3),Note('G',3),Note('Bb',3)], [Note('F',3),Note('A',3),Note('C',4)], [Note('G',3),Note('Bb',3),Note('D',4)], [Note('A',3),Note('C',4),Note('Eb',4)]], 
[[0, 0, 0], [Note('B',3),Note('D#',4),Note('F#',4)], [Note('C#',3),Note('E',4),Note('G#',3)], [Note('D#',3),Note('F#',3),Note('A',3)], [Note('E',3),Note('G#',3),Note('B',3)], [Note('F#',3),Note('A',3),Note('C#',4)], [Note('G#',3),Note('B',3),Note('D#',4)], [Note('A#',3),Note('C#',4),Note('E',4)]]]

chordsMinor = [[[0, 0, 0], [Note('C',3),Note('Eb',3),Note('G',3)], [Note('D',3),Note('F',3),Note('Ab',3)], [Note('E',3),Note('G#',3),Note('B',3)], [Note('F',3),Note('Ab',3),Note('C',4)], [Note('G',3),Note('Bb',3),Note('D',4)], [Note('A',3),Note('C#',4),Note('E',4)], [Note('B',3),Note('D#',4),Note('F#',4)]], 
[[0, 0, 0], [Note('C#',3),Note('E',3),Note('G#',3)], [Note('D#',3),Note('F#',3),Note('A',3)], [Note('E#',3),Note('A',3),Note('C',4)], [Note('F#',3),Note('A',3),Note('C#',4)], [Note('G#',3),Note('B',4),Note('D#',4)], [Note('A#',3),Note('D',4),Note('E#',4)], [Note('B',3),Note('E',4),Note('G',4)]], 
[[0, 0, 0], [Note('D',3),Note('F',3),Note('A',3)], [Note('E',3),Note('G',3),Note('Bb',3)], [Note('F#',3),Note('A#',3),Note('C#',4)], [Note('G',3),Note('Bb',3),Note('D',4)], [Note('A',3),Note('C',4),Note('E',4)], [Note('B',3),Note('D#',4),Note('F#',4)], [Note('C#',3),Note('F',4),Note('G#',3)]], 
[[0, 0, 0], [Note('Eb',3),Note('Gb',3),Note('Bb',3)], [Note('F',3),Note('Ab',3),Note('B',3)], [Note('G',3),Note('B',3),Note('D',4)], [Note('Ab',3),Note('B',3),Note('Eb',4)], [Note('Bb',3),Note('C#',4),Note('F',4)], [Note('C',3),Note('E',3),Note('G',3)], [Note('D',3),Note('F#',4),Note('A',4)]], 
[[0, 0, 0], [Note('E',3),Note('G',3),Note('B',3)], [Note('F#',3),Note('A',3),Note('C',4)], [Note('G#',3),Note('C',4),Note('D#',4)], [Note('A',3),Note('C',4),Note('E',4)], [Note('B',3),Note('D',4),Note('F#',4)], [Note('C#',3),Note('F',3),Note('G#',3)], [Note('D#',3),Note('G',3),Note('A#',3)]], 
[[0, 0, 0], [Note('F',3),Note('Ab',3),Note('C',4)], [Note('G',3),Note('Bb',3),Note('Db',4)], [Note('A',3),Note('C#',4),Note('E',4)], [Note('Bb',3),Note('Db',4),Note('F',4)], [Note('C',3),Note('Eb',4),Note('G',3)], [Note('D',3),Note('F#',3),Note('A',3)], [Note('E',3),Note('G#',3),Note('B',3)]], 
[[0, 0, 0], [Note('F#',3),Note('A',3),Note('C#',4)], [Note('G#',3),Note('B',3),Note('D',4)], [Note('A#',3),Note('D',4),Note('F',4)], [Note('B',3),Note('D',4),Note('F#',4)], [Note('C#',3),Note('E',3),Note('G#',3)], [Note('D#',3),Note('G',3),Note('A',3)], [Note('F',3),Note('A',3),Note('C',4)]], 
[[0, 0, 0], [Note('G',3),Note('Bb',3),Note('D',4)], [Note('A',3),Note('C',4),Note('Eb',4)], [Note('B',3),Note('D#',4),Note('F#',4)], [Note('C',3),Note('Eb',3),Note('G',3)], [Note('D',3),Note('F',3),Note('A',3)], [Note('E',3),Note('G#',3),Note('B',3)], [Note('F#',3),Note('A#',3),Note('C#',4)]], 
[[0, 0, 0], [Note('Ab',3),Note('B',3),Note('Eb',4)], [Note('Bb',3),Note('Db',4),Note('E',4)], [Note('C',3),Note('E',4),Note('G',3)], [Note('Db',3),Note('E',3),Note('Ab',3)], [Note('Eb',3),Note('Gb',3),Note('Bb',3)], [Note('F',3),Note('A',4),Note('C',4)], [Note('G',3),Note('B',3),Note('D',4)]], 
[[0, 0, 0], [Note('A',3),Note('C',4),Note('E',4)], [Note('B',3),Note('D',4),Note('F',4)], [Note('C#',3),Note('F',3),Note('G#',3)], [Note('D',3),Note('F',3),Note('A',3)], [Note('E',3),Note('G',3),Note('B',3)], [Note('F#',3),Note('A#',3),Note('C#',4)], [Note('G#',3),Note('C',4),Note('D#',4)]], 
[[0, 0, 0], [Note('Bb',3),Note('Db',4),Note('F',4)], [Note('C',3),Note('Eb',4),Note('Gb',3)], [Note('D',3),Note('F#',4),Note('A',3)], [Note('Eb',3),Note('Gb',3),Note('Bb',3)], [Note('F',3),Note('Ab',3),Note('C',4)], [Note('G',3),Note('B',3),Note('D',4)], [Note('A',3),Note('C#',4),Note('E',4)]], 
[[0, 0, 0], [Note('B',3),Note('D',4),Note('F#',4)], [Note('C#',3),Note('E',4),Note('G',3)], [Note('D#',3),Note('G',3),Note('A',3)], [Note('E',3),Note('G',3),Note('B',3)], [Note('F#',3),Note('Ab',3),Note('C#',4)], [Note('G#',3),Note('C',4),Note('D#',4)], [Note('A#',3),Note('D',4),Note('F',4)]]]

# Soundfonts 
instruments =["\yamahap45.sf2","\R-violin.sf2","\drums","\TEK bass.sf2"]



### Sound Libraries and Music Generation

def getMod (mApproach):
 if(mApproach==1):
     return [25,4,0]                  # Two octaves of twelve notes, plus silence with piano
 if(mApproach==2):
     return [8,2,0]                   # Assuming no modulations, each of the seven chords of a key with piano
 if(mApproach==3):
     return [5,1,2]                   # Bass drum, snare drum, finalD and hi hat, plus silence
 if(mApproach==4):
     return [25,4,1]                  # Two octaves of twelve notes, plus silence with violin
 if(mApproach==5):
     return [25,4,3]                  # Two octaves of twelve notes, plus silence with bass

def nOf(value,mApproach,mode,key):
 if(mApproach==1):
     print(notes2octaves[value])
     return notes2octaves[value]
 if(mApproach==2):
     if(mode==0):
            print(chordsMajor[key][value])
            return chordsMajor[key][value]
     if(mode==1):
            print(chordsMinor[key][value])
            return chordsMinor[key][value]           
 if(mApproach==4):
     print(notes2octavesUp[value])
     return notes2octavesUp[value]
 if(mApproach==5):
     print(notes2octavesDown[value])
     return notes2octavesDown[value]

def music (universe,mApproach,speed,mode,key):
 gm= getMod(mApproach)
 module=gm[0]
 u=gm[1]
 sf2 = instruments [gm[2]]
 ins = ".\soundfonts"+ sf2
 
 # Call to the hypothetic function reproduce(instrument,key(universe),speed)

 if(mApproach==3):                                 #Pygame for Drum kit
        pygame.init()
        bassDrum = mixer.Sound(ins+"\BassDrum.WAV")
        snareDrum = mixer.Sound(ins+"\SnareDrum.WAV")
        hihat = mixer.Sound(ins+"\Hihat.WAV")
        finalDrum = mixer.Sound(ins+"\FinalDrum.WAV")

        n = mat.divideEtImpera(universe,u) % module
        if(n==0):
            time.sleep(speed)
            time.sleep(speed)
        if(n==1):
            bassDrum.play()
            time.sleep(speed)
        if(n==2):
            snareDrum.play()            
            time.sleep(speed)
        if(n==3):
            hihat.play()
            time.sleep(speed/2)
        if(n==4):
            finalDrum.play()
            time.sleep(speed)
 else:
     if(mApproach==2):
            s = fs.Synth(gain=0.5)                              #Fluidsynth for chords
            s.start()

            soundfont = s.sfload(ins)
            s.program_select(0,soundfont,0,0)

            n = nOf(mat.divideEtImpera(universe,u) % module,mApproach,mode,key)
            if(n[0]==0):
                time.sleep(speed)
                time.sleep(speed)
            else:
                s.noteon(0,int(n[0]),80)
                s.noteon(0,int(n[1]),80)
                s.noteon(0,int(n[2]),80)
                time.sleep(speed)

                s.noteoff(0,int(n[0]))
                s.noteoff(0,int(n[1]))
                s.noteoff(0,int(n[2]))
                time.sleep(speed)

                s.delete()
     else:
            s = fs.Synth()                              #Fluidsynth for notes
            s.start()

            soundfont = s.sfload(ins)
            s.program_select(0,soundfont,0,0)

            n = nOf(mat.divideEtImpera(universe,u) % module,mApproach,mode,key)
            if(n==0):
                time.sleep(speed)
                time.sleep(speed)
            else:
                s.noteon(0,int(n),80)

                time.sleep(speed)

                s.noteoff(0,int(n))

                time.sleep(speed)

                s.delete()