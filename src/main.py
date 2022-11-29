import robin_connection as rc
import openbb_connection as oc
import time
from datetime import datetime


class main:
    def __init__(self):
        pass

    if __name__ == '__main__':
        threshold = 40
        steve_rc = rc.robin_connection()
        steve_oc = oc.openbb_connection()

        steve_rc.robin_login()

        now = datetime.now()
        current_time = now.strftime('%H')

        while int(current_time) < 19:
            now = datetime.now()
            current_time = now.strftime('%H')
            print("Current Time =", now.strftime('%H:%M:%S'))
            stock_names, exps, strikes, types = steve_oc.getUnu(threshold)
            prices = steve_rc.see_a_stock(stock_names)
            if len(stock_names) == 0:
                print('No unusual options for now, will check 30 seconds later.')
            else:
                for i in range(len(stock_names)):
                    print('********************************************************')
                    print(stock_names[i], exps[i], strikes[i], types[i])
                    print('Price now: ', prices[i])
                    steve_rc.see_an_option(stock_names[i], exps[i], strikes[i], types[i])
                print('-----------------------------------------------------------------')
            time.sleep(30)

        steve_rc.robin_logout()
