import sqlite3
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import *
import sqlite3
class edittimetable:
    def getdata(self,d):
        s = "select * from TimeTable,subjects where subjects.subject_code=TimeTable.subject_code and subjects.degree_name='" + self.cb1.get() + "' and subjects.semester='"+self.cb2.get()+"' "
        self.cr.execute(s)
        self.ans = self.cr.fetchall()
        x = ["Select Teachername"]
        for r in self.ans:
            x.append(r[4])
        self.cb3.config(values=x)
    def getdata2(self,d):
        h="select Slot,day_week from TimeTable where Teachername='"+self.cb3.get()+"'"
        self.cr.execute(h)
        ans2=self.cr.fetchall()
        a=["select Slot"]
        for r in ans2:
            a.append(r[0])
        self.cb4.config(values=a)
        b=["Select Day"]
        for r in ans2:
            b.append(r[1])
        self.cb5.config(values=b)
    def delete(self):
        c="delete from TimeTable where Teachername='"+self.cb3.get()+"' and Slot='"+self.cb4.get()+"' and day_week='"+self.cb5.get()+"'"
        self.cr.execute(c)
        self.conn.commit()
        showinfo("","TimeTable deleted")
    def edit(self):
        d="update TimeTable set Teachername='"+self.txt.get()+"' where Teachername='"+self.cb3.get()+"'"
        self.cr.execute(d)
        self.conn.commit()
        showinfo("","Teacher Changed")
    def __init__(self):
        self.root=Tk()
        self.root.geometry("400x400")
        self.lb1=Label(self.root,text="Select Degreename")
        self.lb2=Label(self.root,text="Select Semester")
        self.lb3=Label(self.root,text="Select Teacher Name")
        self.lb4=Label(self.root,text="Select Slot")
        self.lb5=Label(self.root,text="Select Day Of Week")
        self.lb6=Label(self.root,text="Enter New Teachername")
        self.txt=Entry(self.root)
        self.bt1=Button(self.root,text="Change Teacher",command=self.edit)
        self.conn=sqlite3.connect("timetabledata.sqlite3")
        self.cr=self.conn.cursor()
        s="select * from Programmes"
        self.cr.execute(s)
        ans=self.cr.fetchall()
        p=[]
        for r in ans:
           p.append(r[0])
        self.cb1=Combobox(self.root,values=p,state='readonly')
        self.cb2=Combobox(self.root,values=(1,2,3,4,5,6,7,8,9,10,11),state='readonly')
        self.cb1.bind("<<ComboboxSelected>>",self.getdata)
        self.cb2.bind("<<ComboboxSelected>>",self.getdata)
        self.cb3=Combobox(self.root,state='readonly')
        self.cb3.bind("<<ComboboxSelected>>",self.getdata2)
        self.cb4=Combobox(self.root,state='readonly')
        self.cb5=Combobox(self.root,state='readonly')
        self.bt=Button(self.root,text="Delete",command=self.delete)
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
        self.bt.grid(row=5,column=1)
        self.lb6.grid(row=6,column=0)
        self.txt.grid(row=6,column=1)
        self.bt1.grid(row=7,column=1)

        self.root.mainloop()
