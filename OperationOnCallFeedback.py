import tkinter 
from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import pymysql
from Dcallfeedbacksave import *
from Dcallfeedbackfind import *
from Dcallfeedbackupdate import *
from Dcallfeedbackdelete import *
from Dcallfeedbackshow import *
t=tkinter.Tk()
t.geometry('800x650')
t.title('Main Screen')
b1=Button(t,text='CF SAVE', command=dcallfeedbacksave, width=20)
b1.place(x=20,y=20)
b2=Button(t,text='CF FIND',command=dcallfeedbackfind,width=20)
b2.place(x=20,y=70)
b3=Button(t,text='CF UPDATE',command=dcallfeedbackupdate,width=20)
b3.place(x=20,y=120)
b4=Button(t,text='CF DELETE',command=dcallfeedbackdelete,width=20)
b4.place(x=20,y=170)
b5=Button(t,text='CF SHOW',command=dcallfeedbackshow,width=20)
b5.place(x=20,y=210)
t.mainloop()