#as a semi-joke just put 2 of the same item in a box and then move onto the next. It fits and it isn't the most inefficient, uses roughly half as many boxes as 1 item per box
#in the attempt of making it based off of length and width mostly, I realized that I had no idea how to make a good grid system represented in code so I threw that away
class Bin:
        def __init__(self):
            self.length=0
            self.width=0
            self.height=0
            self.items=[]
            self.leftSpace=[self]

        def SetDimension(self, length, width, height):
            self.length=length
            self.width=width
            self.height=height
            self.leftSpace=[self]

        def leftSpace(self, length, width, height):
            self.length = length
            self.width = width
            self.height = height


        def PutItem(self, item):
            for bin in self.leftSpace:
                if (bin.IsHoldable(item)):
                    bin.items.append(item)
                    unhelditems.remove(item)
                    #calculate spaceLeft
                    self.leftSpace.remove(bin)
                    #update spaceLeft
                    strip1=Bin()
                    strip1.length=bin.length
                    strip1.width=bin.width-item.width
                    strip1.height=item.height
                    self.leftSpace.append(strip1)
                    strip2=Bin()
                    strip2.length=item.length
                    strip2.width=bin.width-item.width
                    strip2.height=item.height
                    self.leftSpace.append(strip2)
                    strip3=Bin()
                    strip3.length=bin.length
                    strip3.width=bin.width
                    strip3.height=bin.height-item.height
                    self.leftSpace.append(strip3)

                else:
                    bin.NewBin(item)

        def UpdateLeftSpace(self, item):
            pass

        def IsHoldable(self, item):
            for i in range(6):
                item.RotateTo(i)
                if self.length>=item.length and self.width>= item.width and self.height>=item.height:
                    return True
                else:
                    return False

        def NewBin(self,item):
            #where full bins go and a new bin is put in
            fullbins.append(bin)
            bin.PutItem(item) #this is where the new bin would be put in


class Item:
    def __init__(self):
        self.length=0
        self.width = 0
        self.height = 0
        self.orientation = 0

    def SetDimension(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def GetCurrOrient(self):
        if self.length>=self.width and self.width>=self.height:
            self.orientation=0
        elif self.length>=self.height and self.height>=self.width:
            self.orientation=1
        elif self.width>=self.length and self.length>=self.height:
            self.orientation=2
        elif self.width>=self.height and self.height>=self.length:
            self.orientation=3
        elif self.height>=self.length and self.length>=self.width:
            self.orientation=4
        else:
            self.orientation=5

    def RotateTo(self, new_orient):
        list=[self.length, self.width, self.height]
        list.sort()
        if new_orient==0:
            self.height=list[2]
            self.width=list[1]
            self.length=list[0]
        else:
            pass

class BinList:
    def __init__(self):
        bins=[]
        bins.append(Bin())

    def DropAllItems(self, items):
        pass

fullbins=[]
unhelditems=[]
workingitems=[] #seeing if this gets rid of the x not in list error when trying to remove items
bin1=Bin()
bin2=Bin()
bin3=Bin()
bin4=Bin()
bin1.SetDimension(12,9,6)
#10 items
item1=Item()
item1.SetDimension(5,4,3)
item2=Item()
item2.SetDimension(5,4,3)
item3=Item()
item3.SetDimension(3,3,3)
item4=Item()
item4.SetDimension(3,3,3)
item5=Item()
item5.SetDimension(3,3,3)
item6=Item()
item6.SetDimension(3,3,3)
item7=Item()
item7.SetDimension(3,3,3)
item8=Item()
item8.SetDimension(3,3,3)
item9=Item()
item9.SetDimension(6,2,2)
item10=Item()
item10.SetDimension(6,2,2)
unhelditems.append(item1)
unhelditems.append(item2)
unhelditems.append(item3)
unhelditems.append(item4)
unhelditems.append(item5)
unhelditems.append(item6)
unhelditems.append(item7)
unhelditems.append(item8)
unhelditems.append(item9)
unhelditems.append(item10)
for i in range(len(unhelditems)-1):
    workingitems[i]=unhelditems[i]
bins=[Bin() for i in range(len(unhelditems))]#this creates the max amount of bins needed for the amount of items, 1 bin per item
for bin in bins:
    bin.SetDimension(12,9,6)
#something like while unhelditems is not empty, bin[i].putitem(unhelditems[i})
b=0 #this is for which bin in the list of bins
while len(unhelditems) != 0:
    for i in range(10):
        bins[b].PutItem(unhelditems[i])

#fill in the bins with the items here
print("10 items takes "+str(len(fullbins))+" bins")
#20 items

#30 items