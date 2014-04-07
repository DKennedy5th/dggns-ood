import wx
import Class_Deck
import Class_Card_Stack
import Image
from Helper_Globals import debug

class gameScreen(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        drag={}
        #drawnCard,baseFirst,baseSecond,baseThird,baseFourth,tempFirst,tempSecond,tempThird,tempFourth=Class_Card_Stack.cardStack()
        #acceptors=[drawnCard,baseFirst,baseSecond,baseThird,baseFourth,tempFirst,tempSecond,tempThird,tempFourth]

        deck = Class_Deck.deck()
        deck.createDeck()

        def leftMouseClickDown(deck,event):
            obj=event.GetEventObject()
            if(obj.stack.peekCard()):
                sourceX,sourceY = self.ScreenToClient(obj.GetPositionTuple())
                destX,destY = self.ScreenToClient(wx.GetMousePosition())
                obj._x,obj._y=(sourceX-destX,sourceY-destY)
                obj.deck=deck
                drag['drop']=obj
                if(debug):
                    print "Dragging tracking started"
            
        def mouseMovement(event):
            try:
                if 'drop' in drag:
                    obj=drag['drop']
                    x,y=wx.GetMousePosition()
                    if(debug):
                        try:
                            obj.ox
                            obj.oy
                        except:
                            obj.ox=0
                            obj.oy=0
                        print "Current Mouse Position - x: ",x,"(",x-obj.ox,") y:",y,"(",y-obj.oy,")"
                        obj.ox=x
                        obj.oy=y
                        drag['drop']=obj
                    #obj.SetPosition(wx.Point(x+obj._x,y+obj._y))
            except:
                pass

        def leftMouseClickUp(stack=None,event=None,number=None):
            try:
                if 'drop' in drag:
                    try:
                        obj=event.GetEventObject()
                        if(not number):
                            moveCard(drag['drop'],obj)
                        else:
                            try:
                                if ((obj.stack.peekCard().rank+number)%13==drag['drop'].stack.peekCard().rank):
                                    moveCard(drag['drop'],obj)
                            except:
                                pass
                    except:
                        pass
                    if(debug):
                        print "Dragging tracker released"
            except:
                if(debug):
                    print "Dragging tracker released"
            if(drag):
                del drag['drop']

        def moveCard(cardFrom,cardTo):
            tempCard=cardFrom.stack.returnTopCard()
            if(tempCard):
                cardTo.stack.addCard(tempCard)
            try:
                cardTo.SetBitmap(setCard(cardTo))
            except:
                pass
            try:
                cardFrom.SetBitmap(setCard(cardFrom,cardTo))
            except:
                pass
            testGameOver()

        def testGameOver():
            if(deck.stack.peekCard()==None and drawnCard.stack.peekCard()==None):
                if(testStack(tempFirst) or testStack(tempSecond) or testStack(tempThird) or testStack(tempFourth)):
                    pass
                else:
                    if(not len(tempFirst.stack.cardList) and not len(tempSecond.stack.cardList) and not len(tempThird.stack.cardList) and not len(tempFourth.stack.cardList)):
                        message=wx.MessageDialog(self,"Congratulations! You win!","Play Again", "Exit Game", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
                        result=message.ShowModal()
                        message.Destroy()
                        if(result==wx.ID_OK):
                            parent.setState(2)
                        if(result==wx.ID_CANCEL):
                            parent.setState(-1)
                    else:
                        message=wx.MessageDialog(self,"There are no more available moves.","Try Again", wx.OK|wx.CANCEL|wx.ICON_QUESTION)
                        result=message.ShowModal()
                        message.Destroy()
                        if(result==wx.ID_OK):
                            parent.setState(2)
                        if(result==wx.ID_CANCEL):
                            parent.setState(-1)

        def testStack(testStack):
            for x in xrange(0,len(testStack.stack.cardList)):
                tempCard=testStack.stack.peekCard().rank
                for x in xrange(0,len(tempFirst.stack.cardList)):
                    if((baseFirst.stack.peekCard().rank+1)%13==tempCard):
                        return True
                for x in xrange(0,len(tempSecond.stack.cardList)):
                    if((baseSecond.stack.peekCard().rank+2)%13==tempCard):
                        return True
                for x in xrange(0,len(tempThird.stack.cardList)):
                    if((baseThird.stack.peekCard().rank+3)%13==tempCard):
                        return True
                for x in xrange(0,len(tempFourth.stack.cardList)):
                    if((baseFourth.stack.peekCard().rank+4)%13==tempCard):
                        return True
                return False

        def setBase(baseNum,stack):
            while (deck.peekCard().rank!=baseNum):
                deck.cycleCard()
            moveCard(deck,stack)

        def setCard(stack,toStack=None):
            toStack=stack
            try:
                if(stack.stack.column!=None):
                    stackSize=len(stack.stack.cardList)
                    for x in xrange(0,stackSize):
                        try:
                            tempBitmap=stack.stack.bitmapList.pop(0)
                            tempBitmap.Destroy()
                        except:
                            pass

                    for x in xrange(0,stackSize):
                        stack.stack.cycleCard()
                        tempImage = wx.StaticBitmap(self,-1,wx.EmptyBitmap(75,100),(200+90*stack.stack.column,130+25*x),(75,100))
                        tempCardImage = wx.Image(stack.stack.peekCard().returnImg(), wx.BITMAP_TYPE_ANY).Scale(75,100,wx.IMAGE_QUALITY_NEAREST)
                        tempCardImage=tempCardImage.ConvertToBitmap()
                        tempImage.SetBitmap(tempCardImage)
                        stack.stack.bitmapList.append(tempImage)
                        tempImage.Bind(wx.EVT_LEFT_UP, leftMouseClickUp)
                        tempImage.Bind(wx.EVT_MOTION, mouseMovement)
                        toStack.SetPosition(wx.Point(200+90*stack.stack.column,130+25*x))
                        self.Refresh()

            except:
                pass
            try:
                tempImage=stack.stack.peekCard()
                if (debug):
                    print "Updating image: ",tempImage.returnName()
                tempImage=tempImage.returnImg()
                returnCardImage=wx.Image(tempImage,wx.BITMAP_TYPE_PNG).Scale(75,100,wx.IMAGE_QUALITY_NEAREST)
                returnCardImage=returnCardImage.ConvertToBitmap()
                return returnCardImage
            except:
                if (debug):
                    print "Stack empty, setting background colour. "
                returnCardImage = wx.Image("images\\background.png", wx.BITMAP_TYPE_PNG).Scale(75,100,wx.IMAGE_QUALITY_NEAREST)
                returnCardImage=returnCardImage.ConvertToBitmap()
                return returnCardImage

        self.SetBackgroundColour((12, 94, 1))

        drawnCard = wx.StaticBitmap(self,4,wx.EmptyBitmap(75,100),(100,10),(75,100))
        drawnCard.stack=Class_Card_Stack.cardStack()
        moveCard(deck,drawnCard)

        deckImage = wx.StaticBitmap(self,-1,wx.EmptyBitmap(75,100),(10,10),(75,100))
        tempDeckImage = wx.Image("images\\back.jpg", wx.BITMAP_TYPE_ANY).Scale(75,100,wx.IMAGE_QUALITY_NEAREST)
        tempDeckImage=tempDeckImage.ConvertToBitmap()
        deckImage.SetBitmap(tempDeckImage)
        deckImage.stack=Class_Card_Stack.cardStack()

        baseFirst = wx.StaticBitmap(self,0,wx.EmptyBitmap(75,100),(200,10),(75,100))
        baseFirst.stack=Class_Card_Stack.cardStack()
        setBase(0,baseFirst)

        baseSecond = wx.StaticBitmap(self,1,wx.EmptyBitmap(75,100),(290,10),(75,100))
        baseSecond.stack=Class_Card_Stack.cardStack()
        setBase(1,baseSecond)

        baseThird = wx.StaticBitmap(self,2,wx.EmptyBitmap(75,100),(380,10),(75,100))
        baseThird.stack=Class_Card_Stack.cardStack()
        setBase(2,baseThird)

        baseFourth = wx.StaticBitmap(self,3,wx.EmptyBitmap(75,100),(470,10),(75,100))
        baseFourth.stack=Class_Card_Stack.cardStack()
        setBase(3,baseFourth)

        tempFirst = wx.StaticBitmap(self,-1,wx.EmptyBitmap(75,100),(200,130),(75,100))
        tempFirst.stack=Class_Card_Stack.cardStack()
        tempFirst.SetBitmap(setCard(tempFirst))
        tempFirst.stack.stack=tempFirst.stack
        tempFirst.stack.cascade=True
        tempFirst.stack.column=0

        tempSecond = wx.StaticBitmap(self,-1,wx.EmptyBitmap(75,300),(290,130),(75,100))
        tempSecond.stack=Class_Card_Stack.cardStack()
        tempSecond.SetBitmap(setCard(tempSecond))
        tempSecond.stack.stack=tempSecond.stack
        tempSecond.stack.cascade=True
        tempSecond.stack.column=1

        tempThird = wx.StaticBitmap(self,-1,wx.EmptyBitmap(75,300),(380,130),(75,100))
        tempThird.stack=Class_Card_Stack.cardStack()
        tempThird.SetBitmap(setCard(tempThird))
        tempThird.stack.stack=tempThird.stack
        tempThird.stack.cascade=True
        tempThird.stack.column=2

        tempFourth = wx.StaticBitmap(self,-1,wx.EmptyBitmap(75,300),(470,130),(75,100))
        tempFourth.stack=Class_Card_Stack.cardStack()
        tempFourth.SetBitmap(setCard(tempFourth))
        tempFourth.stack.stack=tempFourth.stack
        tempFourth.stack.cascade=True
        tempFourth.stack.column=3

        
        deckImage.Bind(wx.EVT_LEFT_UP, leftMouseClickUp)
        drawnCard.Bind(wx.EVT_LEFT_UP, leftMouseClickUp)
        deckImage.Bind(wx.EVT_MOTION, mouseMovement)
        drawnCard.Bind(wx.EVT_MOTION, mouseMovement)
        deckImage.Bind(wx.EVT_LEFT_DOWN, lambda event: moveCard(deck,drawnCard))
        drawnCard.Bind(wx.EVT_LEFT_DOWN, lambda event: leftMouseClickDown(drawnCard,event=event))

        baseFirst.Bind(wx.EVT_MOTION, mouseMovement)
        baseSecond.Bind(wx.EVT_MOTION, mouseMovement)
        baseThird.Bind(wx.EVT_MOTION, mouseMovement)
        baseFourth.Bind(wx.EVT_MOTION, mouseMovement)
        baseFirst.Bind(wx.EVT_LEFT_UP, lambda event: leftMouseClickUp(baseFirst,event,1))
        baseSecond.Bind(wx.EVT_LEFT_UP, lambda event: leftMouseClickUp(baseSecond,event,2))
        baseThird.Bind(wx.EVT_LEFT_UP, lambda event: leftMouseClickUp(baseThird,event,3))
        baseFourth.Bind(wx.EVT_LEFT_UP, lambda event: leftMouseClickUp(baseFourth,event,4))

        tempFirst.Bind(wx.EVT_LEFT_DOWN, lambda event: leftMouseClickDown(tempFirst,event=event))
        tempSecond.Bind(wx.EVT_LEFT_DOWN, lambda event: leftMouseClickDown(tempSecond,event=event))
        tempThird.Bind(wx.EVT_LEFT_DOWN, lambda event: leftMouseClickDown(tempThird,event=event))
        tempFourth.Bind(wx.EVT_LEFT_DOWN, lambda event: leftMouseClickDown(tempFourth,event=event))
        tempFirst.Bind(wx.EVT_MOTION, mouseMovement)
        tempSecond.Bind(wx.EVT_MOTION, mouseMovement)
        tempThird.Bind(wx.EVT_MOTION, mouseMovement)
        tempFourth.Bind(wx.EVT_MOTION, mouseMovement)
        tempFirst.Bind(wx.EVT_LEFT_UP, lambda event: leftMouseClickUp(tempFirst,event))
        tempSecond.Bind(wx.EVT_LEFT_UP, lambda event: leftMouseClickUp(tempSecond,event))
        tempThird.Bind(wx.EVT_LEFT_UP, lambda event: leftMouseClickUp(tempThird,event))
        tempFourth.Bind(wx.EVT_LEFT_UP, lambda event: leftMouseClickUp(tempFourth,event))

        self.Bind(wx.EVT_MOTION, mouseMovement)
        self.Bind(wx.EVT_LEFT_UP, leftMouseClickUp)