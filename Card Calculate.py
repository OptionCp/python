from tkinter import *

root = Tk()
root.wm_attributes('-topmost',1)
root.geometry("210x340")
root.title("秋卡合成金币")
FrameRoot = Frame(root)
LeftFrame = Frame(FrameRoot)
RightFrame = Frame(FrameRoot)

CardNum = StringVar()
lable1 = Label(RightFrame, text = "秋卡数量：")
lable1.pack()
en1 = Entry(RightFrame, textvariable = CardNum)
en1.pack()
lable1 = Label(RightFrame, text = "VIP1~3：")
lable1.pack()
GoldNumV3 = StringVar()
en2 = Entry(RightFrame, textvariable = GoldNumV3)
en2.pack()
lable1 = Label(RightFrame, text = "VIP4：")
lable1.pack()
GoldNumV4 = StringVar()
en2 = Entry(RightFrame, textvariable = GoldNumV4)
en2.pack()
lable1 = Label(RightFrame, text = "VIP5：")
lable1.pack()
GoldNumV5 = StringVar()
en2 = Entry(RightFrame, textvariable = GoldNumV5)
en2.pack()
lable1 = Label(RightFrame, text = "VIP6：")
lable1.pack()
GoldNumV6 = StringVar()
en2 = Entry(RightFrame, textvariable = GoldNumV6)
en2.pack()
lable1 = Label(RightFrame, text = "VIP7：")
lable1.pack()
GoldNumV7 = StringVar()
en2 = Entry(RightFrame, textvariable = GoldNumV7)
en2.pack()



RightFrame.pack()
FrameRoot.pack()


def Sum1():
    res = CardNum.get()
    res = int(res)
    if res < 1000:
        res = res * 10
        GoldNumV3.set(str(res))
        GoldNumV4.set(str(res))
        GoldNumV5.set(str(res))
        GoldNumV6.set(str(res))
        GoldNumV7.set(str(res))
    else:
        resRem = res%1000*10
        resInt = res//1000      
        GoldNumV3.set(str(resRem + resInt*12000))
        GoldNumV4.set(str(resRem + resInt*12240))
        GoldNumV5.set(str(resRem + resInt*12360))
        GoldNumV6.set(str(resRem + resInt*12480))
        GoldNumV7.set(str(resRem + resInt*12600))

def Sum(self):
    res = CardNum.get()
    res = int(res)
    if res < 1000:
        res = res * 10
        GoldNumV3.set(str(res))
        GoldNumV4.set(str(res))
        GoldNumV5.set(str(res))
        GoldNumV6.set(str(res))
        GoldNumV7.set(str(res))
    else:
        resRem = res%1000*10
        resInt = res//1000      
        GoldNumV3.set(str(resRem + resInt*12000))
        GoldNumV4.set(str(resRem + resInt*12240))
        GoldNumV5.set(str(resRem + resInt*12360))
        GoldNumV6.set(str(resRem + resInt*12480))
        GoldNumV7.set(str(resRem + resInt*12600))
    
resb = Button(root, text = "get", command = Sum1)
resb.pack()
en1.bind("<Return>", Sum)


root.mainloop()
