import sqlite3
from tkinter import *
from tkinter.ttk import Treeview, Combobox
class view:
    def fire(self):
        for i in self.t1.get_children():
            self.t1.delete(i)
        s="select subject_code,subject_name,degree_name,semester from subjects"
        self.cr.execute(s)
        ans=self.cr.fetchall()
        x = []
        y = []
        z = []
        p = []
        t = []
        for row in ans:
            if self.cb1.get()==row[2] and int(self.cb2.get())==row[3]:
                sc=row[0]
                sn=row[1]
                n = "select subject_code,Teachername,day_week,slot from TimeTable where subject_code='"+str(sc)+"'"
                ct = self.conn.cursor()
                ct.execute(n)
                ans2 = ct.fetchall()
                i=0
                for r in ans2:
                    if r[2]=="Monday":
                        x.append(sc)
                        x.append(sn)
                        x.append(r[1])
                        y=z=p=t=[]
                    elif r[2]=="Tuesday":
                        y.append(sc)
                        y.append(sn)
                        y.append(r[1])
                        x=z=p=t=[]
                    elif r[2]=="Wednesday":
                        z.append(sc)
                        z.append(sn)
                        z.append(r[1])
                        x=y=p=t=[]
                    elif r[2]=="Thursday":
                        p.append(sc)
                        p.append(sn)
                        p.append(r[1])
                        x=y=z=t=[]
                    elif r[2]=="Friday":
                        t.append(sc)
                        t.append(sn)
                        t.append(r[1])
                        x=y=z=p=[]
                    self.t1.insert("",index=i,values=(r[3],x,y,z,p,t))
                    i+=1
    def __init__(self):
        self.conn = sqlite3.connect("timetabledata.sqlite3")
        self.cr = self.conn.cursor()
        s = "select degree_name from Programmes"
        self.cr.execute(s)
        ans = self.cr.fetchall()
        x = []
        for r in ans:
            x.append(r[0])
        self.root=Tk()
        self.p1=PanedWindow(self.root)
        self.p2=PanedWindow(self.root)
        self.bt1=Button(self.p1,text="submit",command=self.fire).grid(row=0,column=4)
        self.lb1=Label(self.p1,text ="Enter Degree Name")
        self.lb2=Label(self.p1,text ="Enter Semester")
        self.cb1=Combobox(self.p1,values=x,state='readonly')
        self.cb2=Combobox(self.p1,values=(1,2,3,4,5,6,7,8,9,10,11),state='readonly')
        self.lb1.grid(row=0,column=0)
        self.lb2.grid(row=0,column=2)
        self.cb1.grid(row=0,column=1)
        self.cb2.grid(row=0,column=3)
        self.t1=Treeview(self.p2,columns=("slot","mon","tues","wed","thurs","fri"))
        self.t1.heading("slot",text="Slots")
        self.t1.heading("mon",text="Monday")
        self.t1.heading("tues",text="Tuesday")
        self.t1.heading("wed",text="Wednesday")
        self.t1.heading("thurs",text="Thursday")
        self.t1.heading("fri",text="Friday")
        self.t1["show"]="headings"
        self.t1.pack()
        self.p1.pack()
        self.p2.pack()
        self.root.mainloop()
obj=view()