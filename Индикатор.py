import time
from tkinter import *


def activ_or_deactiv():
    if button['text'] == 'on':
        button['text'] = 'off'
        while button['text'] == 'off':
            c.itemconfig(indicate, fill='red')
            c.update()
            time.sleep(0.5)
            c.itemconfig(indicate, fill='blue')
            c.update()
            time.sleep(0.5)
    else:
        button['text'] = 'on'
        c.itemconfig(indicate, fill='blue')

windows = Tk()
c = Canvas(windows, width=500, height=500, bg='grey')
c.pack()
indicate = c.create_rectangle(250, 250, 320, 270, fill='blue')
button = Button(c, text='on', command=activ_or_deactiv)
button.place(x=250, y=280)
windows.mainloop()