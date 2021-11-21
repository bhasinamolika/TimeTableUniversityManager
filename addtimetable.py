import sqlite3
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import *
class addtimetable:
    def getdata(self,d):

        s="select subject_code from subjects where degree_name='"+self.cb1.get()+"' and semester='"+self.cb2.get()+"'"
        self.cr.execute(s)
        ans=self.cr.fetchall()
        x=[]
        for r in ans:
            x.append(r[0])
        self.cb3.config(values=x)
    def insert(self):
        s="insert into TimeTable values (NULL,'"+self.cb3.get()+"','"+self.cb4.get()+"','"+self.cb5.get()+"','"+self.txt.get()+"')"
        self.cr.execute(s)
        self.conn.commit()
        self.conn.close()
        showinfo("","timetable added")
    def __init__(self):
        self.root=Tk()

        self.lb1=Label(self.root,text="Select Programme")
        self.lb2=Label(self.root,text="Select Semester")
        self.lb3=Label(self.root,text="Select Subject Code")
        self.lb4=Label(self.root,text="Select Day Of Week")
        self.lb5=Label(self.root,text="Select Slot")
        self.lb6=Label(self.root,text="Select Teacher's Name")

        self.conn=sqlite3.connect("timetabledata.sqlite3")
        self.cr=self.conn.cursor()
        s="select degree_name from Programmes"
        self.cr.execute(s)
        ans=self.cr.fetchall()
        x=[]
        for r in ans:
            x.append(r[0])
        self.cb1=Combobox(self.root,values=x,state="readonly")
        self.cb1.bind("<<ComboboxSelected>>",self.getdata)
        self.bt1=Button(self.root,text="Add Timetable",command=self.insert).grid(row=6,column=0)
        self.cb2=Combobox(self.root,values=(1,2,3,4,5,6,7,8,9,10,11),state="readonly")
        self.cb2.bind("<<ComboboxSelected>>",self.getdata)
        self.cb3=Combobox(self.root,state='readonly')
        self.cb4=Combobox(self.root,state='readonly',values=("Monday","Tuesday","Wednesday","Thursday","Friday"))
        self.cb5=Combobox(self.root,state='readonly',values=("9:00-10:00","10:00-11:00","11:00-12:00","1:00-2:00","2:00-3:00"))
        self.txt=Entry(self.root)


        self.lb1.grid(row=0,column=0)
        self.cb1.grid(row=0,column=1)
        self.lb2.grid(row=1,column=0)
        self.cb2.grid(row=1,column=1)
        self.lb3.grid(row=2,column=0)
        self.cb3.grid(row=2,column=1)
        self.lb4.grid(row=3,column=0)
        self.cb4.grid(row=3,column=1)
        self.lb5.grid(row=4,column=0)
        self.cb5.grid(row=4,column=1)
        self.lb6.grid(row=5,column=0)
        self.txt.grid(row=5,column=1)

        self.root.mainloop()

