import robin_stocks as rh


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
        login = rh.robinhood.login(self.robinhood_username, self.robinhood_passcode, self.robinhood_OTC)

    def see_full_profile(self):
        return rh.robinhood.profiles.load_account_profile()

    def see_simple_profile(self):
        return rh.robinhood.profiles.load_basic_profile()
