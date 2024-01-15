import  tkinter as tk
import sqlite3
buttons = []  # массив кнопок
list_btn = []
conn = sqlite3.connect('DataBase.db')
curs = conn.cursor()
frames = {}  # Словарь для хранения фреймов
def make_buttons_menu(a,list_btn, x,y, func):
    button = 0
    i=0
    for btn in range(len(list_btn)):
        btn = tk.Button(a, text=list_btn[btn], font="Helvetica 20", width=20, height=5, bg='white')
        btn.config(command=lambda button=button: func(button))
        btn.place(x=x, y=y)
        if i % 2 == 0:
            x += 350
        else:
            x = 0
            y += 200
        i += 1
        button += 1
        buttons.append(btn)

def make_buttons_menu_dop(a,list_btn, x,x_1,x_2, function):
    button = 0
    i = 0
    for btn in range(len(list_btn)):
        btn = tk.Button(a,text=list_btn[btn], font="Helvetica 14", width=19, height=4, bg='white')
        btn.config(command=lambda button=button: function(button))
        if i in range(0, 3):
            btn.place(x=x, y=0)
            x += 230
        elif i in range(3, 6):
            btn.place(x=x_1, y=120)
            x_1 += 230
        elif i in range(6, 8):
            btn.place(x=x_2, y=240)
            x_2 += 230
        i += 1
        button += 1
        buttons.append(btn)



