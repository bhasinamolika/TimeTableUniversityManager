from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import sqlite3
class editcourse:
    conn=sqlite3.connect("timetabledata.sqlite3")
    def remove(self):
        s="delete from programmes where degree_name='"+self.cb1.get()+"'"
        self.cr.execute(s)
        self.conn.commit()
        showinfo("","Removed Successfully")
        self.txt1.delete(0,"end")
        self.cb1.current(0)
    def search(self):
        p="select * from programmes where degree_name='"+self.cb1.get()+"'"
        self.cr.execute(p)
        ans=self.cr.fetchone()
        self.txt1.insert(0,str(ans[1]))
    def edit(self):
        n="update Programmes set Description='"+self.txt3.get()+"' where Degree_name='"+self.cb2.get()+"'"
        self.cr.execute(n)
        self.conn.commit()
        showinfo("","Description Edited")


    def __init__(self):
        self.root=Tk()
        self.root.geometry("550x550")
        self.cr=self.conn.cursor()
        s="select * from Programmes"
        self.cr.execute(s)
        self.ans=self.cr.fetchall()
        p=["Select Programme"]
        for r in self.ans:
            p.append(r[0])
        self.lb1=Label(self.root,text="Programme Name")
        self.lb2=Label(self.root,text="Description")

        self.lb3 = Label(self.root, text="Programme Name")
        self.lb4 = Label(self.root, text="Edit Description")
        self.cb2 = Combobox(self.root, values=p, state='readonly')
        self.bt=Button(self.root,text="Edit",command=self.edit)
        self.txt3=Entry(self.root)
        self.cb1=Combobox(self.root,values=p,state='readonly')

        self.cb1.current(0)
        self.bt1=Button(self.root,text="Search",command=self.search)
        self.bt2=Button(self.root,text='Delete',command=self.remove)
        self.txt1=Entry(self.root)

        self.lb1.grid(row=0,column=0)
        self.lb2.grid(row=1,column=0)
        self.bt1.grid(row=0,column=2)
        self.bt2.grid(row=2,column=1)
        self.lb3.grid(row=3,column=0)
        self.txt3.grid(row=4,column=1)
        self.lb4.grid(row=4,column=0)
        self.cb2.grid(row=3,column=1)
        self.bt.grid(row=5,column=1)

        self.cb1.grid(row=0,column=1)
        self.txt1.grid(row=1,column=1)
        self.root.mainloop()
