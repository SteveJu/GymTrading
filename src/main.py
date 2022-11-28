import robin_connection as rc
import openbb_connection as oc
import time
from datetime import datetime


class main:

    def go(Name):
        steve_rc = rc.robin_connection(Name)
        steve_rc.robin_login('')

        now = datetime.now()
        current_time = now.strftime('%H')

        steve_oc = oc.openbb_connection()
        stock_names, exps, strikes, types = steve_oc.getUnu(30)

        while int(current_time) < 16:
            now = datetime.now()
            print("Current Time =", now.strftime('%H:%M:%S'))
            for i in range(len(stock_names)):
                print('********************************************************')
                print(stock_names[i], exps[i], strikes[i], types[i])
                price = steve_rc.see_a_stock(stock_names[i])
                steve_rc.see_an_option(stock_names[i], exps[i], strikes[i], types[i])
            time.sleep(30)
            print('-----------------------------------------------------------------')

    if __name__ == '__main__':
        go('Steve')
