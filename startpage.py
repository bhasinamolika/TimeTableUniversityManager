from tkinter import *
import addtimetable
import viewtimetable
import viewsubjects
import addsubjects
import demo
import editcourse
import viewcourse
import editsubjects
import edittimetable
class start:
    def fire1(self):
        obj=addtimetable.addtimetable()
    def fire2(self):
        obj=viewtimetable.view()
    def fire3(self):
        obj=edittimetable.edittimetable()
    def fire4(self):
        obj=viewsubjects.view()
    def fire5(self):
        obj=addsubjects.addsub()
    def fire6(self):
        obj=editsubjects.demo()
    def fire7(self):
        obj=demo.test()
    def fire8(self):
        obj=editcourse.editcourse()
    def fire9(self):
        obj=viewcourse.view_program()
    def __init__(self):
        self.root=Tk()
        self.root.geometry("1080x1080")
        self.mymenu=Menu(self.root)
        self.root.title("TimeTable Management")
        self.root.config(menu=self.mymenu)
        self.submenu1=Menu(self.mymenu,tearoff=False)
        self.mymenu.add_cascade(label="Manage Course",menu=self.submenu1)
        self.submenu1.add_command(label="Add New Course",command=self.fire7)
        self.submenu1.add_command(label="View All Courses",command=self.fire9)
        self.submenu1.add_command(label="Edit/Delete Course",command=self.fire8)

        self.submenu2 = Menu(self.mymenu, tearoff=False)
        self.mymenu.add_cascade(label="Manage Subjects", menu=self.submenu2)
        self.submenu2.add_command(label="Add New Subjects",command=self.fire5)
        self.submenu2.add_command(label="View All Subjects",command=self.fire4)
        self.submenu2.add_command(label="Edit/Delete Subjects",command=self.fire6)

        self.submenu3 = Menu(self.mymenu, tearoff=False)
        self.mymenu.add_cascade(label="Manage TimeTable", menu=self.submenu3)
        self.submenu3.add_command(label="Add New TimeTable",command=self.fire1)
        self.submenu3.add_command(label="View TimeTable",command=self.fire2)
        self.submenu3.add_command(label="Edit/Delete TimeTable",command=self.fire3)
        self.root.mainloop()
obj=start()