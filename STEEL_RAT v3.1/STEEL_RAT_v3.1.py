from tkinter import *
from tkinter import messagebox as mb   # для меню 
from time import sleep
from v1.library_1v import library_1
from tkinter.scrolledtext import ScrolledText    # многострочное текстовое окно с прокруткой
from tkinter import filedialog as fd    # настройка для активации настроек меню

def on_closing():
    global app_running
    if mb.askokcancel("Выход из игры", "Вы действительно хотите покинуть игру?"):
        app_running = False

tk = Tk()
app_running = True
tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("STEEL RAT")
tk.resizable(False, False)
tk.wm_attributes("-topmost", 1)
tk.iconbitmap("photo.ico")

sc = Canvas(tk, width=1147, height=705, bg="blue", highlightthickness=0)    
sc.pack()

indicate = sc.create_rectangle(30, 15, 1120, 610, fill='blue')

our_image = PhotoImage(file='6122245.png')
sc.create_image(-27, -277.5, anchor=NW, image=our_image)

text = ScrolledText(sc, width=90, height=14, bg='#CCFFFF', fg='green', font=('Arial', 14, 'bold'), relief=SUNKEN,
                    bd=8, padx=10, pady=8, wrap=WORD, spacing1=10, spacing2=20, state=NORMAL)    # state=DISABLED
                    
text.insert("1.0", "")
text.place(x=59, y=52, anchor=NW)

#text.configure(state=NORMAL)

e = 'Здравствуй дорогой читатель. По всей видимости ты любитель книг и в душе исследователь всего'\
    'неведанного и странного. Эта книга или точнее сказать Книга - игра, изобилует и тем и другим. '\
    'Не буду раскрывать всех ее тайн и предлагаю уже перейти к ней самому и убедиться в этом. Могу '\
    'еще добавить одно набери в маленьком окошке лептопа число 400 и нажмите на кнопку "ДАЛЕЕ".                     ' \
    '           !                                                             ПРИЯТНОЙ ИГРЫ БУДУЩИЙ КУРСАНТ!                                                             !' 

text.insert(1.0, e)

text_2 = Entry(sc, width=27, bg='#FFD700', fg='green', font=('Arial', 14, 'bold'), relief=SUNKEN,
              bd=8)              
text_2.place(x=60, y=547)

text_3 = Entry(sc, width=5, bg='#CCFFFF', fg='green', font=('Arial', 14, 'bold'), relief=SUNKEN,
              bd=8)
text_3.place(x=740, y=647)

def activ_or_deactiv():   
    if text_2:
        p = 0
        while p < 3:           
            sc.itemconfig(indicate, fill='#FFD700')
            sc.update()
            Label_1_red()
            sleep(1)
            sc.itemconfig(indicate, fill='blue')
            sc.update()
            Label_1_black()
            sleep(1)
            p += 1            
            sc.update()
        Label_1()    
    else:
        sc.itemconfig(indicate, fill='blue')
        sc.update()

def start():
    #text.configure(state=NORMAL)   
    text.delete(1.0, END)   
    v = text_3.get()
    e = open(library_1[v], 'r', -1, 'utf-8')
    stuff = e.read()

    text.insert(END, stuff)
    e.close()
    text_3.delete(0, END)
    varible(v)

def varible(v):
    text_2.delete(0, END)
    s = []
    e0 = open(library_1[v], 'r', -1, 'utf-8')
    r = e0.readlines()
    r1 = ', '.join(r).split(' ')
    for r1 in r1:
        if r1 in library_1:
            s.append(r1)

    if len(s) == 1:
        text_2.config(justify=CENTER)
        text_2.insert(END, 'жми ')
        text_2.insert(END, s[0])
        text_2.insert(END, ' и далее')
        activ_or_deactiv()
        
    elif len(s) == 2:
        text_2.config(justify=CENTER, fg='red')
        text_2.insert(END, s[0])
        text_2.insert(END, ' или ')
        text_2.insert(END, s[1])
        text_2.insert(END, ' выбирай!')
        activ_or_deactiv()
    elif len(s) == 3:
        text_2.config(justify=CENTER, fg='red')
        text_2.insert(END, s[0])
        text_2.insert(END, ', ')
        text_2.insert(END, s[1])
        text_2.insert(END, ' или ')
        text_2.insert(END, s[2])
        text_2.insert(END, ' выбирай!')
        activ_or_deactiv()

    elif len(s) == 4:
        text_2.config(justify=CENTER, fg='red')
        text_2.insert(END, s[0])
        text_2.insert(END, ' ')
        text_2.insert(END, s[1])
        text_2.insert(END, ' ')
        text_2.insert(END, s[2])
        text_2.insert(END, ' ')
        text_2.insert(END, s[3])
        text_2.insert(END, ' выбирай!')
        activ_or_deactiv()

    elif len(s) == 5:
        text_2.config(justify=CENTER, fg='red')
        text_2.insert(END, s[0])
        text_2.insert(END, ', ')
        text_2.insert(END, s[1])
        text_2.insert(END, ', ')
        text_2.insert(END, s[2])
        text_2.insert(END, ', ')
        text_2.insert(END, s[3])
        text_2.insert(END, ', ')
        text_2.insert(END, s[4])
        text_2.insert(END, ' подумай')
        activ_or_deactiv()

    e0.close()

