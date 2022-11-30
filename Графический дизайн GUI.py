import tkinter as tk    # Графическая библиотека

# Настройка окна:
windows = tk.Tk()   # Создаем переменную и заносим в нее через модуль tk и вызываем у него класс Tk()

photo = tk.PhotoImage(file='photo_png.png')    # Создаем иконку на окне через класс PhotoImage. Формат строго png
windows.iconphoto(False, photo)    # Закрепляем иконку к окну через метод icon photo

windows.config(bg='#CCFFFF')    # Создаем цвет фона окна через метод config со свойством background

windows.title('STEEL RAT game')    # Таким образом мы меняем заголовок окна mainloop с tk на другое

windows.geometry('965x500+325+60')   # Задаем размер и положение окна на экране, 965(длина)x500(ширина)
# +325(положение от левого угла в право)+60(положение от левого угла вниз)
windows.minsize(900, 400)    # Можно задать максимальную и минимальную регулировку окна
windows.maxsize(1000, 600)
windows.resizable(True, True)    # Фиксация размеров окна, по умолчанию длина и ширина True(меняется)


# Кнопки:
# метод Label()
label_1 = tk.Label(windows, text='''Ваш 
выбор:''',
                   bg='#FFFFFF',
                   fg='#66B2FF',
                   font=('Arial', 14, 'bold'),
                   # padx=10, pady=0,
                   width=15, height=0,
                   anchor='w',
                   relief=tk.RAISED, bd=4,
                   justify=tk.LEFT)    # Создаем лейбл для окна с помощью класса Label(свойства),
# text - текст, bg - фон, fg - цвет текста, font - шрифт label, pad x - отступ внутри от текста, width и height -
# отступ ведущийся в знаках, anchor - положение текста по сторонам света на англ., relief - контур lable, bd - ширина
# контура, justify - выравнивание текста относительно данного положения
# label_1.pack()    # Закрепим лейбл в окне

# метод grid()
btn1 = tk.Button(windows, text='номер 1')   # Создаем лейбл для окна с помощью класса Button(свойства)
btn2 = tk.Button(windows, text='номер 2')
btn3 = tk.Button(windows, text='номер 3')
btn4 = tk.Button(windows, text='номер 4 больше остальных')
btn5 = tk.Button(windows, text='номер 5')
btn6 = tk.Button(windows, text='номер 6')


btn1.grid(row=0, column=0)    # Закрепим лейбл в окне методом grid(), где row - ряд, column - колонка
btn2.grid(row=0, column=1, sticky='e')    # с помощью sticky выравниваем кнопку в нужную сторону
btn3.grid(row=1, column=0)
btn4.grid(row=1, column=1)
btn5.grid(row=2, column=0, columnspan=2, sticky='we')    # column span - ставит кнопку между колонок, sticky - со
# сторонами света, растягивает кнопку, но только на ширину колонок с кнопками
btn6.grid(row=0, column=2, rowspan=3, sticky='sn')    # row span - ставит кнопку между колонок строк, sticky - со
# сторонами света, растягивает кнопку, но только на ширину строк с кнопками

windows.grid_columnconfigure(0, minsize=200)    # можно задать минимальное значение столбика, где 0 номер столба

windows.mainloop()    # Подключаем главное меню которое дает нам пустое окно
