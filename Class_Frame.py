import wx
import time
import Screen_Game
import Screen_Welcome
import Class_Deck
from Helper_Globals import debug

class frame(wx.Frame):
    state=1
    if(debug):
        state=1
    def __init__(self):
        wx.Frame.__init__(self, None, style=(wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER),title='Calculation Solitaire', size=(595,485))
        menuBar=wx.MenuBar()
        menu=wx.Menu()
        exitMenu=menu.Append(wx.ID_EXIT,"E&xit\tAlt-X", "Exits Calculation Solitaire.")
        self.Bind(wx.EVT_MENU,lambda event: self.setState(-1),exitMenu)
        menuBar.Append(menu,"&File")
        menu=wx.Menu()
        newGame=menu.Append(wx.ID_ANY,"&New Game\tAlt-N", "Starts a new game.")
        self.Bind(wx.EVT_MENU,lambda event: self.setState(2),newGame)
        menuBar.Append(menu,"&New Game")
        self.SetMenuBar(menuBar)
        sizer = wx.BoxSizer(wx.VERTICAL)

        def navigate():
            if(self.state == -1):
                self.Destroy()
            if(self.state != 0):
                try:
                    if self.screen_welcome.Shown:
                        self.old=self.screen_welcome
                except:
                    pass
                try:
                    if self.screen_game.Shown:
                        self.old=self.screen_game
                except:
                    pass
                if (self.state == 1):
                    self.screen_welcome=Screen_Welcome.welcomeScreen(self)
                    sizer.Add(self.screen_welcome,1,wx.EXPAND)
                if (self.state == 2):
                    self.screen_game=Screen_Game.gameScreen(self)
                    sizer.Add(self.screen_game,1,wx.EXPAND)
                try:
                    self.old.Destroy()
                except:
                    pass
                self.state=0
                self.SetSizer(sizer)
                self.Layout()
            self.timer.Restart(20)

        self.timer = wx.FutureCall(20,navigate)



    def setState(self,i):
        self.state=i

    def returnDeck():
        return self.deck
