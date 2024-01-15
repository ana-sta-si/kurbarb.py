import tkinter as tk
from datetime import datetime
from tkinter import LEFT, NW, RIGHT
import sqlite3
#главное окно приложения
class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Внесение денег') #название программы
        self['background'] = '#202020'#цвет фона программы
        self.geometry('1000x800+500+100') #размер окна
        self.var = tk.StringVar()
        self.label_1 = tk.Label(self,text="ВНЕСЕНИЕ", foreground='#F8F8FF', font="Helvetica 25", background='#202020')
        self.label_1.pack(pady=20)
        self.label_2 = tk.Label(self,text="Внесение наличных", foreground='#FFFF99', font="Helvetica 15", background='#202020')
        self.label_2.pack(pady=10)
        label_3 = tk.Label(self,text="Комментарий:", foreground='#F8F8FF', font="Helvetica 12",background='#202020')
        label_3.pack(pady=180,padx=230, side=LEFT, anchor=NW)
        entry_1 = tk.Entry(self,background='#F8F8FF', foreground='black')
        entry_1.place(y = 350, x =230, height=300, width=550)
        vcmd = (self.register(self.callback))
        entry_2 = tk.Entry(self,background='grey', foreground='white', font="Helvetica 35 bold", justify= RIGHT, validate='all', validatecommand=(vcmd, '%P'))
        entry_2.place(y = 200, x =230, height=80, width=550)
        but_otmena = tk.Button(self, background='#202020', text='Отмена', command=self.close, font="Helvetica 25 bold", foreground='#F8F8FF', borderwidth=0)
        but_otmena.place(x = 845, y = 730)
        but_ok = tk.Button(self, background='#202020', text='Внести', command=self.in_, font="Helvetica 25 bold", foreground='#F8F8FF', borderwidth=0)
        but_ok.place(x = 690, y = 730)
    def callback(self, P):
        print("P = ", P)
        if str.isnumeric(P) or ( P == "" or  "," in P) :
            return True
        else:
            return False


    def close(self):
        app.destroy()
    def in_(self):
        pass






app = MainApp()
app.overrideredirect(True)
app.mainloop()