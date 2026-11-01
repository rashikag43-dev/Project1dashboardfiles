import tkinter 
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql
from Dservicecentresave import *
from Dservicecentrefind import *
from Dservicecentreupdate import *
from Dservicecentredelete import *
from Dservicecentreshow import *
t=tkinter.Tk()
t.geometry('800x650')
t.title('Main Screen')
b1=Button(t,text='SC SAVE', command=dservicecentresave, width=20)
b1.place(x=20,y=20)
b2=Button(t,text='SC FIND',command=dservicecentrefind,width=20)
b2.place(x=20,y=70)
b3=Button(t,text='SC UPDATE',command=dservicecentreupdate,width=20)
b3.place(x=20,y=120)
b4=Button(t,text='SC DELETE',command=dservicecentredelete,width=20)
b4.place(x=20,y=170)
b5=Button(t,text='SC SHOW',command=dservicecentreshow,width=20)
b5.place(x=20,y=210)
t.mainloop()