def save_game():
    name_file = fd.asksaveasfilename(initialdir=r'\SAVE', defaultextension="txt", filetypes=(("TEXT_file", "*.txt"), 
    ("ALL", "*.*")))
    if name_file:
        with open(name_file, 'w', -1, 'utf-8') as f:
            sv = text.get(1.0, END)
            f.write(sv)

def load_game():
    wanted_files = ((("TEXT_file", "*.txt"), ("ALL", "*.*")))

    file_name = fd.askopenfilename(initialdir=r'/SAVE', title='Загрузить сохранение', filetypes=wanted_files)
    text.insert(END, file_name)
    if file_name:
        with open(file_name, 'r', -1, 'utf-8') as f:
            text.delete(1.0, END) 
            text.insert(END, f.read())
              
def help():
    label_help = Tk()
    label_help.title('Правила игры')
    label_help.wm_attributes("-topmost", 1)
    label_help.iconbitmap("resources/photo.ico")

    label_help.resizable(False, False)
    lh = Canvas(label_help, width=1147, height=705, bg="blue", highlightthickness=0)
    lh.pack()   
    text_help = Text(lh, width=90, height=14, bg='#CCFFFF', fg='green', font=('Arial', 14, 'bold'), relief=SUNKEN,
                    bd=8, padx=10, pady=8, wrap=WORD, spacing1=10, spacing2=20, state=NORMAL)    # state=DISABLED
    text_help.pack() 
    text_help.insert("1.0", "")

    e_help = '1. Для игры вам нужна мышка и клавиатура.                                                                                                 \
              2. Колесиком мыши вы можете прокручиваь основной текст игры.                                                      \
              3. Окно желтого цвета для вашего удобства предлагает варианты ответов.                                      \
              4. Маленькое окошко предназначено для ввода одного из предложенных вариантов из желтого окна\
              5. Кнопка "ДАЛЕЕ" осуществляет согласие вашего выбора ответа введенного в малое окошко \
              6. В меню ФАЙЛ вы можете сохранить ваш текущий прогресс или загрузить прошлое сохранение, так же завершить игру'              
    text_help.insert(END, e_help)

def Label_1_black():
    label_1 = Label(tk, text='ВНИМАНИЕ ВАШ ВЫБОР!', fg='#FF0000', bg='#070707', padx=15, pady=6, font=('Arial', 14, 'bold'),
    anchor='n', justify=LEFT)
    label_1.place(x=435, y=565)

def Label_1_red():
    label_1 = Label(tk, text='ВНИМАНИЕ ВАШ ВЫБОР!', fg='#070707', bg='#070707', padx=15, pady=6, font=('Arial', 14, 'bold'),
    anchor='n', justify=LEFT)
    label_1.place(x=435, y=565)

def Label_1():        
    label_1 = Label(tk, text='ВНИМАНИЕ ВАШ ВЫБОР!', fg='#070707', bg='#070707', padx=15, pady=6, font=('Arial', 14, 'bold'), 
    anchor='n', justify=LEFT) 
    label_1.place(x=435, y=565)

btn1_1 = PhotoImage(file='Кнопка салатовая.png')
btn1_1 = btn1_1.subsample(7, 10)
 
Btn_start = Button(sc, image=btn1_1, highlightthickness=0, bg='#000000', activebackground='#000000', bd=0,
       fg='#66B2FF', activeforeground='#66B2FF', font='Arial 8 bold',
       compound=BOTTOM, text='ДАЛЕЕ', command=start).place(x=878, y=645)

menu_bar = Menu(tk)
file_menu = Menu(menu_bar, tearoff=0, background='#FFD700', foreground='green', activebackground='red')
file_menu.add_command(label='Сохранить как ...', command=save_game)
file_menu.add_command(label='Загрузить сохранение', command=load_game) 
file_menu.add_separator()
file_menu.add_command(label='Выйти из игры', command=on_closing)

menu_bar.add_cascade(label='Файл', menu=file_menu)
menu_bar.add_command(label='Помощь', command=help)
tk.configure(menu=menu_bar)

while app_running:
    if app_running:
        tk.update_idletasks()
        tk.update()
    sleep(0.005)
tk.destroy()