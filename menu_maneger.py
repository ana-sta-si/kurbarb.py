import tkinter as tk
from datetime import datetime
from tkinter import LEFT, NW
import sqlite3
#главное окно приложения
class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Касса') #название программы
        self['background'] = '#403a3a'#цвет фона программы
        self.state('zoomed') #размер окна
        self.put_data_time()#вызов функции отображения даты и времени
        Frame1(self)
        Work_with_workers(self)
        Work_with_providers(self)
        Kassa(self)
        Menu(self)
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
    # функция при нажатии на меню
def menu():
            pass
#фрейм 4 - верхнее меню
class Frame1(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(y=20, height=65, width=1930)
        self.configure(background="grey")
        self.btn_lock = tk.Button(self, text="\U0001f512",  font="Helvetica 50", command=self.lock, borderwidth=0, background='grey')
        self.btn_lock.place(y=-3, x=1850, height=65, width=65)
        self.btn_menu = tk.Button(self, text='\u2261', command=menu, font="Helvetica 65", borderwidth=0, background='grey')
        self.btn_menu.place(y=0, x=1770, height=65, width=65)
    # функция при нажимании замка
    def lock(self):
        app.destroy()
        import start_window
class Work_with_workers(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(y=90, height=900, width=400)
        self.configure(background="#403a3a")
        self.buttons = [] #массив кнопок
        self.make_buttons() #вызов функции создания кнопок меню
        label_1 = tk.Label(self,text="Персонал", foreground='#F8F8FF', background="#9932CC", height=1, width =21,  font="Helvetica 21")
        label_1.pack(side=LEFT, anchor=NW, padx=3, ipadx=9)
#создание кнопок меню
    def make_buttons(self):
        list_btn = ['Редактировать работников']
        button = 0
        x, y = 3, 40
        for btn in range(len(list_btn)):
            btn = tk.Button(self, text=list_btn[btn], font="Helvetica 17", width=27, height=3, bg='white')
            btn.config(command=lambda button=button:self.change_frame(button))
            btn.place(x=x, y=y)
            y += 100
            button += 1
            self.buttons.append(btn)
    # функция изменения фреймов
    def change_frame(self, button):
        for i in range(len(self.buttons)):
            if i == 0 and i == button:
                import work_with_workers
                app.destroy()
            elif i == 2 and i ==button:
                import work_with_provider
                app.destroy()
class Work_with_providers(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(y=90, x=400, height=900, width=400)
        self.configure(background="#403a3a")
        self.buttons = [] #массив кнопок
        self.make_buttons() #вызов функции создания кнопок меню
        label_1 = tk.Label(self, text="Поставщики", foreground='#F8F8FF', background="#4169E1", height=1, width=21,
                           font="Helvetica 21")
        label_1.pack(side=LEFT, anchor=NW, padx=3, ipadx=9)
#создание кнопок меню
    def make_buttons(self):
        list_btn = ['Контакты поставщиков']
        button = 0
        x, y = 3, 40
        for btn in range(len(list_btn)):
            btn = tk.Button(self, text=list_btn[btn], font="Helvetica 17", width=27, height=3, bg='white')
            btn.config(command=lambda button=button:self.change_frame(button))
            btn.place(x=x, y=y)
            y += 100
            button += 1
            self.buttons.append(btn)
# функция изменения фреймов
    def change_frame(self, button):
        for i in range(len(self.buttons)):
            if i == 0 and i == button:
                import work_with_provider
                app.destroy()
            elif i == 2 and i ==button:
                import work_with_provider
                app.destroy()
class Kassa(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(y=90, x=1182, height=900, width=735)
        self.configure(background="#403a3a")
        self.buttons = [] #массив кнопок
        self.make_buttons() #вызов функции создания кнопок меню
        label_1 = tk.Label(self, text="Касса", foreground='#F8F8FF', background="#2E8B57", height=1, width=21,
                           font="Helvetica 21")
        label_1.pack(side=LEFT, anchor=NW, padx=3, ipadx=255)
    # функция изменения фреймов
    def change(self, button):
        for i in range(len(self.buttons)):
            if i == 0 and i == button:
                import money_in
            elif i == 2 and i ==button:
                import money_out

#создание кнопок меню
    def make_buttons(self):
        listk_btn = ['Внести деньги', 'Возврат товара']
        button = 0
        x, y = 3, 40
        for btn in range(len(listk_btn)):
            btn = tk.Button(self, text=listk_btn[btn], font="Helvetica 17", width=27, height=3, bg='white')
            btn.config(command=lambda button=button:self.change(button))
            btn.place(x=x, y=y)
            y += 100
            button += 1
            self.buttons.append(btn)
        listk2_btn = ['Изъять деньги', 'Закрытые заказы']
        x, y = 373, 40
        for btn in range(len(listk2_btn)):
            btn = tk.Button(self, text=listk2_btn[btn], font="Helvetica 17", width=27, height=3, bg='white')
            btn.config(command=lambda button=button: self.change(button))
            btn.place(x=x, y=y)
            y += 100
            button += 1
            self.buttons.append(btn)
class Menu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(y=90, x=800, height=900, width=365)
        self.configure(background="#403a3a")
        self.buttons = [] #массив кнопок
        self.make_buttons() #вызов функции создания кнопок меню
        label_1 = tk.Label(self, text="Меню", foreground='#F8F8FF', background="#F08080", height=1, width=21,
                           font="Helvetica 21")
        label_1.pack(side=LEFT, anchor=NW, padx=3, ipadx=255)
    # функция изменения фреймов
    def change(self, button):
        for i in range(len(self.buttons)):
            if i == 0 and i == button:
                import work_with_menu
            elif i == 2 and i ==button:
                import money_out

#создание кнопок меню
    def make_buttons(self):
        listk_btn = ['Редактировать меню']
        button = 0
        x, y = 3, 40
        for btn in range(len(listk_btn)):
            btn = tk.Button(self, text=listk_btn[btn], font="Helvetica 17", width=27, height=3, bg='white')
            btn.config(command=lambda button=button:self.change(button))
            btn.place(x=x, y=y)
            y += 100
            button += 1
            self.buttons.append(btn)





app = MainApp()
app.mainloop()