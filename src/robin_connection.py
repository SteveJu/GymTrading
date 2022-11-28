import tkinter.simpledialog

import robin_stocks.robinhood as rh
from tkinter import *


class robin_connection:
    def __init__(self):
        tkWindow = tkinter.Tk()
        tkWindow.geometry('250x100')
        tkWindow.title('Login Robinhood')

        Label(tkWindow, text="Enter Username:").grid(row=0, column=0)
        username = StringVar()
        username.set('steveju546@gmail.com')
        Entry(tkWindow, textvariable=username).grid(row=0, column=1)
        Label(tkWindow, text="Enter Password:").grid(row=1, column=0)
        password = StringVar()
        Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)
        Label(tkWindow, text="Enter OTC:").grid(row=2, column=0)
        OTC = StringVar()
        Entry(tkWindow, textvariable=OTC).grid(row=2, column=1)
        Button(tkWindow, text="Login", command=tkWindow.destroy).grid(row=4, column=0)
        Button(tkWindow, text="Cancel", command=tkWindow.destroy).grid(row=4, column=1)
        tkWindow.mainloop()

        self.robinhood_username = username.get()
        self.robinhood_passcode = password.get()
        self.robinhood_OTC = OTC.get()

    def robin_login(self):
        login = rh.login(self.robinhood_username, self.robinhood_passcode, self.robinhood_OTC)

    def see_a_stock(self, stock_names):
        target = rh.stocks.get_latest_price(stock_names)
        # print('Price Now: ', target[0])
        return target

    def see_an_option(self, option_name, ex_date, strike, types):
        target = rh.options.find_options_by_expiration_and_strike(option_name, ex_date, strike, types)
        for item in target:
            print('ask_price: ', item['ask_price'])
            print('bid_price: ', item['bid_price'])
            print('gamma: ', item['gamma'])
            print('implied_volatility: ', item['implied_volatility'])
        return
