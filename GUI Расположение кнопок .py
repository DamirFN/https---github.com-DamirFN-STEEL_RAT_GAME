from tkinter import messagebox
from tkinter import *
import tkinter as tk

def on_closing():  # Создаем функцию закрытия приложения
    if messagebox.askokcancel('Выход из игры', 'Хотите выйти из STEEL RAT?'):
        windows.destroy()  # Разрушаем наше приложение

# Настройка окна:
windows = Tk()  # Создаем переменную и заносим в нее через модуль tk и вызываем у него класс Tk()

windows.protocol("WM_DELETE_WINDOW", on_closing)  # Протокол закрытия с параметром WM_DELETE_WINDOW
windows.wm_attributes('-topmost', 1)  # Расположение окошка "Закрытия приложения" на передний план

photo = PhotoImage(file='photo.png')  # Создаем иконку на окне через класс PhotoImage. Формат строго png
windows.iconphoto(False, photo)  # Закрепляем иконку к окну через метод icon photo

# windows.config(bg='#CCFFFF')    # Создаем цвет фона окна через метод config со свойством background

windows.title('STEEL RAT game')  # Таким образом мы меняем заголовок окна mainloop с tk на другое

windows.geometry('1147x705+325+60')  # Задаем размер и положение окна на экране, 965(длина)x500(ширина)
# +325(положение от левого угла в право)+60(положение от левого угла вниз)
windows.minsize(900, 400)  # Можно задать максимальную и минимальную регулировку окна
windows.maxsize(1147, 800)
windows.resizable(True, True)  # Фиксация размеров окна, по умолчанию длина и ширина True(меняется)

# Фоновая картинка:
our_image = PhotoImage(file='6122245.png')  # задействуем нашу фоновую картинку
# our_image = our_image.subsample(3, 3)    # Регулировка размера картинки
our_label = Label(windows, bg='#CCFFFF')
our_label.image = our_image
our_label['image'] = our_label.image
our_label.place(x=-28, y=-277.5)

# Кнопки:
# метод Label()
label_1 = Label(windows, text='СКОРЕЙ ВЫБИРАЙ!',
                bg='#FF0000',
                padx=20, pady=6,
                relief=tk.RAISED, bd=5,
                font=('Arial', 14, 'bold'),
                anchor='n',
                justify=LEFT)  # Создаем лейбл для окна с помощью класса Label(свойства),
# text - текст, bg - фон, fg - цвет текста, font - шрифт label, pad x - отступ внутри от текста, width и height -
# отступ ведущийся в знаках, anchor - положение текста по сторонам света на англ., relief - контур lable, bd - ширина
# контура, justify - выравнивание текста относительно данного положения(RIGHT, LEFT)
label_1.place(x=39, y=647)  # Закрепим лейбл в окне

# метод ()
# Кнопки с картинками:
btn1_1 = PhotoImage(file='Кнопка синяя.png')
btn1_1 = btn1_1.subsample(7, 10)

btn2_2 = PhotoImage(file='Кнопка салатовая.png')
btn2_2 = btn2_2.subsample(7, 10)

btn3_3 = PhotoImage(file='Кнопка зеленая.png')
btn3_3 = btn3_3.subsample(7, 10)

btn4_4 = PhotoImage(file='Кнопка коричневая.png')
btn4_4 = btn4_4.subsample(7, 10)

btn5_5 = PhotoImage(file='Кнопка серая.png')
btn5_5 = btn5_5.subsample(7, 10)

Button(windows, image=btn1_1, highlightthickness=0, bg='#000000', activebackground='#000000', bd=0,
       fg='#66B2FF', activeforeground='#66B2FF', font='Arial 8 bold',
       compound=BOTTOM, text='номер 1').place(x=278, y=645)

Button(windows, image=btn2_2, highlightthickness=0, bg='#000000', activebackground='#000000', bd=0,
       fg='#66B2FF', activeforeground='#66B2FF', font='Arial 8 bold',
       compound=BOTTOM, text='номер 2').place(x=398, y=645)

Button(windows, image=btn3_3, highlightthickness=0, bg='#000000', activebackground='#000000', bd=0,
       fg='#66B2FF', activeforeground='#66B2FF', font='Arial 8 bold',
       compound=BOTTOM, text='номер 3').place(x=518, y=645)

Button(windows, image=btn4_4, highlightthickness=0, bg='#000000', activebackground='#000000', bd=0,
       fg='#66B2FF', activeforeground='#66B2FF', font='Arial 8 bold',
       compound=BOTTOM, text='номер 4').place(x=638, y=645)

Button(windows, image=btn5_5, highlightthickness=0, bg='#000000', activebackground='#000000', bd=0,
       fg='#66B2FF', activeforeground='#66B2FF', font='Arial 8 bold',
       compound=BOTTOM, text='номер 5').place(x=758, y=645)

windows.mainloop()  # Подключаем главное меню которое дает нам пустое окно
