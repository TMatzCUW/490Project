#This one is to put as many of the same item in a bin as possible. No mixing here
#Can fit 8 A in a bin, 24 B, 24 C without rotating
#I know this is not fancy or elegant but to be fair, it does work fairly well
import math

aItems=0
bItems=0
cItems=0
aMax=8
bMax=24
cMax=24
bins=0
#10 items should be 3 bins
def LevelOne():
    aItems=2
    bItems=6
    cItems=2
    a=int(math.ceil(aItems/aMax))#math.ceil rounds up so I don't get .25 of a bin
    b=int(math.ceil(bItems/bMax))
    c=int(math.ceil(cItems/cMax))
    bins=a+b+c
    print("Level One will take "+str(bins)+" bins")
#20 items should be 3 bins again
def LevelTwo():
    aItems=5
    bItems=10
    cItems=5
    a=int(math.ceil(aItems/aMax))#math.ceil rounds up so I don't get .25 of a bin
    b=int(math.ceil(bItems/bMax))
    c=int(math.ceil(cItems/cMax))
    bins=a+b+c
    print("Level One will take "+str(bins)+" bins")
#30 items should be 4 bins
def LevelThree():
    aItems=12
    bItems=12
    cItems=6
    a=int(math.ceil(aItems/aMax))#math.ceil rounds up so I don't get .25 of a bin
    b=int(math.ceil(bItems/bMax))
    c=int(math.ceil(cItems/cMax))
    bins=a+b+c
    print("Level One will take "+str(bins)+" bins")
LevelOne()
LevelTwo()
LevelThree()