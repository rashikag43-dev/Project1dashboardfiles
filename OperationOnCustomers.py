import tkinter 
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql
from Dcustomerssavee import *
from Dcustomersfindd import *
from Dcustomersupdatee import *
from Dcustomersdelet import *
from Dcustomersshoww import *
t=tkinter.Tk()
t.geometry('800x650')
t.title('Main Screen')
b1=Button(t,text='Cs SAVE', command=dcustomerssavee, width=20)
b1.place(x=20,y=20)
b2=Button(t,text='Cs FIND',command=dcustomersfindd,width=20)
b2.place(x=20,y=70)
b3=Button(t,text='Cs UPDATE',command=dcustomersupdatee,width=20)
b3.place(x=20,y=120)
b4=Button(t,text='Cs DELETE',command=dcustomersdeletee,width=20)
b4.place(x=20,y=170)
b5=Button(t,text='Cs SHOW',command=dcustomersshoww,width=20)
b5.place(x=20,y=210)
t.mainloop()