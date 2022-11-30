# from tkinter import messagebox
from tkinter import *

tk = Tk()

canvas = Canvas(tk, width=600, height=600, highlightthickness=0)
canvas.pack()

btn1_1 = PhotoImage(file='Кнопка синяя.png')
btn1_1 = btn1_1.subsample(6, 6)
id_img1 = canvas.create_image(120, 100, anchor='nw', image=btn1_1)

tk.mainloop()