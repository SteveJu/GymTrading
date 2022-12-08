import robin_stocks.robinhood as rh
import login


def robin_logout(time):
    rh.logout()
    print('Logged out at', time)


def see_a_stock(stock_names):
    target = rh.stocks.get_latest_price(stock_names)
    return target


def see_an_option(option_name, ex_date, strike, types):
    target = rh.options.find_options_by_expiration_and_strike(option_name, ex_date, strike, types)
    item = target[0]
    return [item['ask_price'], item['bid_price'], item['gamma'], item['implied_volatility'], item['sellout_datetime']]


class robin_connection:
    def __init__(self):
        username, password, OTC = login.tkLogin()
        self.robinhood_username = username.get()
        self.robinhood_passcode = password.get()
        self.robinhood_OTC = OTC.get()

    def robin_login(self, time):
        rh.login(self.robinhood_username, self.robinhood_passcode, self.robinhood_OTC)
        print('Logged in at', time)

