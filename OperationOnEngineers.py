import tkinter 
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql
from Dengineerssave import *
from Dengineersfind import *
from Dengineersupdate import *
from Dengineersdelete import *
from Dengineersshow import *
t=tkinter.Tk()
t.geometry('800x650')
t.title('Main Screen')
b1=Button(t,text='Es SAVE', command=dengineerssave, width=20)
b1.place(x=20,y=20)
b2=Button(t,text='Es FIND',command=dengineersfind,width=20)
b2.place(x=20,y=70)
b3=Button(t,text='Es UPDATE',command=dengineersupdate,width=20)
b3.place(x=20,y=120)
b4=Button(t,text='Es DELETE',command=dengineersdelete,width=20)
b4.place(x=20,y=170)
b5=Button(t,text='Es SHOW',command=dengineersshow,width=20)
b5.place(x=20,y=210)
t.mainloop()