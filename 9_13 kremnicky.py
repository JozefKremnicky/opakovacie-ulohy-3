import tkinter, random

canvas=tkinter.Canvas(width=400,height=200)
canvas.pack()
farba=random.choice(['green','yellow','blue'])
def napis():
    global napis
    napis=(entry1.get())
    x=0
    for i in range(len(napis)):
        x=x+20
        canvas.create_text(100+x,50,text=napis[i],font='Arial 30',fill=farba)
button1=tkinter.Button(text='Ok',command=napis)
button1.pack()

entry1=tkinter.Entry()
entry1.pack()


        
    
