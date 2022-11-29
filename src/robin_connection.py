import tkinter.simpledialog

import robin_stocks.robinhood as rh
from tkinter import *


class robin_connection:
    def __init__(self):
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

        self.robinhood_username = username.get()
        self.robinhood_passcode = password.get()
        self.robinhood_OTC = OTC.get()

    def robin_login(self, time):
        login = rh.login(self.robinhood_username, self.robinhood_passcode, self.robinhood_OTC)
        print('Logged in at', time)

    def robin_logout(self, time):
        rh.logout()
        print('Logged out at', time)

    def see_a_stock(self, stock_names):
        target = rh.stocks.get_latest_price(stock_names)
        return target

    def see_an_option(self, option_name, ex_date, strike, types):
        target = rh.options.find_options_by_expiration_and_strike(option_name, ex_date, strike, types)
        item = target[0]
        return [item['ask_price'], item['bid_price'], item['gamma'], item['implied_volatility']]
