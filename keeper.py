import maths as mat
import actualize as a
from music import getMod 
import random
import numpy as nm
from progress.bar import Bar


###Searching

# Searching for an initial configuration that satisfies the values given
def findConfiguration(mApproach,universeD,searchL,values):
 dimXgrid = universeD
 dimYgrid = universeD  
 searchLimit = searchL

 gm = getMod(mApproach)
 module = gm[0]
 u = gm[1]

 fileName = ''
 if(mApproach==1):
        fileName = 'melodic piano '                 # Two octaves of twelve notes, plus silence with piano
 if(mApproach==2):
        fileName = 'armonic piano '                 # Assuming no modulations, each of the seven chords of a key with piano
 if(mApproach==3):
        fileName = 'drums '                         # Bass drum, snare drum, cymbal and hi hat, plus silence
 if(mApproach==4):
        fileName = 'melodic violin '                # Two octaves of twelve notes, plus silence with violin
 if(mApproach==5):
        fileName = 'melodic bass '                  # Two octaves of twelve notes, plus silence with bass

 file = ''

 configuration = [[ 0  for i in range(dimXgrid)] for j in range(dimYgrid)]
 obtained = [ 0  for i in range(len(values))]

 resul = nm.array(configuration)
 found = False

 limit = searchLimit
 limitbar =limit/100

 with Bar('Searching', fill='║', suffix='%(percent).1f%% - %(eta)ds') as bar:
  while(not found) and (limit>0):
        configuration = [[ random.choice([0,0,0,0,1,1]) for i in range(dimXgrid)] for j in range(dimYgrid)]
        resul = configuration
        ep = True
        cont = 0
        contBar = 100

        while(cont<len(values)) and (ep):
            obtained[cont]= (mat.divideEtImpera(configuration,u)) % module

            if(obtained[cont]!=values[cont]):
                ep = False

            cont+=1
            configuration = a.nextState(configuration)

        if(obtained==values):
            found=True
            nm.savetxt(fileName + str(limit)+'.txt',resul,fmt='%d')
            file = fileName + str(limit)+'.txt'

            for x in range(contBar):
                bar.next()


        if(found== False):
            if(limit % limitbar==0):
             bar.next()
             contBar -= 1

        limit -=1


 if(found==True):
     return[0,file]
 else:
     return[1,file]



### Checking

# Checking given values
def checkConfiguration(mApproach,values,file):
 gm = getMod(mApproach)
 module = gm[0]
 u = gm[1]

 data = nm.loadtxt(file, dtype=int)
 obtained = [ module+2  for i in range(len(values))]

 for x in range(len(values)):
    obtained[x] = (mat.divideEtImpera(data,u)) % module
    data = a.nextState(data)

 print(values)
 print(obtained) 
