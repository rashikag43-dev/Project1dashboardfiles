
import tkinter
from tkinter import *
from tkinter import messagebox
import os
import sys

t = tkinter.Tk()
t.geometry('700x700')
t.title('Samsung Service Centre Login')
t.configure(bg='#EAF2F8')
t.resizable(False, False)


def login():

    username = e1.get()
    password = e2.get()

    if username == 'admin' and password == '1234':

        try:
            project_path = os.path.dirname(os.path.abspath(__file__))

            if project_path not in sys.path:
                sys.path.insert(0, project_path)

            from Dashboard import open_dashboard

            open_dashboard(t)

        except Exception as error:
            messagebox.showerror(
                'Dashboard Error',
                str(error),
                parent=t
            )

    else:
        messagebox.showerror(
            'Login Error',
            'Invalid Username or Password',
            parent=t
        )


Label(
    t,
    text='SAMSUNG SERVICE CENTRE',
    font=('Arial', 17, 'bold'),
    bg='#1B365D',
    fg='white',
    pady=20
).pack(fill=X)

Label(
    t,
    text='LOGIN',
    font=('Arial', 22, 'bold'),
    bg='#EAF2F8'
).place(x=155, y=100)

Label(
    t,
    text='Username',
    font=('Arial', 11),
    bg='#EAF2F8'
).place(x=45, y=165)

e1 = Entry(t, font=('Arial', 11))
e1.place(x=150, y=165, width=180)

Label(
    t,
    text='Password',
    font=('Arial', 11),
    bg='#EAF2F8'
).place(x=45, y=215)

e2 = Entry(t, font=('Arial', 11), show='*')
e2.place(x=150, y=215, width=180)

Button(
    t,
    text='LOGIN',
    command=login,
    font=('Arial', 11, 'bold'),
    bg='#1B65A7',
    fg='white',
    width=12
).place(x=145, y=275)

t.mainloop()
