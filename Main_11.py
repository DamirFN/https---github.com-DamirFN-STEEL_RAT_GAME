from tkinter import *
from tkinter import messagebox
from time import sleep
from v1.library_1v import library_1
from tkinter.scrolledtext import ScrolledText

def on_closing():
    global app_running
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        app_running = False

tk = Tk()
app_running = True
tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("steel_rat")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
tk.iconbitmap("resources/photo.ico")

w = 1147
h = 705

sc = Canvas(tk, width=w, height=h,
                bg="#CCFFFF",
                highlightthickness=0)
sc.pack()

our_image = PhotoImage(file='6122245.png')
sc.create_image(-27, -277.5, anchor=NW, image=our_image)

text = ScrolledText(sc, width=126, height=30)
text.insert("1.0", "")
text.place(x=59, y=52, anchor=NW)

def start():
    t = input('введите: ')
    e = open(library_1[t], 'r', -1, 'utf-8')
    for LINE in e:
        print(LINE, end='')
        sleep(0.5)
    e.close()
    sleep(1)
    print('\n')

    s = []
    e0 = open(library_1[t], 'r', -1, 'utf-8')
    r = e0.readlines()
    r1 = ', '.join(r).split(' ')
    for r1 in r1:
        if r1 in library_1:
            s.append(r1)

    if len(s) == 1:
        print(f'Жмите: {s[0]}')
    elif len(s) == 2:
        print(f'Ваш выбор: {s[0]} или {s[1]}')
    elif len(s) == 3:
        print(f'Ваш выбор: {s[0]}, {s[1]} или {s[2]}')
    elif len(s) == 4:
        print(f'Ваш выбор: {s[0]}, {s[1]}, {s[2]} или {s[3]}')

    e0.close()

# def game():
#     print('Здравствуй дорогой читатель. По всей видимости ты любитель книг и в душе исследователь всего неведанного и '
#           'странного. Эта книга или точнее сказать Книга - игра, изобилует и тем и другим. Не буду раскрывать '
#           'всех ее тайн и предлагаю уже перейти к книге самому и убедиться в этом. Могу еще добавить одно ПРИЯТНОЙ '
#           'ИГРЫ БУДУЩИЙ КУРСАНТ И ЖМИ на клаве 400!')

label_1 = Label(tk, text='СКОРЕЙ ВЫБИРАЙ!', bg='#FF0000', padx=15, pady=6, relief='ridge', bd=5, font=('Arial', 14, 'bold'),
                anchor='n', justify=LEFT)  # Создаем лейбл для окна с помощью класса Label(свойства),
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

btn6_6 = PhotoImage(file='Кнопка серая.png')
btn6_6 = btn6_6.subsample(7, 10)

Button(sc, image=btn1_1, highlightthickness=0, bg='#000000', activebackground='#000000', bd=0,
       fg='#66B2FF', activeforeground='#66B2FF', font='Arial 8 bold',
       compound=BOTTOM, text='номер 1').place(x=278, y=645)

Button(sc, image=btn2_2, highlightthickness=0, bg='#000000', activebackground='#000000', bd=0,
       fg='#66B2FF', activeforeground='#66B2FF', font='Arial 8 bold',
       compound=BOTTOM, text='номер 2').place(x=398, y=645)

Button(sc, image=btn3_3, highlightthickness=0, bg='#000000', activebackground='#000000', bd=0,
       fg='#66B2FF', activeforeground='#66B2FF', font='Arial 8 bold',
       compound=BOTTOM, text='номер 3').place(x=518, y=645)

Button(sc, image=btn4_4, highlightthickness=0, bg='#000000', activebackground='#000000', bd=0,
       fg='#66B2FF', activeforeground='#66B2FF', font='Arial 8 bold',
       compound=BOTTOM, text='номер 4').place(x=638, y=645)

Button(sc, image=btn5_5, highlightthickness=0, bg='#000000', activebackground='#000000', bd=0,
       fg='#66B2FF', activeforeground='#66B2FF', font='Arial 8 bold',
       compound=BOTTOM, text='номер 5').place(x=758, y=645)

Button(sc, image=btn5_5, highlightthickness=0, bg='#000000', activebackground='#000000', bd=0,
       fg='#66B2FF', activeforeground='#66B2FF', font='Arial 8 bold',
       compound=BOTTOM, text='Start').place(x=878, y=645)

while app_running:
    if app_running:
        # t = input('введите: ')
        # e = open(library_1[t], 'r', -1, 'utf-8')
        # for LINE in e:
        #     print(LINE, end='')
        #     sleep(0.5)
        # e.close()
        # sleep(1)
        # print('\n')
        #
        # s = []
        # e0 = open(library_1[t], 'r', -1, 'utf-8')
        # r = e0.readlines()
        # r1 = ', '.join(r).split(' ')
        # for r1 in r1:
        #     if r1 in library_1:
        #         s.append(r1)
        #
        # if len(s) == 1:
        #     print(f'Жмите: {s[0]}')
        # elif len(s) == 2:
        #     print(f'Ваш выбор: {s[0]} или {s[1]}')
        # elif len(s) == 3:
        #     print(f'Ваш выбор: {s[0]}, {s[1]} или {s[2]}')
        # elif len(s) == 4:
        #     print(f'Ваш выбор: {s[0]}, {s[1]}, {s[2]} или {s[3]}')
        #
        # e0.close()
        # start()
        tk.update_idletasks()
        tk.update()
# game()
    sleep(0.005)
tk.destroy()
# tk.mainloop()