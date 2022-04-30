#as a semi-joke just put 2 of the same item in a box and then move onto the next. It fits and it isn't the most inefficient
class Bin:
        def __init__(self):
            self.length=0
            self.width=0
            self.height=0
            self.items=[]
            self.leftSpace=[]

        def SetDimension(self, length, width, height):
            self.length=length
            self.width=width
            self.height=height
            self.leftSpace=[self]

        def PutItem(self, item):
            for bin in self.leftSpace:
                if (bin.IsHoldable(item)):
                    bin.items.append(item)
                    #calculate spaceLeft
                    #update spaceLeft
            pass

        def UpdateLeftSpace(self, item):
            pass

        def IsHoldable(self, item):
            for i in range(6):
                item.RotateTo(i)
                if self.length>=item.length and self.width>= item.width and self.height>=item.height:
                    return True
            return False


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