import tkinter, random

canvas=tkinter.Canvas(width=400,height=200)
canvas.pack()

def napis():
    global napis
    napis=(entry1.get())
    x=0
    for i in range(len(napis)):
        x=x+20
        if i%2==0:
            canvas.create_text(100+x,50,text=napis[i],font='Arial 30',fill='blue')
        if i%2==1:
            canvas.create_text(100+x,80,text=napis[i],font='Arial 30',fill='blue')


button1=tkinter.Button(text='Ok',command=napis)
button1.pack()

entry1=tkinter.Entry()
entry1.pack()
