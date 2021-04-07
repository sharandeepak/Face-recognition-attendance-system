
from tkinter import *
import os
from datetime import datetime
import eel
import dataset_capture2
import train_dataset_new
import offline_records

eel.init('assets')


@eel.expose
def dummy(dummy_param):
    print('i got a parameter'+dummy_param)
    return "String_value", 1, 1.2, True, [1, 2, 3, 4], {"name": "eel"}

# root=Tk()

# root.configure(background="white")


@eel.expose
def capture_dataset(uid, name):
    dataset_capture2.clickfun(uid, name)


@eel.expose
def train_dataset():
    if train_dataset_new.train_model() == 2:
        return 3


@eel.expose
def take_attendance():
    offline_records.qr()


@eel.expose
def open_workbook2():
    os.startfile('Attendance Report.xlsx')


@eel.expose
def Manual_Entry(uin):
    print("uin"+uin)
    offline_records.facee(uin)

@eel.expose
def Save_Attendance():
    if offline_records.readFromdb()==2:
        return 3


eel.start('/index.html')
input()


# def function4():

#     root.destroy()


# root.title("Intelligent attendance system ")

# Label(root, text="ATTENDANCE SYSTEM",font=("times new roman",30),fg="white",bg="purple",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

# Button(root,text="Create Dataset",font=("times new roman",30),bg="#0D47A2",fg='white',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

# Button(root,text="Train Dataset",font=("times new roman",30),bg="#0D47A1",fg='white',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

# Button(root,text="Take Attendance`",font=('times new roman',30),bg="#0D47A1",fg="white",command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

# Button(root,text="Attendance Sheet",font=('times new roman',30),bg="#0D47A1",fg="white",command=attend).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

# Button(root,text="Exit",font=('times new roman',20),bg="red",fg="white",command=function4).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


# root.mainloop()
