import sqlite3
from tkinter import *
from tkinter.messagebox import showerror, showinfo
from tkinter.ttk import Combobox



class test:


    conn=sqlite3.connect("timetabledata.sqlite3")



    def save(self):
        ans=self.cr.fetchall()
        flag= False
        for r in self.ans:
            if str(r[0]).upper()==self.txt2.get().upper:
                flag=True
                break
        if flag==True:
            showinfo("","Duplicate Course Name")
        elif self.txt2.get()=="" or self.txt3.get()=="":
            showerror("","Please Fill The Record")
        else:

            cr = self.conn.cursor()
            s = "insert into programmes values ('" +self.txt2.get()+ "','" + self.txt3.get() + "')"

            self.cr.execute(s)
            self.conn.commit()
            showinfo("", "Record Added Successfully")


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




        self.lb3 = Label(self.root, text="Add Programme Name")
        self.lb4 = Label(self.root, text="Add Description")
        self.bt3 = Button(self.root, text='Save',command=self.save)
        self.txt2=Entry(self.root)
        self.txt3=Entry(self.root)



        self.lb3.grid(row=3,column=0)
        self.lb4.grid(row=4,column=0)
        self.txt2.grid(row=3,column=1)
        self.txt3.grid(row=4,column=1)
        self.bt3.grid(row=5,column=1)

        self.root.mainloop()
