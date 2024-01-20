import tkinter as tk
from tkinter import ttk
import sqlite3
#главное окно приложения
class MainApp(tk.Tk):
    conn = sqlite3.connect('DataBase.db')
    cursor = conn.cursor()
    def __init__(self):
        super().__init__()
        self.title('Работа с поставщиками') #название программы
        self['background'] = '#F8F8FF'#цвет фона программы
        self.state('zoomed') #размер окна
        Frame1(self)
        Frame2(self)
        #engine = sqlalchemy.create_engine('')
# фрейм для таблицы сотрудников
class Frame1(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(y=0, x =0, height=1200, width=1150)
        self.configure(background="white")
        # определяем столбцы
        columns = ("code",  "name", "contacts", "product")
        tree = ttk.Treeview(self, columns=columns, show="headings")
        tree.pack(fill=tk.BOTH, expand=1)
        # определяем заголовки
        tree.heading("code", text="Код")
        tree.heading("name", text="Название организации")
        tree.heading("contacts", text="Контакты")
        tree.heading("product", text="Товар")
        MainApp.cursor.execute("SELECT * FROM Поставщики")
        result = MainApp.cursor.fetchall()
        for row in result:
            tree.insert('', tk.END, values=row)
# фрейм для добавления новых сотрудников
class Frame2(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(y=0, x = 1151, height=1200, width=950)
        self.configure(background="grey")
        label_1 = tk.Label(self, text = "Добавить поставщика", font="Helvetica 47", foreground="black", background='grey')
        label_1.pack(pady=90, padx=100, anchor=tk.NW)
        list_label = ['Код', 'Организация', "Контакты", "Товар"]
        for lable in range(len(list_label)):
            lable = tk.Label(self, foreground="black", font="Helvetica 27", text=list_label[lable], background='grey')
            lable.pack(padx=3, pady=5, anchor=tk.W)
        vcmd = (self.register(self.only_text))
        self.text_1 = tk.Entry(self,font="Helvetica 27", background='white', foreground='black',validate='all', validatecommand=(vcmd, '%P'))
        self.text_1.place(x = 280, y = 260)
        self.text_2 = tk.Entry(self,font="Helvetica 27", background='white', foreground='black',validate='all', validatecommand=(vcmd, '%P'))
        self.text_2.place(x = 280, y = 315)
        self.text_3 = tk.Entry(self,font="Helvetica 27", background='white', foreground='black',validate='all', validatecommand=(vcmd, '%P'))
        self.text_3.place(x = 280, y = 370)
        self.text_4 = tk.Entry(self,font="Helvetica 27", background='white', foreground='black',validate='all', validatecommand=(vcmd, '%P'))
        self.text_4.place(x = 280, y = 425)
        vcmd = (self.register(self.only_num))
        but_add = tk.Button(self, background='grey', text='Добавить', command= lambda: self.add(self.text_1.get(),self.text_2.get(),self.text_3.get(),self.text_4.get()), font="Helvetica 27 bold", foreground='black', borderwidth=0)
        but_add.place(x = 50, y = 900)
        but_deli = tk.Button(self, background='grey', text='Очистить', command= self.deli, font="Helvetica 27 bold", foreground='black', borderwidth=0)
        but_deli.place(x = 300, y = 900)
        but_ret =  tk.Button(self, background='grey', text='Назад', command= self.ret, font="Helvetica 27 bold", foreground='black', borderwidth=0)
        but_ret.place(x = 550, y = 900)
    #добавление данных в базу данных
    def add(self, code, name, contacts, product):
        MainApp.cursor.execute(f'SELECT * FROM Поставщики WHERE Код = "{code}";')
        MainApp.result = MainApp.cursor.fetchone()
        if MainApp.result !=[]:
            print('уже есть')
            MainApp.cursor.execute(f'INSERT INTO Поставщики (Код, Название, Контакты, Товар) VALUES ("{code}", "{name}","{contacts}", "{product}" )')
            MainApp.conn.commit()
        MainApp.cursor.close()
        MainApp.conn.commit()
    #очистка всех полей
    def deli(self):
        self.text_1.delete(0, 'end')
        self.text_2.delete(0, 'end')
        self.text_3.delete(0, 'end')
        self.text_4.delete(0, 'end')
        self.combo.delete(0, 'end')
    #возвращение в меню
    def ret(self):
        app.destroy()
    # проверка ввода - можно только текст
    def only_text(self, P):
        if str.istitle(P) or P =="":
            return True
        else:
            return False
    # проверка ввода - можно только цифры
    def only_num(self, P):
        if str.isnumeric(P) or P =="":
            return True
        else:
            return False




app = MainApp()
app.mainloop()
