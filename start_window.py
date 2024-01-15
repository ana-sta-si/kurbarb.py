import tkinter as tk
from tkinter import LEFT, N, W, BOTTOM
from PIL import Image, ImageTk
import keyboard
import sqlite3
#главное окно программы
class MainAp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Касса') #название программы
        self['background'] = 'white'#цвет фона программы
        self.state('zoomed')  # размер окна
        # Создание фреймов
        Frame1(self)
        Frame2(self)
        Frame3(self)
#картинка в программе
class Frame1(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(width=1200, height=1100, x=0, y=0) #размеры Фрейма
        #добавление картинки
        image_1 = Image.open("images\start_image.jpg")
        image_1 = image_1.resize((1200, 1200))
        image_1 = ImageTk.PhotoImage(image_1)
        label_1 = tk.Label(self,image=image_1)
        label_1.image = image_1
        label_1.pack(pady=0, padx=0)
#логотип
class Frame2(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(width=300, height=300, x=1410, y=50) #размеры Фрейма
        self.configure(background="white")#фон
        #добавление картинки
        image_1 = Image.open("images\log.png")
        image_1 = image_1.resize((210, 150))
        image_1 = ImageTk.PhotoImage(image_1)
        label_1 = tk.Label(self,image=image_1, background='white')
        label_1.image = image_1
        label_1.pack(pady=0, padx=0)
#функция, отвечающая за нажатие кнопки
def press(letter):
        keyboard.write(letter)
#сравнение паролей
def pass_check(entr):
        con = sqlite3.connect('DataBase.db')
        cur = con.cursor()
        cur.execute("SELECT Должность FROM Работники WHERE Код = ?", [entr.get()])
        result = cur.fetchone()
        if result == ('управляющая',):
                app.destroy()
                import menu_maneger
        elif result == ('администратор',):
            app.destroy()
            import menu_administrator
        elif result == ('официант',):
            app.destroy()
            import window

        else:
                print("Access Denied")
#экранная клавиатура
class Frame3(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(width=550, height=800, x=1300, y=200) # размер и расположение фрейма
        self.configure(background="white") #фон
        #списки значений клавиатуры
        line_first = "123"
        line_second = "456"
        line_third = "789"
        line_fourth = "\u27140\u2718"
        #строка ввода
        entry_ = tk.Entry(self, width=5, show="*", font="Helvetica 44 bold", borderwidth=0, insertontime=0)
        entry_.config({"background": "white"})
        entry_.pack(padx=0,pady=20)
        entry_.focus_set()
        #первая строка клавиатуры
        tmp_frame1 = tk.Frame(self)
        tmp_frame1.config(background='white')
        tmp_frame1.pack(pady=0,padx=0)
        for letter in line_first:
            btn = tk.Button(tmp_frame1, text=letter, font=('', 60), borderwidth=0, background='white')
            btn.config(command=lambda b=letter: press(b))
            btn.pack(side=LEFT, expand=1, anchor=N, padx=30)
        # вторая строка клавиатуры
        tmp_frame2 = tk.Frame(self)
        tmp_frame2.config(background='white')
        tmp_frame2.pack(pady=20)
        for letter in line_second:
            btn = tk.Button(tmp_frame2, text=letter, font=('', 60), borderwidth=0, background='white')
            btn.config(command=lambda b=letter: press(b))
            btn.pack(side=LEFT,expand=1, pady=0, padx=30)
        # третья строка клавиатуры
        tmp_frame3 = tk.Frame(self)
        tmp_frame3.config(background='white')
        tmp_frame3.pack(pady=0)
        for letter in line_third:
            btn = tk.Button(tmp_frame3, text=letter, font=('', 60), borderwidth=0, background='white')
            btn.config(command=lambda b=letter: press(b))
            btn.pack(side=LEFT,expand=1, pady=0, padx=30)
        # четвертая строка клавиатуры
        tmp_frame4 = tk.Frame(self)
        tmp_frame4.config(background='white')
        tmp_frame4.pack(pady=20)
        for letter in line_fourth:
            if letter == "\u2718":
                btn = tk.Button(tmp_frame4, text=letter, font=('', 60), borderwidth=0, background='white')
                btn.config(command=lambda: [entry_.delete(0, tk.END)])
                btn.pack(side=LEFT, expand=1, pady=0, padx=20)
            if letter == "0":
                btn = tk.Button(tmp_frame4, text=letter, font=('', 60), borderwidth=0, background='white')
                btn.config(command=lambda b=letter: press(b))
                btn.pack(side=LEFT,expand=1, pady=0, padx=20)
            if letter == "\u2714":
                btn = tk.Button(tmp_frame4, text=letter, font=('', 60), borderwidth=0, background='white')
                btn.config(command=lambda e=entry_: pass_check(e))
                btn.pack(side=LEFT,expand=1, pady=0, padx=20)
app = MainAp()
app.mainloop()
