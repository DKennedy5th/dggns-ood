import Helper_Globals
import Class_Deck

class images(self,parent,x,y):
    def __init__(self,x,y):
        self.img=wx.StaticBitmap(self, -1,size=(75,100),pos=(x,y))
        self.img=wx.Image(selfParent.deck.returnTopCard().img,wx.BITMAP_TYPE_PNG)
        self.img=self.image.Scale(75,100,wx.IMAGE_QUALITY_HIGH)
        self.img=self.img.ConvertToBitmap()
        self.drawnCard.SetBitmap(self.img)
        selfParent.Refresh()

        '''
        imageFile = d.returnTopCard().returnImg()
        image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY)
        image1 = image1.Scale(75, 100, wx.IMAGE_QUALITY_HIGH)
        image1 = image1.ConvertToBitmap()
        self.deckButton = wx.BitmapButton(self, column=-1, bitmap=image1, pos=(105, 10))
        '''

    def imageClick(self,event):
        global d
        imageFile = d.returnTopCard().returnImg()
        image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY)
        image1 = image1.Scale(75, 100, wx.IMAGE_QUALITY_HIGH)
        image1 = image1.ConvertToBitmap()
        self.deckButton = wx.BitmapButton(self, column=-1, bitmap=image1,
            pos=(105, 10))