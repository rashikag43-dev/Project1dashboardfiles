import tkinter 
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql
from Dcallclosedatasave import *
from Dcallclosedatafind import *
from Dcallclosedataupdate import *
from Dcallclosedatadelete import *
from Dcallclosedatashow import *
t=tkinter.Tk()
t.geometry('800x650')
t.title('Main Screen')
b1=Button(t,text='CCD SAVE', command=dcallclosedatasave, width=20)
b1.place(x=20,y=20)
b2=Button(t,text='CCD FIND',command=dcallclosedatafind,width=20)
b2.place(x=20,y=70)
b3=Button(t,text='CCD UPDATE',command=dcallclosedataupdate,width=20)
b3.place(x=20,y=120)
b4=Button(t,text='CCD DELETE',command=dcallclosedatadelete,width=20)
b4.place(x=20,y=170)
b5=Button(t,text='CCD SHOW',command=dcallclosedatashow,width=20)
b5.place(x=20,y=210)
t.mainloop()