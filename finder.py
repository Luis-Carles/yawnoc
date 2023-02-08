import keeper as k

###Initial declarations and global parameters

mApproach = 1
universeD = 100
searchL = 1000

values = []

allGood = [False,False,False,False]



### Setting the searching Parameters

# mApproach
while(not allGood[0]):
    try:
        mApproach = int(input("\nChoose one musical approach \n\n"
        + "\n\t1: Melodic Piano"
        + "\n\t2: Armonic Piano"
        + "\n\t3: Rhytmic & Drums"
        + "\n\t4: Melodic Violin"
        + "\n\t5: Melodic Bass\n\n"))
    except ValueError:
        print("mApproach must be an integer")
        exit(-1)

    if (mApproach<1) or (mApproach>5):
        print("\nERROR: wrong musical approach, \n\nmust use a"
        +"\n\tnumber between 1-5 for:"
        +"\n\t[musical approach]")
    else:
        allGood[0] = True

# universe dimension
while(not allGood[1]):
    try:
        universeD = int(input("\nChoose one universe dimension \n\n"
        + "\n\tmust be a multiple of 10\n\n"))
    except ValueError:
        print("universe dimension must be an integer")
        exit(-1)

    if ((universeD%10)!=0):
        print("\nERROR: wrong universe dimension, \n\nmust use a"
        +"\n\tmultiple of 10 for:"
        +"\n\t[universe's Dimension]")
    else:
        allGood[1] = True

# search limit
while(not allGood[2]):
    try:
        searchL = int(input("\nChoose one limit for analyzed configurations \n\n"
        + "\n\tmust be a multiple of 100\n\n"))
    except ValueError:
        print("search limit must be an integer")
        exit(-1)

    if ((searchL%100)!=0):
        print("\nERROR: wrong search limit, \n\nmust use a"
        +"\n\tmultiple of 100 for:"
        +"\n\t[search limit]")
    else:
        allGood[2] = True


### Setting the set of values to be achieved

v = -5
# 2 octaves piano
if(mApproach==1):
    print("\nNotes distribution and its associated number \n\n"
    + "\n\t▀  C4  C#4 D4  D#4  E4  F4  F#4 G4  G#4 A4  A#4 B4"
    + "\n\t0   1  2   3    4   5   6    7  8   9   10  11  12"
    + "\n\t"
    + "\n\t   C5  C#5 D5  D#5  E5  F5  F#5 G5  G#5 A5  A#5 B5"
    + "\n\t   13  14  15  16   17  18  19  20  21  22  23  24"
    + "\n\t")
    print("▀ stands for silence. Type -1 to terminate")

    while(not allGood[3]):
        try:
            v = int(input("Introduce next note: \n\n"))
        except ValueError:
            print("introduced note must be an integer")

        if(v<-1) or (v>24):
            print("introduced note must be between -1 - 24")
        else:
            if(v==-1):
                allGood[3] = True
            else:
                values.append(v)

# 7 chords
if(mApproach==2):
    print("\nChords distribution and its associated number \n\n"
    + "\n\t             Major Tonality           "
    + "\n\t▀   I   ii  iii   IV   V   vi  viidim "
    + "\n\t0   1   2    3    4    5   6     7    "
    + "\n\t"
    + "\n\t             Minor Tonality           "
    + "\n\t▀   i  iidim   III   iv   v   VI  VII "
    + "\n\t0   1    2      3    4    5   6    7  "
    + "\n\t")
    print("▀ stands for silence. Type -1 to terminate")

    while(not allGood[3]):
        try:
            v = int(input("Introduce next chord: \n\n"))
        except ValueError:
            print("introduced chord must be an integer")

        if(v<-1) or (v>7):
            print("introduced chord must be between -1 - 7")
        else:
            if(v==-1):
                allGood[3] = True
            else:
                values.append(v)

# Drums
if(mApproach==3):
    print("\nDrum hits distribution and its associated number \n\n"
    + "\n\t▀    BassDrum   SnareDrum   HiHat   Tum(FinalDrum)"
    + "\n\t0       1           2         3            4      "
    + "\n\t")
    print("▀ stands for silence. Type -1 to terminate")

    while(not allGood[3]):
        try:
            v = int(input("Introduce next hit: \n\n"))
        except ValueError:
            print("introduced hit must be an integer")

        if(v<-1) or (v>4):
            print("introduced hit must be between -1 - 4")
        else:
            if(v==-1):
                allGood[3] = True
            else:
                values.append(v)

# 2 octaves violin
if(mApproach==4):
    print("\nNotes distribution and its associated number \n\n"
    + "\n\t▀  C5  C#5 D5  D#5  E5  F5  F#5 G5  G#5 A5  A#5 B5"
    + "\n\t0   1  2   3    4   5   6    7  8   9   10  11  12"
    + "\n\t"
    + "\n\t   C6  C#6 D6  D#6  E6  F6  F#6 G6  G#6 A6  A#6 B6"
    + "\n\t   13  14  15  16   17  18  19  20  21  22  23  24"
    + "\n\t")
    print("▀ stands for silence. Type -1 to terminate")

    while(not allGood[3]):
        try:
            v = int(input("Introduce next note: \n\n"))
        except ValueError:
            print("introduced note must be an integer")

        if(v<-1) or (v>24):
            print("introduced note must be between -1 - 24")
        else:
            if(v==-1):
                allGood[3] = True
            else:
                values.append(v)

# 2 octaves bass
if(mApproach==5):
    print("\nNotes distribution and its associated number \n\n"
    + "\n\t▀  C2  C#2 D2  D#2  E2  F2  F#2 G2  G#2 A2  A#2 B2"
    + "\n\t0   1  2   3    4   5   6    7  8   9   10  11  12"
    + "\n\t"
    + "\n\t   C3  C#3 D3  D#3  E3  F3  F#3 G3  G#3 A3  A#3 B3"
    + "\n\t   13  14  15  16   17  18  19  20  21  22  23  24"
    + "\n\t")
    print("▀ stands for silence. Type -1 to terminate")

    while(not allGood[3]):
        try:
            v = int(input("Introduce next note: \n\n"))
        except ValueError:
            print("introduced note must be an integer")

        if(v<-1) or (v>24):
            print("introduced note must be between -1 - 24")
        else:
            if(v==-1):
                allGood[3] = True
            else:
                values.append(v)



# Calls to keeper.py
resul = k.findConfiguration(mApproach,universeD,searchL,values)

if (resul[0]==1):
    print("Unsuccessful Search")
else:
    print("Successful Search, Checking: \n\n")
    k.checkConfiguration(mApproach,values,resul[1])



