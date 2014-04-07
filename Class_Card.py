import os

class card(object):
    suit = 0
    rank = 0
    img = ''
    def createCard(self,s,r):
        self.suit = s
        self.rank = r
        self.img = os.getcwd()+"\\images\\"+self.returnRank()+"_of_"+self.returnSuit()+".PNG"

    def returnName(self):
        return self.returnRank()+" of "+self.returnSuit()
    
    def returnSuit(self):
        return suitToString(self.suit)

    def returnRank(self):
        global rank
        return rankToString(self.rank)

    def returnImg(self):
        return self.img

def rankToString(i):
    return str({
           0:'Ace',
           1:'2',
           2:'3',
           3:'4',
           4:'5',
           5:'6',
           6:'7',
           7:'8',
           8:'9',
           9:'10',
           10:'Jack',
           11:'Queen',
           12:'King',
           }[i])

def suitToString(i):
    return str({
           0: 'Clubs',
           1: 'Spades',
           2: 'Hearts',
           3: 'Diamonds'
           }[i])