import tkinter 
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql
from Dproductcategorysave import *
from Dproductcategoryfind import *
from Dproductcategoryupdate import *
from Dproductcategorydelete import *
from Dproductcategoryshow import *
t=tkinter.Tk()
t.geometry('800x650')
t.title('Main Screen')
b1=Button(t,text='PC SAVE', command=dproductcategorysave, width=20)
b1.place(x=20,y=20)
b2=Button(t,text='PC FIND',command=dproductcategoryfind,width=20)
b2.place(x=20,y=70)
b3=Button(t,text='PC UPDATE',command=dproductcategoryupdate,width=20)
b3.place(x=20,y=120)
b4=Button(t,text='PC DELETE',command=dproductcategorydelete,width=20)
b4.place(x=20,y=170)
b5=Button(t,text='PC SHOW',command=dproductcategoryshow,width=20)
b5.place(x=20,y=210)
t.mainloop()