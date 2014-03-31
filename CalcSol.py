import wx

cheat = 0

def changeCheat(num):
    global cheat
    cheat = num

class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Calculation Solitaire', size=(600,500))
        self.swap = SwapPanels(self,
                               Panel1(self, -1),
                               Panel2(self, -1))
        
        self.timer = wx.FutureCall(2000, self.Swap)

    def Swap(self):
        global cheat
        if(cheat == 1):
            self.window_1 = self.swap.do()
            cheat = 0
        if(cheat == 2):
            self.Destroy()
        self.timer.Restart(20)
        

class SwapPanels:
    def __init__(self, frame, panel1, panel2):
        self.panel = panel2
        self.panel1 = panel1
        self.panel2 = panel2

        self.box = wx.BoxSizer(wx.VERTICAL)
        self.do()
        frame.SetSizer(self.box)

    def do(self):
        self.panel.Hide()
        self.box.Remove(self.panel)

        if self.panel == self.panel1:
            self.panel = self.panel2
        else:
            self.panel = self.panel1

        self.box.Add(self.panel, 1, wx.EXPAND, 0)
        self.panel.Show()

        self.box.Layout()

        return self.panel

class Panel1(wx.Panel):
    def __init__(self, *args, **kwds):
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        yesButton=wx.Button(self,label="Play Game!",pos=(200,200),size=(90,40))
        self.Bind(wx.EVT_BUTTON, self.moveToBoard, yesButton)
        exitButton=wx.Button(self,label="Exit Game",pos=(300,200),size=(90,40))
        self.Bind(wx.EVT_BUTTON, self.exitGame, exitButton)
        self.label=wx.StaticText(self, label="SWE4743 By Rhett, Hue, Adam, Brian.", pos=(150,150), size=(300,100))
        dragSource = wx.DropSource(self)
        dragSource.SetData(yesButton)
        result = dragSource.DoDragDrop(True)
        
    def moveToBoard(self,event):
        self.label.SetLabel("Starting Game...")
        global cheat
        cheat = 1
    
    def exitGame(self,event):
        global cheat
        cheat = 2

class Panel2(wx.Panel):
    def __init__(self, *args, **kwds):
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.SetBackgroundColour((12, 94, 1))
        imageFile = "king-hearts.png"
        image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY)
        image1 = image1.Scale(75, 100, wx.IMAGE_QUALITY_HIGH)
        image1 = image1.ConvertToBitmap()
        self.button1 = wx.BitmapButton(self, id=-1, bitmap=image1,
            pos=(210, 10))
            
        imageFile = "5S.png"
        image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY)
        image1 = image1.Scale(75, 100, wx.IMAGE_QUALITY_HIGH)
        image1 = image1.ConvertToBitmap()
        
        self.button3 = wx.BitmapButton(self, id=-1, bitmap=image1,
            pos=(305, 10))
        imageFile = "AS.jpg"
        image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY)
        image1 = image1.Scale(75, 100, wx.IMAGE_QUALITY_HIGH)
        image1 = image1.ConvertToBitmap()
        self.button4 = wx.BitmapButton(self, id=-1, bitmap=image1,
            pos=(400, 10))
        imageFile = "KD.png"
        image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY)
        image1 = image1.Scale(75, 100, wx.IMAGE_QUALITY_HIGH)
        image1 = image1.ConvertToBitmap()
        self.button5 = wx.BitmapButton(self, id=-1, bitmap=image1,
            pos=(495, 10))
		
        imageFile = "back.jpg"
        image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY)
        image1 = image1.Scale(75, 100, wx.IMAGE_QUALITY_HIGH)
        image1 = image1.ConvertToBitmap()
        self.button2 = wx.BitmapButton(self, id=-1, bitmap=image1,
            pos=(10, 10))
        self.button2.Bind(wx.EVT_BUTTON, self.imgClk)
    
    def imgClk(self,event):
        imageFile = "JS.png"
        image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY)
        image1 = image1.Scale(75, 100, wx.IMAGE_QUALITY_HIGH)
        image1 = image1.ConvertToBitmap()
        self.deckButton = wx.BitmapButton(self, id=-1, bitmap=image1,
            pos=(105, 10))


app=wx.PySimpleApp()
f=MyFrame(None, -1)
f.Show()
app.MainLoop()
