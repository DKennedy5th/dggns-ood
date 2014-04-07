import Class_Card
import Helper_Globals

class cardStack(object):
    cardList=[]
    #coordinates=(0,0)
    def __init__(self):
        self.cardList=[]
        self.bitmapList=[]

    def addCard(self,card):
        self.cardList.append(card)

    def returnTopCard(self):
        try:
            try:
                tempBitmap=self.bitmapList.pop()
                tempBitmap.Destroy()
            except:
                pass
            return self.cardList.pop()
        except:
            return None

    def peekCard(self):
        try:
            returnCard=self.cardList.pop()
            self.cardList.append(returnCard)
            return returnCard
        except:
            return None

    def cycleCard(self):
        tempCard=self.cardList.pop(0)
        self.cardList.insert(len(self.cardList),tempCard)

