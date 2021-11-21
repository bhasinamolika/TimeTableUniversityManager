import sqlite3
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import *
class demo:
    conn=sqlite3.connect("timetabledata.sqlite3")
    def getdata(self,d):

        s="select subject_code from subjects where degree_name='"+self.cb.get()+"' "
        self.cr.execute(s)
        ans=self.cr.fetchall()
        x=["Select Subjects"]
        for r in ans:
            x.append(r[0])
        self.cb1.config(values=x)
        self.cb2.config(values=x)
    def remove(self):
        s="delete from subjects where subject_code='"+self.cb1.get()+"'"
        self.cr.execute(s)
        self.conn.commit()
        showinfo("","Removed Successfully")
        self.txt1.delete(0,"end")
        self.cb1.current(0)
    def search(self):
        p="select * from subjects where subject_code='"+self.cb1.get()+"'"
        self.cr.execute(p)
        ans=self.cr.fetchone()
        self.txt1.insert(0,str(ans[2]))
    def edit(self):
        n="update subjects set semester='"+self.txt3.get()+"' where subject_code='"+self.cb2.get()+"' "
        self.cr.execute(n)
        self.conn.commit()
        showinfo("","Semester Edited")
    def __init__(self):
        self.root=Tk()
        self.root.geometry("550x550")
        self.cr = self.conn.cursor()

        m="select * from Programmes"


        self.cr.execute(m)
        self.ans2=self.cr.fetchall()

        h=["Select Degree"]
        for row in self.ans2:
            h.append(row[0])

        self.cb = Combobox(self.root, values=h, state='readonly')
        self.cb.bind("<<ComboboxSelected>>",self.getdata)


        self.lb1 = Label(self.root, text="Subject Code")
        self.lb2 = Label(self.root, text="Semester")
        self.lb=Label(self.root,text="Select Degree")

        self.lb3 = Label(self.root, text="Subject Code")
        self.lb4 = Label(self.root, text="Edit Semester")
        self.cb2 = Combobox(self.root, state='readonly')

        self.bt = Button(self.root, text="Edit", command=self.edit)
        self.txt3 = Entry(self.root)
        self.cb1 = Combobox(self.root, state='readonly')



        self.bt1 = Button(self.root, text="Search", command=self.search)
        self.bt2 = Button(self.root, text='Delete', command=self.remove)
        self.txt1 = Entry(self.root)
        self.lb.grid(row=0,column=0)
        self.cb.grid(row=0,column=1)
        self.lb1.grid(row=1, column=0)
        self.lb2.grid(row=2, column=0)
        self.bt1.grid(row=1, column=2)
        self.bt2.grid(row=3, column=1)
        self.lb3.grid(row=4, column=0)
        self.txt3.grid(row=5, column=1)
        self.lb4.grid(row=5, column=0)
        self.cb2.grid(row=4, column=1)
        self.bt.grid(row=6, column=1)

        self.cb1.grid(row=1, column=1)
        self.txt1.grid(row=2, column=1)
        self.root.mainloop()
