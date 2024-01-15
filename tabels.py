import tkinter as tk
from tkinter import ttk
from datetime import datetime
from time import sleep
import sqlite3
import func_btn
#главное окно приложения
class MainApp(tk.Tk):
    # работа с базой данных
    conn = sqlite3.connect('DataBase.db')
    curs = conn.cursor()
    frames = {}  # Словарь для хранения фреймов
    def __init__(self):
        super().__init__()
        self.title('Касса') #название программы
        self['background'] = '#403a3a'#цвет фона программы
        self.state('zoomed') #размер окна
        self.put_data_time()#вызов функции отображения даты и времени
        #добавление фреймов
        frame1 = Frame_drink(self)
        frame2 = Frame_alc(self)
        frame3 = Frame_pizza(self)
        frame = Frame_menu(self)
        Frame_zakaz(self)
        Frame_data_zakaz(self)
        Data_zakaz(self)
        Frame1(self)
        Frame2(self)
        # Добавление фреймов в словарь
        self.frames[0] = frame
        self.frames[1] = frame1
        self.frames[2] = frame2
        self.frames[3] = frame3
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
#фрейм 1 - верхнее меню
class Frame1(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(y=20, height=65, width=1930)
        self.configure(background="white")
        self.btn_lock = tk.Button(self, text="\U0001f512",  font="Helvetica 50", command=self.lock, borderwidth=0, background='white')
        self.btn_lock.place(y=-3, x=1850, height=65, width=65)
        self.btn_menu = tk.Button(self, text='\u2261', command=self.menu, font="Helvetica 65", borderwidth=0, background='white')
        self.btn_menu.place(y=0, x=1770, height=65, width=65)
    # функция при нажатии на меню
    def menu(self):
            pass
    # функция при нажимании замка
    def lock(self):
        app.destroy()
        import start_window
#фрейм 2 - меню выхода
class Frame2(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(y=85, x = 760, height=65, width=1930)
        self.configure(background="#403a3a")
        self.btn_lock = tk.Button(self, text="\u2302", font="Helvetica 50",  borderwidth=0,background='#403a3a', command= self.menu)
        self.btn_lock.place(y=0, x=305, height=65, width=65)
    # функция при нажатии на меню
    def menu(self):
        frame = MainApp.frames[0]
        frame.tkraise()
#
class Data_zakaz(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(y=65, x = 0, height=85, width=750)
        self.configure(background="#002238")
        # result = MainApp.curs.execute("SELECT Номер_стола FROM Карта_заказа")
        # num_tb =0
        # for row in result:
        #     for field in row:
        #         num_tb = field
        # label = tk.Label(self,text=f"Cтол {num_tb}", font="Helvetica 25",background="#002238", foreground='white')
        # label.pack(anchor=tk.W, pady=30, padx=10)

#Фрейм 2 - фрейм меню
class Frame_menu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(y=150, x = 760, height=820, width=700)
        self.configure(background="#403a3a")
        self.buttons = []  # массив кнопок
        MainApp.curs.execute("SELECT Название FROM Разделы_меню")
        list_btn = []
        for row in MainApp.curs:
            for field in row:
                list_btn.append(field)
        # вызов функции создания кнопок меню
        func_btn.make_buttons_menu(self, list_btn, 0, 0, self.change_frame)
        self.buttons = func_btn.buttons
        self.menu = [Frame_drink, Frame_alc, Frame_pizza]
# функция изменения фреймов
    def change_frame(self, button):
        frame = MainApp.frames[button+1]
        frame.tkraise()
        # for i in range(len(self.buttons)):
        #     if i == 0 and i == button:
        #         frame = MainApp.frames[Frame_drink]
        #         frame.tkraise()
        #     elif i == 1 and i == button:
        #         frame = MainApp.frames[Frame_alc]
        #         frame.tkraise()
        #     elif i == 2 and i == button:
        #         frame = MainApp.frames[Frame_pizza]
        #         frame.tkraise()
class Frame_zakaz(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(y=150, x=0, height=605, width=750)
        self.configure(background="white")
        # определяем столбцы
        columns = ("name", "number", "price")
        tree = ttk.Treeview(self, columns=columns, show="headings")
        tree.pack(fill=tk.BOTH, expand=1)
        style = ttk.Style()
        style.configure("Treeview", font=('Helvetica', 10))
        MainApp.curs.execute("SELECT Название_блюда, Количество, Цена_блюда FROM Карта_заказа")
        result = MainApp.curs.fetchall()
        for row in result:
            tree.insert('', tk.END, values=row)
    #  способ 2   self.updt(tree)
    # def updt(self, tree):
    #     for x in range(100):
    #         sleep(1)
    #         tree.config(text=str(x))
    #         self.update()
    #     способ 1 self.update_bd()
    # #     Thread(target=self.update_bd).start()
    # def update_bd(self):
    #     while True:
    #         dt_str = datetime.today().strftime("%m/%d/%y - %I:%M:%S %p")
    #         MainApp.curs.config(text=dt_str)
    #         query.UpdateStats()
    #         query.UpdateCounts()
        # scroll_bar = tk.Scrollbar(self)
        # scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)

#Фрейм 3 - фрейм напитков
class Frame_drink(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(y=150, x = 760, height=820, width=700)
        self.configure(background="#403a3a")
        self.buttons = []  # массив кнопок
        MainApp.curs.execute("SELECT Название FROM Меню WHERE Код_раздела = '1'")
        list_btn = []
        for row in MainApp.curs:
            for field in row:
                list_btn.append(field)
        self.buttons = func_btn.buttons
        func_btn.make_buttons_menu_dop(self, list_btn, 0, 0, 0, self.add_possition)

    def add_possition(self, button):
        for i in range(len(self.buttons)):
            if i == 0 and i == button:
                result = MainApp.curs.execute(f'insert into Карта_заказа (Название_блюда, Цена_блюда) select Название, Цена from Меню WHERE Код_раздела = 1 and Код_блюда = {i + 1}')
                if result != []:
                    query = "Update Карта_заказа set Количество = 1"
                MainApp.curs.execute(query)
                MainApp.conn.commit()
                MainApp.curs.fetchall()
                MainApp.conn.commit()
            elif i == 1 and i == button:
                result = MainApp.curs.execute(f'insert into Карта_заказа (Название_блюда, Цена_блюда) select Название, Цена from Меню WHERE Код_раздела = 1 and Код_блюда = {i + 1}')
                if result != []:
                    l=0
                    query = f"Update Карта_заказа set Количество = {l+1}"
                #     l+=1
                # elif result ==[]:
                #     query = f"Update Карта_заказа set Количество = {l + 1}"
                #     l+=1
                MainApp.curs.execute(query)
                MainApp.conn.commit()
                MainApp.curs.fetchall()
                MainApp.conn.commit()
                # MainApp.curs.execute(f'SELECT Название, Цена from Меню WHERE Код_раздела = 1 and Код_блюда = {i+1}')
                # rows = MainApp.curs.fetchall()
                # MainApp.curs.executemany("insert into Карта_заказа (Название_блюда, Цена_блюда) values (%s,%s);", rows)
                # # cursor1.execute('SELECT * FROM имя_таблицы')
                # data = cursor1.fetchall()
                # query = 'INSERT INTO имя_таблицы VALUES (?, ?, ...)'
                # cursor2.executemany(query, data)
                #
                # # Сохранение изменений и закрытие соединений
                # conn2.commit()
                # conn2.close()
                # conn1.close()
                # MainApp.curs.execute( f'insert into Карта_заказа (Название_блюда, Цена_блюда) select Название, Цена from Меню WHERE Код_раздела = 1 and Код_блюда = {i+1}')
                # MainApp.curs.fetchall()
                # MainApp.curs.close()
                # MainApp.curs.execute(f"SELECT Цена FROM Меню WHERE Код_раздела = 1 and Код_блюда = {i+1}")
                # result = MainApp.curs.fetchall()
                # MainApp.curs.execute(f"SELECT Название FROM Меню WHERE Код_раздела = 1 and Код_блюда = {i+1}")
                # res = MainApp.curs.fetchall()
                # for row in result:
                #     for field in row:
                #         price = field
                # for row in res:
                #     for fields in row:
                #         name = fields
                #
                # print(lst)
        # for i in range(len(self.buttons)):
        #     if i == 0 and i == button:
        #         frame = MainApp.frames[Frame_drink]
        #         frame.tkraise()
        #     elif i == 1 and i == button:
        #         frame = MainApp.frames[Frame_alc]
        #         frame.tkraise()
        #     elif i == 2 and i == button:
        #         frame = MainApp.frames[Frame_pizza]
        #         frame.tkraise()
        #     MainApp.curs.execute(f"SELECT Название, Цена FROM Меню WHERE Код_раздела = '{code_raz}'")
        #     list_btn = []
        #     for row in MainApp.curs:
        #         for field in row:
        #             list_btn.append(field)
        #     print(list_btn)

#Фрейм 4 - фрейм алкоголя
class Frame_alc(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(y=150, x = 760, height=820, width=700)
        self.configure(background="#403a3a")
        self.buttons = []  # массив кнопок
        MainApp.curs.execute("SELECT Название FROM Меню WHERE Код_раздела = '2'")
        # list_btn = []
        # for row in MainApp.curs:
        #     for field in row:
        #         list_btn.append(field)
        # func_btn.make_buttons_menu_dop(self, list_btn, 0, 0, 0, func_btn.add_possition(2))
#Фрейм 5 - фрейм пиццы
class Frame_pizza(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(y=150, x=760, height=820, width=700)
        self.configure(background="#403a3a")
        self.buttons = []  # массив кнопок
        MainApp.curs.execute("SELECT Название FROM Меню WHERE Код_раздела = '3'")
        # list_btn = []
        # for row in MainApp.curs:
        #     for field in row:
        #         list_btn.append(field)
        # func_btn.make_buttons_menu_dop(self, list_btn, 0, 0, 0, func_btn.add_possition(3))
class Frame_data_zakaz(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(y=755, x=0, height=180, width=750)
        self.configure(background="#002238")
        res = MainApp.curs.execute("SELECT Количество * Цена_блюда FROM Карта_заказа")
        list_ol =[]
        for row in res:
            for field in row:
                 price = field
                 list_ol.append(price)
        print(sum(list_ol))
        label = ttk.Label(self, text=f'{sum(list_ol)} p.', foreground='white', font="Helvetica 60", background="#002238")
        label.pack(anchor=tk.E, padx=120, pady=36)
        btn_sk = tk.Button(self, text="Скидка", foreground='black', font="Helvetica 14", borderwidth=0, background='white', width=2, height=3)
        btn_sk.place(x=0, y=0, height=605, width=250)
app = MainApp()
app.mainloop()