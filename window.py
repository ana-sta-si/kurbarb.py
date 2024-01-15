import sqlite3
import tkinter as tk
from datetime import datetime
from PIL import Image, ImageTk
#главное окно приложения
class MainApp(tk.Tk):
    # работа с базой данных
    conn = sqlite3.connect('DataBase.db')
    curs = conn.cursor()
    def __init__(self):
        super().__init__()
        self.title('Касса') #название программы
        self['background'] = '#403a3a'#цвет фона программы
        self.state('zoomed') #размер окна
        self.buttons = [] #массив кнопок
        self.make_buttons() #вызов функции создания кнопок меню
        self.put_data_time()#вызов функции отображения даты и времени
        self.frames = {}  # Словарь для хранения фреймов
        # Создание фреймов
        frame1 = Frame1(self)
        frame2 = Frame2(self)
        frame3 = Frame3(self)
        frame4 = Frame4(self)
        frame0 = Frame0(self)
        # Добавление фреймов в словарь
        self.frames[Frame1] = frame1
        self.frames[Frame2] = frame2
        self.frames[Frame3] = frame3
        self.frames[Frame4] = frame4
        self.frames[Frame0] = frame0
    #функция, которая показывает фреймы
    def show_frame(self, container):
            frame = self.frames[container]
            frame.tkraise()
    # динамическое изменение времени
    def update_time(self):
        self.label_str_up.config(text=f"{datetime.now():%H:%M:%S  %d/%m/%y}")
        self.after(100, self.update_time)
    # изменение времени
    def put_data_time(self):
        self.label_str_up = tk.Label(background='#403a3a', fg='#f0f0f0')
        self.label_str_up.config(anchor="sw")
        self.label_str_up.place(height=20, width=1900)
        self.update_time()
    #создание кнопок меню
    def make_buttons(self):
        list_btn = ['Предзаказ', 'Зал', 'Доставка']
        button = 0
        x, y = 3, 90
        for btn in range(len(list_btn)):
            btn = tk.Button(self, text=list_btn[btn], font="Helvetica 25", width=17, height=2, bg='white')
            btn.config(command=lambda button=button: [self.change_colour(button), self.change_frame(button)])
            btn.place(x=x, y=y)
            y += 110
            button += 1
            self.buttons.append(btn)
    # функция изменения цвета кнопок
    def change_colour(self, button):
        for i in range(len(self.buttons)):
            if i == button:
                self.buttons[i].config(bg='#FFFF99')
            else:
                self.buttons[i].config(bg='white')
    # функция изменения фреймов
    def change_frame(self, button):
        for i in range(len(self.buttons)):
            if i == 0 and i == button:
                frame = self.frames[Frame1]
                frame.tkraise()
            elif i == 1 and i == button:
                frame = self.frames[Frame2]
                frame.tkraise()
            elif i == 2 and i == button:
                frame = self.frames[Frame3]
                frame.tkraise()
