import Class_Card_Stack
import Class_Card
import math
import random
from Helper_Globals import debug

class deck(Class_Card_Stack.cardStack):
    def __init__(self):
        super(deck,self).__init__()
        self.stack=self
        self.bitmapList=[]
    def createDeck(self):
        i=0
        for x in xrange(0,4):
            for y in xrange(0,13):
                tempCard=Class_Card.card()
                tempCard.createCard(x,y)
                self.cardList.append(tempCard)
                if(debug):
                    print super(deck,self).peekCard().returnName()
                i+=1
        self.shuffleDeck()

    def shuffleDeck(self):
        tempDeck = []
        while (len(self.cardList)>0):
            tempRand=int(random.random()*len(self.cardList))
            tempCard=self.cardList.pop(tempRand)
            tempDeck.append(tempCard)
            if(debug):
                print str(tempRand)+" ("+tempCard.returnName()+") should be less than "+str(len(self.cardList)+1)
        self.cardList=tempDeck