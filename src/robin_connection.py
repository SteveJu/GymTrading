import robin_stocks.robinhood as rh


class robin_connection:
    def __init__(self, name):
        if name == 'Steve':
            self.robinhood_username = 'steveju546@gmail.com'
            self.robinhood_passcode = 'Stevejuju546@'
            self.robinhood_OTC = ''  # ask Steve for one time code
        else:
            self.robinhood_username = ''
            self.robinhood_passcode = ''
            self.robinhood_OTC = ''

    def robin_login(self, otc):
        self.robinhood_OTC = otc
        login = rh.login(self.robinhood_username, self.robinhood_passcode, self.robinhood_OTC)

    def see_full_profile(self):
        return rh.profiles.load_account_profile()

    def see_simple_profile(self):
        return rh.profiles.load_basic_profile()

    def see_a_stock(self, stock_name):
        target = rh.stocks.get_latest_price(stock_name)
        print('Price Now: ', target[0])
        return target

    def see_an_option(self, option_name, ex_date, strike, type):
        target = rh.options.find_options_by_expiration_and_strike(option_name, ex_date, strike, type)
        for item in target:
            print('ask_price: ', item['ask_price'])
            print('bid_price: ', item['bid_price'])
            print('gamma: ', item['gamma'])
            print('implied_volatility: ', item['implied_volatility'])
        return
