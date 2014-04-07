import wx
import os
import Image
import Class_Frame

#slice("classic-playing-cards.png", os.getcwd()+"\\images", 4) 

app=wx.App(False)
frame=Class_Frame.frame()
frame.Show()
app.MainLoop()

    
def slice(image_path, outdir, slices):
    img=Image.open(image_path)
    wcolumnth,height=img.size
    slice_size=int(height/slices)
    upper=0
    left=0
    count=1
    for slice in range(slices):
        if (count==slices):
            lower=height
        else:
            lower=int(count*slice_size)   
        bbox=(left,upper,wcolumnth,lower)
        working_slice=img.crop(bbox)
        upper+=slice_size
        working_slice.save(os.path.join(outdir,Class_Card.suitToString(count-1)+".png"))
        dice(os.getcwd()+"\\images\\"+Class_Card.suitToString(count-1)+".png",Class_Card.suitToString(count-1),outdir,13)
        count+=1

def dice(image_path,name,outdir,dices):
    img=Image.open(image_path)
    wcolumnth,height=img.size
    upper=0
    left=0
    dice_size=int(wcolumnth/dices)
    count=1
    for dice in range(dices):
        upper=0
        left=(count-1)*dice_size
        if (count==dices):
            right=wcolumnth
        else:
            right=int(count*dice_size)   
        bbox=(left,upper,right,height)
        right+=dice_size
        working_dice=img.crop(bbox)
        working_dice.save(os.path.join(outdir,Class_Card.rankToString(count-1)+"_of_"+name+".png"))
        count+=1