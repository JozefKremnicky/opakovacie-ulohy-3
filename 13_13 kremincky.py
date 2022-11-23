import tkinter
canvas=tkinter.Canvas(width=300,height=300)
canvas.pack()

def slovo():
    global slovo
    slovo=(entry1.get())
    x=0
    y=0
    for i in range(len(slovo)):
        x=x+25
        y=y+30
        canvas.create_text(100+x,50+y,text=slovo[i],font='Arial 35')



button1=tkinter.Button(text='ok',command=slovo)
button1.pack()

entry1=tkinter.Entry()
entry1.pack()
