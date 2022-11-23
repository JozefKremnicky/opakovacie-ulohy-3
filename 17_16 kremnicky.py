import tkinter, random
canvas=tkinter.Canvas(width=300,height=300)
canvas.pack()
def mail():
    global mail
    mail=(entry1.get())
    for i in range (len(mail)):
        canvas.create_text(70,150,text=(mail[-4:]))
        canvas.create_text(155,130,text=(mail[-3:]))
        if mail[i] =='@':
            canvas.create_text(100,70,text=mail[i:])
        if mail[i] =='@':
            canvas.create_text(100,90,text=mail[:i])
        if mail[i] =='@' and '.':
            canvas.create_text(155,150,text=mail[i:'.'])
canvas.create_text(35,50,text='TLD:')
canvas.create_text(40,70,text='Server:')            
canvas.create_text(37,90,text='User:')
canvas.create_text(47,110,text='Domeny:')
canvas.create_text(80,130,text='Domena 1. urovne je:')
canvas.create_text(80,150,text='Domena 2. urovne je:')
canvas.create_text(80,170,text='Domena 3. urovne je:')

button1=tkinter.Button(text='potvrd',command=mail)
button1.pack()
entry1=tkinter.Entry()
entry1.pack()
