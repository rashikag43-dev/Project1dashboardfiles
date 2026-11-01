import tkinter 
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql
from Dproductssave import *
from Dproductsfind import *
from Dproductsupdate import *
from Dproductsdelete import *
from Dproductsshow import *
t=tkinter.Tk()
t.geometry('800x650')
t.title('Main Screen')
b1=Button(t,text='Ps SAVE', command=dproductssave, width=20)
b1.place(x=20,y=20)
b2=Button(t,text='Ps FIND',command=dproductsfind,width=20)
b2.place(x=20,y=70)
b3=Button(t,text='Ps UPDATE',command=dproductsupdate,width=20)
b3.place(x=20,y=120)
b4=Button(t,text='Ps DELETE',command=dproductsdelete,width=20)
b4.place(x=20,y=170)
b5=Button(t,text='Ps SHOW',command=dproductsshow,width=20)
b5.place(x=20,y=210)
t.mainloop()