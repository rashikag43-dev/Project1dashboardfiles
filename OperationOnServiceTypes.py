import tkinter 
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql
from Dservicetypessave import *
from Dservicetypesfind import *
from Dservicetypesupdate import *
from Dservicetypesdelete import *
from Dservicetypesshow import *
t=tkinter.Tk()
t.geometry('800x650')
t.title('Main Screen')
b1=Button(t,text='ST SAVE', command=dservicetypessave, width=20)
b1.place(x=20,y=20)
b2=Button(t,text='ST FIND',command=dservicetypesfind,width=20)
b2.place(x=20,y=70)
b3=Button(t,text='ST UPDATE',command=dservicetypesupdate,width=20)
b3.place(x=20,y=120)
b4=Button(t,text='ST DELETE',command=dservicetypesdelete,width=20)
b4.place(x=20,y=170)
b5=Button(t,text='ST SHOW',command=dservicetypesshow,width=20)
b5.place(x=20,y=210)
t.mainloop()