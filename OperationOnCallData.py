import tkinter 
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql
from Dcalldatasave import *
from Dcalldatafind import *
from Dcalldataupdate import *
from Dcalldatadelete import *
from Dcalldatashow import *
t=tkinter.Tk()
t.geometry('800x650')
t.title('Main Screen')
b1=Button(t,text='CD SAVE', command=dcalldatasave, width=20)
b1.place(x=20,y=20)
b2=Button(t,text='CD FIND',command=dcalldatafind,width=20)
b2.place(x=20,y=70)
b3=Button(t,text='CD UPDATE',command=dcalldataupdate,width=20)
b3.place(x=20,y=120)
b4=Button(t,text='CD DELETE',command=dcalldatadelete,width=20)
b4.place(x=20,y=170)
b5=Button(t,text='CD SHOW',command=dcalldatashow,width=20)
b5.place(x=20,y=210)
t.mainloop()