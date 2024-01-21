import tkinter as tk
from tkinter import LEFT, NW, RIGHT
import sqlite3
import datetime
from tkinter.messagebox import showerror
#главное окно приложения
class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Изъятие денег') #название программы
        self['background'] = '#202020'#цвет фона программы
        self.geometry('1000x800+500+100') #размер окна
        self.curr_time = datetime.datetime.now()
        self.label_1 = tk.Label(self,text="Изъятие", foreground='#F8F8FF', font="Helvetica 25", background='#202020')
        self.label_1.pack(pady=20)
        self.label_2 = tk.Label(self,text="Изъятие наличных", foreground='#FFFF99', font="Helvetica 15", background='#202020')
        self.label_2.pack(pady=10)
        label_3 = tk.Label(self,text="Комментарий:", foreground='#F8F8FF', font="Helvetica 12",background='#202020')
        label_3.pack(pady=180,padx=230, side=LEFT, anchor=NW)
        self.entry_1 = tk.Entry(self,background='#F8F8FF', foreground='black')
        self.entry_1.place(y = 350, x =230, height=300, width=550)
        self.entry_2 = tk.Entry(self,background='grey', foreground='white', font="Helvetica 35 bold", justify= RIGHT )
        self.entry_2.place(y = 200, x =230, height=80, width=550)
        but_otmena = tk.Button(self, background='#202020', text='Отмена', command=self.close, font="Helvetica 25 bold", foreground='#F8F8FF', borderwidth=0)
        but_otmena.place(x = 845, y = 730)
        but_ok = tk.Button(self, background='#202020', text='Изъять', command= lambda : self.out_(self.curr_time,self.entry_2.get(),self.entry_1.get()), font="Helvetica 25 bold", foreground='#F8F8FF', borderwidth=0)
        but_ok.place(x = 690, y = 730)
    def close(self):
        app.destroy()
    def out_(self, data, summa,comm):
        conn = sqlite3.connect('DataBase.db')
        curs = conn.cursor()
        bal = curs.execute('SELECT SUM(Дебит)-SUM(Кредит) FROM Финансы').fetchone()
        ibal =bal[0] - int(summa)
        print(ibal)
        if ibal >= 0:
            conn.execute('INSERT INTO Финансы (Дата, Кредит, Баланс, Комментарий) VALUES (?,?,?,?)',
                         (data, summa, ibal, comm))
            conn.commit()
            curs.close()
            conn.commit()
            app.destroy()
        else:showerror(title="Ошибка", message="Вы не можете изъять больше денег, чем находится в кассе")






app = MainApp()
app.overrideredirect(True)
app.mainloop()
