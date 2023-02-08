### Moore Neighborhood

def neighborhood(universe, x, y):
    n = 0
    if(y==0) and (x==0):        #upper left corner
         n=n+universe[y][x+1]
         n=n+universe[y+1][x]
         n=n+universe[y+1][x+1]

    if(y==0) and (x==len(universe[0])-1):    #upper right corner
         n=n+universe[y][x-1]
         n=n+universe[y+1][x-1]
         n=n+universe[y+1][x]

    if(y==0) and (0<x) and (x<len(universe[0])-1):    #upper limit
         n=n+universe[y][x-1]
         n=n+universe[y][x+1]
         n=n+universe[y+1][x-1]
         n=n+universe[y+1][x]
         n=n+universe[y+1][x+1]                          

    if(y==len(universe)-1) and (x==0):     #lower left corner
         n=n+universe[y][x+1]
         n=n+universe[y-1][x]
         n=n+universe[y-1][x+1]

    if(y==len(universe)-1) and (x==len(universe[0])-1):     #lower right corner    
         n=n+universe[y][x-1]
         n=n+universe[y-1][x-1]
         n=n+universe[y-1][x]

    if(y==len(universe)-1) and (0<x) and(x<len(universe[0])-1):   #lower limit     
         n=n+universe[y][x-1]
         n=n+universe[y][x+1]
         n=n+universe[y-1][x-1]
         n=n+universe[y-1][x]
         n=n+universe[y-1][x+1]

    if(0<y<len(universe)-1) and (x==0):     #western limit
         n=n+universe[y][x+1]
         n=n+universe[y-1][x]
         n=n+universe[y-1][x+1]
         n=n+universe[y+1][x]
         n=n+universe[y+1][x+1]

    if(0<y) and (y<len(universe)-1) and (x==len(universe[0])-1):     #eastern limit                           
         n=n+universe[y][x-1]
         n=n+universe[y-1][x]
         n=n+universe[y-1][x-1]
         n=n+universe[y+1][x]
         n=n+universe[y+1][x-1]

    if(0<y) and (y<len(universe)-1) and (0<x) and (x<len(universe[0])-1):     #any other cell
         n=n+universe[y][x-1]
         n=n+universe[y][x+1]
         n=n+universe[y-1][x-1]
         n=n+universe[y-1][x]
         n=n+universe[y-1][x+1]
         n=n+universe[y+1][x-1]
         n=n+universe[y+1][x]
         n=n+universe[y+1][x+1]
                            
    return n



### Game of life Rules

def nextState(universe):
    
    height = len(universe)
    width = len(universe[0])
    
    nextUniverse = [[0] * width for _ in range(height)]

    #calculating new state
    for y in range(height):
        for x in range(width):
                if(universe[y][x]==0) and (neighborhood(universe,x,y)==3): #Dead Cell Reborn with 3 living cells
                        nextUniverse[y][x]=1
                if(universe[y][x]==1) and (neighborhood(universe,x,y)==2): #Living cell remains alive with 2 living cells
                        nextUniverse[y][x]=1 
                if(universe[y][x]==1) and (neighborhood(universe,x,y)==3): #Living cell remains alive with 3 living cells
                        nextUniverse[y][x]=1


    return nextUniverse

