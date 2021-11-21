from tkinter import *
from tkinter.ttk import *
import sqlite3
from tkinter.messagebox import *
class view:
    def check(self):
        for i in self.t1.get_children():
            self.t1.delete(i)
        s = "select * from subjects where degree_name='" + self.txt1.get() + "' and semester='" + self.txt2.get() + "'"
        conn = sqlite3.connect("timetabledata.sqlite3")
        cr = conn.cursor()
        cr.execute(s)
        ans = cr.fetchall()

        i = 0
        for row in ans:
            self.t1.insert("", index=i, values=row)
            i += 1
    def __init__(self):
        self.root=Tk()
        self.p1 = PanedWindow(self.root)
        self.p2 = PanedWindow(self.root)
        s = "select Degree_name from programmes"
        self.conn = sqlite3.connect("timetabledata.sqlite3")
        self.cr = self.conn.cursor()
        self.cr.execute(s)
        ans = self.cr.fetchall()
        p = []
        for r in ans:
            p.append(r[0])
        self.lb1 = Label(self.p1, text='Select Degree')
        self.lb2 = Label(self.p1, text='Select Semester')
        self.txt1 = Combobox(self.p1, values=p, state='readonly')
        self.txt2 = Combobox(self.p1, values=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), state='readonly')
        self.bt1 = Button(self.p1, text='submit', command=self.check)
        self.t1 = Treeview(self.p2, columns=("subjectcode", "subjectname", "semester", "degree"))
        self.t1.heading("subjectcode", text="Subject Code")
        self.t1.heading("subjectname", text="Subject Name")
        self.t1.heading("semester", text="Semester")
        self.t1.heading("degree", text="Degree")
        self.t1["show"] = "headings"
        self.lb1.grid(row=0, column=0)
        self.txt1.grid(row=0, column=1)
        self.lb2.grid(row=0, column=2)
        self.txt2.grid(row=0, column=3)
        self.bt1.grid(row=0, column=4)

        self.t1.pack()
        self.p1.pack()
        self.p2.pack()
        self.root.mainloop()
