import wx 
class Frame1(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'Frame1',size=(400,300))      
        Panel1(self)
 
class Panel1(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent,-1,pos=(00,0),size=(200,300))
        button = wx.Button(self, -1, '打开第二个Frame', (50, 50))
        button.Bind(wx.EVT_BUTTON,self.OnClick)
       
        self.tc = wx.TextCtrl(self, -1, pos=(50, 100))
        
    def OnClick(self,evt):
    	a=self.tc.GetValue()
    	Panel2(self).tc2.SetValue(a)
    	print(a)
       
class Panel2(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent,-1,pos=(200,0),size=(200,300))
        self.tc2 = wx.TextCtrl(self, -1,"iu", pos=(50, 100),style=wx.TE_READONLY)
        # button = wx.Button(self,-1,'打开第二个Frame',(50,50))
    #     self.b=0
    #     button.Bind(wx.EVT_BUTTON,self.kl)

    # def kl(self,e):
    # 	c=self.tc2.GetValue()
    # 	self.b=int(c)+self.b
    # 	print(a,self.b)

        
       

if __name__=='__main__':
    app = wx.App()
    frame = Frame1()
    frame.Show()
    app.MainLoop()
