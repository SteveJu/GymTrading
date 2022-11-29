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

        now = datetime.now()
        current_time = now.strftime('%H')

        steve_rc.robin_login(now.strftime('%H:%M:%S'))

        while int(current_time) < 24:
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
                    opt_info = steve_rc.see_an_option(stock_names[i], exps[i], strikes[i], types[i])
                    print('ask price: ', opt_info[0])
                    print('bid price: ', opt_info[1])
                    print('gamma: ', opt_info[2])
                    print('implied volatility: ', opt_info[3])
                print('-----------------------------------------------------------------')
            time.sleep(30)
        now = datetime.now()
        steve_rc.robin_logout(now.strftime('%H:%M:%S'))
