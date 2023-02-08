from sympy import *
import numpy as nm
from mpmath import *

ulam_aux = [[100,99,98,97,96,95,94,93,92,91],
[65,64,63,62,61,60,59,58,57,90],
[66,37,36,35,34,33,32,31,56,89],
[67,38,17,16,15,14,13,30,55,88],
[68,39,18,5,4,3,12,29,54,87],
[69,40,19,6,1,2,11,28,53,86],
[70,41,20,7,8,9,10,27,52,85],
[71,42,21,22,23,24,25,26,51,84],
[72,43,44,45,46,47,48,49,50,83],
[73,74,75,76,77,78,79,80,81,82]]

ulam = nm.array(ulam_aux)

### Association Function between Conway's Game of Life and Sound

# Mutates the obtained value with Riemann Zeta Function  
def mutate (value):
 finalValue=value
 if(value!=0):
        s= nm.absolute(zeta(0.5+value*j))
        finalValue+=round(s)

 return finalValue

# Mathematical relationship between the state of the universe and the chosen module
def associationFunction(universe,u):
 height = len(universe)
 width = len(universe[0])

 value=0
    ### Combinatorics with prime numbers and Ulam Spiral

 i=1
 for y in range(height):
        for x in range(width):
            if(universe[y][x]==1) and (isprime(ulam[y][x])):    # Alive Prime in Ulam Spiral
                    value+=3*u
            if(universe[y][x]==1) and (not isprime(ulam[y][x])):    # Alive Cell in Ulam Spiral
                    value+=1*u
            if(universe[y][x]==1) and (isprime(i)):    # Alive Prime
                    value+=3*u
            if(universe[y][x]==1) and (not isprime(i)):    # Alive Cell
                    value+=1*u
            try:
                if(universe[y-1][x-1]==1) and (isprime(i-(height-1)-1)):   # Alive Prime in upper left diagonal
                    value+=1*u
            except:
                value+=0
            try:
                if(universe[y-1][x+1]==1) and (isprime(i-(height-1)+1)):   # Alive Prime in upper right diagonal
                    value+=1*u
            except:
                value+=0            
            try:
                if(universe[y+1][x-1]==1) and (isprime(i+(height-1)-1)):   # Alive Prime in lower left diagonal
                    value+=1*u
            except:
                value+=0  
            try:
                if(universe[y+1][x+1]==1) and (isprime(i+(height-1)+1)):   # Alive Prime in lower right diagonal
                    value+=1*u
            except:
                value+=0 

            i+=1

 # Both Twin Prime Numbers Alive
 if(universe[0][2]==1) and (universe[0][4]==1):
        value+=4*u
 if(universe[0][4]==1) and (universe[0][6]==1):
        value+=4*u        
 if(universe[1][0]==1) and (universe[1][2]==1):
        value+=4*u
 if(universe[1][6]==1) and (universe[1][8]==1):
        value+=4*u
 if(universe[2][8]==1) and (universe[3][0]==1):
        value+=4*u       
 if(universe[4][0]==1) and (universe[4][2]==1):
        value+=4*u
 if(universe[5][8]==1) and (universe[6][0]==1):
        value+=4*u  
 if(universe[7][0]==1) and (universe[7][2]==1):
        value+=4*u


 # Both Twin Prime Numbers Alive in Ulam Spiral
 if(universe[4][5]==1) and (universe[4][3]==1):
        value+=4*u
 if(universe[4][3]==1) and (universe[6][3]==1):
        value+=4*u
 if(universe[5][6]==1) and (universe[3][6]==1):
        value+=4*u
 if(universe[3][2]==1) and (universe[5][2]==1):
        value+=4*u
 if(universe[4][7]==1) and (universe[2][7]==1):
        value+=4*u 
 if(universe[6][1]==1) and (universe[8][1]==1):
        value+=4*u
 if(universe[1][6]==1) and (universe[1][4]==1):
        value+=4*u 
 if(universe[7][0]==1) and (universe[9][0]==1):
        value+=4*u

    ### Symmetry

 axis=[9,8,7,6,5,4,3,2,1,0]
 distances = [9,7,5,3,1,-1,-3,-5,-7,-9]
 dist=0

 for y in range(len(universe)):
        for x in range (len(universe[0])):
            dist = axis[x]-y
            if(universe[y][x]==1) and (universe[y+dist][x+dist]==1):       # Dextroversely, lower-upper Diagonal
                 value+=1*u

            if(universe[y][x]==1) and (universe[x][y]==1):                 # Dextroversely, upper-lower Diagonal
                 value+=1*u

            if(universe[y][x]==1) and (universe[y+distances[y]][x]==1):    # Horizontal axis
                 value+=1*u

            if(universe[y][x]==1) and (universe[y][x+distances[x]]==1):    # Vertical axis
                 value+=1*u

 return value

# Divides the universe in 10x10 arrays and return the combined value
def divideEtImpera(universe,u):

 height = len(universe)
 width = len(universe[0])
 
 array = [[ 0  for i in range(10)] for j in range(10)]
 value= 0

 i = 0
 j = 0
 for m in range(int(width/10)):             # Value is updated m x n =  len(universe)/10 *2
     for n in range(int(height/10)):  
            for y in range(10):        # Each array evaluated individually has 10x10 elements
                for x in range(10):
                    array[y][x]=universe[y+j][x+i]
            
            value+=associationFunction(array,u)

            i+=10
     i=0       
     j+=10       
 
 value=mutate(value)
 return value


 
    


