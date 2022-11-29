from tkinter import *
import tkinter


def tkLogin():
    tk_window = tkinter.Tk()
    tk_window.geometry('300x120')
    tk_window.title('Login Robinhood')

    Label(tk_window, text="Enter Username:").grid(row=0, column=0)
    username = StringVar()
    Entry(tk_window, textvariable=username).grid(row=0, column=1)
    Label(tk_window, text="Enter Password:").grid(row=1, column=0)
    password = StringVar()
    Entry(tk_window, textvariable=password, show='*').grid(row=1, column=1)
    Label(tk_window, text="Enter OTC:").grid(row=2, column=0)
    OTC = StringVar()
    Entry(tk_window, textvariable=OTC).grid(row=2, column=1)
    Button(tk_window, text="Login", command=tk_window.destroy).grid(row=4, column=0)
    Button(tk_window, text="Cancel", command=tk_window.destroy).grid(row=4, column=1)
    tk_window.mainloop()
    return username, password, OTC
