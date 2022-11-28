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
        return rh.stocks.find_instrument_data(stock_name)

    def see_an_option(self):
        return rh.options.find_options_by_expiration_and_strike('TSLA', '2022-12-02', '149', 'put')
