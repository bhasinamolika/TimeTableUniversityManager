import sqlite3
from tkinter import *
from tkinter.ttk import Treeview, Combobox
class view:
    def fire(self):
        for i in self.t1.get_children():
            self.t1.delete(i)
        slot1=["9:00-10:00"]
        days=["Monday","Tuesday","Wednesday","Thursday","Friday"]
        for day in days:
            n="select TimeTable.Teachername, TimeTable.subject_code, subjects.subject_name, TimeTable.day_week from TimeTable, subjects where subjects.subject_code = TimeTable.subject_code and TimeTable.Slot='9:00-10:00' and subjects.degree_name='"+self.cb1.get()+"' and subjects.semester='"+str(self.cb2.get())+"' and TimeTable.day_week='"+day+"'"
            self.cr.execute(n)
            ans=self.cr.fetchone()

            if ans!=None:
                slot1.append(str(ans[0])+","+str(ans[1])+","+str(ans[2]))
            else:
                slot1.append("Free Lecture")
        self.t1.insert("",index=0,values=slot1)
        slot2 = ["10:00-11:00"]
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        for day in days:
            n = "select TimeTable.Teachername, TimeTable.subject_code, subjects.subject_name, TimeTable.day_week from TimeTable, subjects where subjects.subject_code = TimeTable.subject_code and TimeTable.Slot='10:00-11:00' and subjects.degree_name='" + self.cb1.get() + "' and subjects.semester='" + str(
                self.cb2.get()) + "' and TimeTable.day_week='" + day + "'"
            self.cr.execute(n)
            ans = self.cr.fetchone()

            if ans != None:
                slot2.append(str(ans[0]) + "," + str(ans[1]) + "," + str(ans[2]))
            else:
                slot2.append("Free Lecture")
        self.t1.insert("", index=1, values=slot2)
        slot3 = ["11:00-12:00"]
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        for day in days:
            n = "select TimeTable.Teachername, TimeTable.subject_code, subjects.subject_name, TimeTable.day_week from TimeTable, subjects where subjects.subject_code = TimeTable.subject_code and TimeTable.Slot='11:00-12:00' and subjects.degree_name='" + self.cb1.get() + "' and subjects.semester='" + str(
                self.cb2.get()) + "' and TimeTable.day_week='" + day + "'"
            self.cr.execute(n)
            ans = self.cr.fetchone()

            if ans != None:
                slot3.append(str(ans[0]) + "," + str(ans[1]) + "," + str(ans[2]))
            else:
                slot3.append("Free Lecture")
        self.t1.insert("", index=2, values=slot3)
        slot4 = ["1:00-2:00"]
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        for day in days:
            n = "select TimeTable.Teachername, TimeTable.subject_code, subjects.subject_name, TimeTable.day_week from TimeTable, subjects where subjects.subject_code = TimeTable.subject_code and TimeTable.Slot='1:00-2:00' and subjects.degree_name='" + self.cb1.get() + "' and subjects.semester='" + str(
                self.cb2.get()) + "' and TimeTable.day_week='" + day + "'"
            self.cr.execute(n)
            ans = self.cr.fetchone()

            if ans != None:
                slot4.append(str(ans[0]) + "," + str(ans[1]) + "," + str(ans[2]))
            else:
                slot4.append("Free Lecture")
        self.t1.insert("", index=3, values=slot4)
        slot5 = ["2:00-3:00"]
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        for day in days:
            n = "select TimeTable.Teachername, TimeTable.subject_code, subjects.subject_name, TimeTable.day_week from TimeTable, subjects where subjects.subject_code = TimeTable.subject_code and TimeTable.Slot='2:00-3:00' and subjects.degree_name='" + self.cb1.get() + "' and subjects.semester='" + str(
                self.cb2.get()) + "' and TimeTable.day_week='" + day + "'"
            self.cr.execute(n)
            ans = self.cr.fetchone()

            if ans != None:
                slot5.append(str(ans[0]) + "," + str(ans[1]) + "," + str(ans[2]))
            else:
                slot5.append("Free Lecture")
        self.t1.insert("", index=4, values=slot5)

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
