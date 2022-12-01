import robin_connection as rc
import openbb_connection as oc
import time
from datetime import datetime


class main:
    def __init__(self):
        pass

    if __name__ == '__main__':
        threshold = 30
        steve_rc = rc.robin_connection()

        now = datetime.now()
        current_hour = int(now.strftime('%H'))

        steve_rc.robin_login(now.strftime('%H:%M:%S'))

        try:
            stock_names, exps, strikes, types = oc.getUnu(threshold)
        except:
            stock_names, exps, strikes, types = [], [], [], []

        while current_hour < 24:
            now = datetime.now()
            current_hour = int(now.strftime('%H'))
            current_min = int(now.strftime('%M'))
            print("Current Time =", now.strftime('%H:%M:%S'))
            if current_min % 30 == 0:
                stock_names, exps, strikes, types = oc.getUnu(threshold)
            if len(stock_names) == 0:
                print('********************************************************')
                print('No unusual options for now, will check 30 seconds later.')
                print('********************************************************')
            else:
                prices = steve_rc.see_a_stock(stock_names)
                for i in range(len(stock_names)):
                    print('********************************************************')
                    print(stock_names[i], exps[i], strikes[i], types[i])
                    print('Price now: ', prices[i])
                    opt_info = steve_rc.see_an_option(stock_names[i], exps[i], strikes[i], types[i])
                    print('ask price: ', opt_info[0])
                    print('bid price: ', opt_info[1])
                    print('gamma: ', opt_info[2])
                    print('implied volatility: ', opt_info[3])
                print('========================================================')
            time.sleep(30)
        now = datetime.now()
        steve_rc.robin_logout(now.strftime('%H:%M:%S'))
