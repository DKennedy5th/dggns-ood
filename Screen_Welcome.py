import wx
import Class_Card
import random
from Helper_Globals import debug

class welcomeScreen(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        def screenGame(self):
            parent.setState(2)
            if(debug):
                print "Switching state to 2 (Playing)"

        def leftMouseClick(event):
            obj=event.GetEventObject()
            tempImage = wx.Image("images\\"+Class_Card.rankToString(int(random.random()*13))+"_of_"+Class_Card.suitToString(int(random.random()*4))+".png", wx.BITMAP_TYPE_PNG).Scale(75,100,wx.IMAGE_QUALITY_NEAREST)
            tempImage=tempImage.ConvertToBitmap()
            obj.SetBitmap(tempImage)


        setBackground=wx.Image("images\\Solitairebackground.png",wx.BITMAP_TYPE_PNG).Scale(590,440,wx.IMAGE_QUALITY_NEAREST)
        setBackground=setBackground.ConvertToBitmap()
        self.background=wx.StaticBitmap(self,-1,setBackground,(0,0))

        yesButton=wx.Button(self.background,label="Play Calculation Solitaire!",pos=(225,200),size=(150,50))
        self.Bind(wx.EVT_BUTTON, screenGame, yesButton)
        if(debug):
            label=wx.StaticText(self.background, label="Codename: \"Good Question\" Dbg On", pos=(198,150), size=(200,20))
        else:
            label=wx.StaticText(self.background, label="SWE4743 By Rhett, Hue, Brian, Adam.", pos=(198,150), size=(200,20))

        tempFirst = wx.StaticBitmap(self.background,-1,wx.EmptyBitmap(75,100),(75,250),(75,100))
        tempDeckImage = wx.Image("images\\back.jpg", wx.BITMAP_TYPE_ANY).Scale(75,100,wx.IMAGE_QUALITY_NEAREST)
        tempDeckImage=tempDeckImage.ConvertToBitmap()
        tempFirst.SetBitmap(tempDeckImage)
        tempFirst.Bind(wx.EVT_LEFT_DOWN,leftMouseClick)

        tempSecond = wx.StaticBitmap(self.background,-1,wx.EmptyBitmap(75,100),(265,290),(75,100))
        tempDeckImage = wx.Image("images\\back.jpg", wx.BITMAP_TYPE_ANY).Scale(75,100,wx.IMAGE_QUALITY_NEAREST)
        tempDeckImage=tempDeckImage.ConvertToBitmap()
        tempSecond.SetBitmap(tempDeckImage)
        tempSecond.Bind(wx.EVT_LEFT_DOWN,leftMouseClick)

        tempThird = wx.StaticBitmap(self.background,-1,wx.EmptyBitmap(75,100),(445,250),(75,100))
        tempDeckImage = wx.Image("images\\back.jpg", wx.BITMAP_TYPE_ANY).Scale(75,100,wx.IMAGE_QUALITY_NEAREST)
        tempDeckImage=tempDeckImage.ConvertToBitmap()
        tempThird.SetBitmap(tempDeckImage)
        tempThird.Bind(wx.EVT_LEFT_DOWN,leftMouseClick)

        self.Layout()


            
