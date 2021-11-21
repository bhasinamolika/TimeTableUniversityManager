import sqlite3
from tkinter import *
from tkinter.ttk import *
class view_program:
    def __init__(self):
        self.root=Tk()
        self.t1=Treeview(self.root,columns=('degree','desc'))
        self.t1.heading('degree',text="Degree name")
        self.t1.heading('desc',text="Description")

        self.t1["show"]="headings"


        conn=sqlite3.connect("timetabledata.sqlite3")
        cr=conn.cursor()


        s="select * from programmes"
        cr.execute(s)
        ans=cr.fetchall()
        i=0
        for r in ans:
            self.t1.insert("",index=i,values=r)
            i+=1

        self.t1.pack()
        self.root.mainloop()