#фрейм 1 - предзаказ
class Frame1(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(width=1550, height=900, x=350, y=90)
        self.configure(background="#403a3a")
        self.buttons = []
        MainApp.curs.execute("SELECT Номер_стола FROM Стол WHERE Описание = 'Самовывоз'")
        list_btn = []
        for row in MainApp.curs:
            for field in row:
                list_btn.append(field)
        button = 0
        x, y = 2, 2
        for btn in range(len(list_btn)):
            btn = tk.Button(self, text=list_btn[btn], font="Helvetica 25", width=6, height=2, bg='white')
            btn.config(command=lambda button=button: self.change_windows(button))
            btn.place(x=x, y=y)
            x += 150
            button += 1
            self.buttons.append(btn)
    def change_windows(self, button):
        # for i in range(len(self.buttons)):
        num_tb = button+91
        MainApp.curs.execute(f'INSERT INTO Карта_заказа (Номер_стола) VALUES ({num_tb})')
        MainApp.conn.commit()
        app.destroy()
        import tabels
#фрейм 2 - зал
class Frame2(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(width=1550, height=900, x=350, y=90)
        self.configure(background="#403a3a")
        self.buttons = []
        MainApp.curs.execute("SELECT Номер_стола FROM Стол WHERE Описание = 'Зал' ORDER BY Номер_стола DESC")
        list_btn = []
        for row in MainApp.curs:
            for field in row:
                list_btn.append(field)
        button = 0
        x, y = 150, 2
        for btn in range(0, 2):
            btn = tk.Button(self, text=list_btn[btn], font="Helvetica 25", width=6, height=4, bg='white')
            btn.config(command=lambda button=button: self.change_windows(button))
            btn.place(x=x, y=y)
            x += 170
            button += 1
            self.buttons.append(btn)
        for btn in range(2,7):
            btn = tk.Button(self, text=list_btn[btn], font="Helvetica 25", width=4, height=2, bg='white')
            btn.config(command=lambda button=button: self.change_windows(button))
            btn.place(x=x, y=y)
            x += 100
            button += 1
            self.buttons.append(btn)
        x+=100
        for btn in range(7,9):
            btn = tk.Button(self, text=list_btn[btn], font="Helvetica 25", width=17, height=4, bg='white')
            btn.config(command=lambda button=button: self.change_windows(button))
            btn.place(x=x, y=y)
            y += 350
            button += 1
            self.buttons.append(btn)
        x-=20
        y-=450
        list_labels = ['1', '2']
        for lab in range(len(list_labels)):
            label_stoika1 = tk.Label(self, background='#808080', width=60, height=1)
            label_stoika1.place(x=x, y=y)
            y += 360
        x, y = 455, 2
        for lab in range(len(list_labels)):
            label_stoika = tk.Label(self,background='#808080', width=2, height=14)
            label_stoika.place(x=x, y=y)
            x += 540
        label_in = tk.Label(self,background='#403a3a', text='Вход',font="Courier 50")
        label_in.place(x=1200,y=700)
    def change_windows(self, button):
        # for i in range(len(self.buttons)):
        num_tb = button+1
        MainApp.curs.execute(f'INSERT INTO Карта_заказа (Номер_стола) VALUES ({num_tb})')
        MainApp.conn.commit()
        app.destroy()
        import tabels
#фрейм 3 - доставка
class Frame3(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(width=1550, height=900, x=350, y=90)
        self.configure(background="#403a3a")
        self.buttons=[]
        MainApp.curs.execute("SELECT Номер_стола FROM Стол WHERE Описание = 'Доставка'")
        list_btn = []
        for row in MainApp.curs:
            for field in row:
                list_btn.append(field)
        button = 0
        x, y = 2, 2
        for btn in range(len(list_btn)):
            btn = tk.Button(self, text=list_btn[btn], font="Helvetica 25", width=6, height=2, bg='white')
            btn.config(command=lambda button=button: self.change_windows(button))
            btn.place(x=x, y=y)
            x += 150
            button += 1
            self.buttons.append(btn)
    def change_windows(self, button):
        # for i in range(len(self.buttons)):
        num_tb = button+201
        MainApp.curs.execute(f'INSERT INTO Карта_заказа (Номер_стола) VALUES ({num_tb})')
        MainApp.conn.commit()
        app.destroy()
        import tabels
#фрейм 4 - верхнее меню
class Frame4(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(y=20, height=65, width=1930)
        self.configure(background="grey")
        self.btn_lock = tk.Button(self, text="\U0001f512",  font="Helvetica 50", command=self.lock, borderwidth=0, background='grey')
        self.btn_lock.place(y=-3, x=1850, height=65, width=65)
        self.btn_menu = tk.Button(self, text='\u2261', command=self.menu, font="Helvetica 65", borderwidth=0, background='grey')
        self.btn_menu.place(y=0, x=1770, height=65, width=65)
    # функция при нажатии на меню
    def menu(self):
            pass
    # функция при нажимании замка
    def lock(self):
        app.destroy()
        import start_window
#фрейм 0 - просто цвет
class Frame0(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(width=1550, height=900, x=350, y=90)
        self.configure(background="#403a3a")
app = MainApp()
app.mainloop()
