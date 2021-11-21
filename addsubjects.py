from tkinter import *
from tkinter.ttk import *
import sqlite3
from tkinter.messagebox import *
class addsub:
    def insert(self):
        conn=sqlite3.connect("timetabledata.sqlite3")
        s="insert into subjects values ('"+self.txt1.get()+"','"+self.txt2.get()+"','"+self.txt3.get()+"','"+self.txt4.get()+"')"
        cr=conn.cursor()
        conn.execute(s)
        conn.commit()
        conn.close()
        showinfo("","Subject Added")
    def __init__(self):
        self.x=Tk()
        self.x.geometry("400x400")
        s="select Degree_name from programmes"
        self.conn=sqlite3.connect("timetabledata.sqlite3")
        self.cr=self.conn.cursor()
        self.cr.execute(s)
        ans=self.cr.fetchall()
        p=[]
        for r in ans:
            p.append(r[0])
        self.lb=Label(self.x,text="Enter Subject Code")
        self.lb2=Label(self.x,text="Enter Subject Name")
        self.lb3=Label(self.x,text="Enter Semester")
        self.lb4=Label(self.x,text="Enter degree name")
        self.txt1=Entry(self.x)
        self.txt2=Entry(self.x)
        self.txt3=Entry(self.x)
        self.txt4=Combobox(self.x,values=p,state='readonly')
        self.bt1=Button(self.x,text="Submit",command=self.insert)
        self.lb.grid(row=0,column=0)
        self.lb2.grid(row=1,column=0)
        self.lb3.grid(row=2,column=0)
        self.lb4.grid(row=3,column=0)
        self.txt1.grid(row=0,column=1)
        self.txt2.grid(row=1,column=1)
        self.txt3.grid(row=2,column=1)
        self.txt4.grid(row=3,column=1)
        self.bt1.grid(row=4,column=1)
        self.x.mainloop()
