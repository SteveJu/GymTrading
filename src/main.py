import robin_connection as rc
import time
from datetime import datetime


class main:
    def go(Name):
        steve_rc = rc.robin_connection(Name)
        steve_rc.robin_login('')
        stock_name = 'GM'
        now = datetime.now()
        current_time = now.strftime('%H')

        while int(current_time) < 15:
            now = datetime.now()
            print("Current Time =", now.strftime('%H:%M:%S'))
            price = steve_rc.see_a_stock(stock_name)
            steve_rc.see_an_option(stock_name, '2023-03-17', '18', 'put')
            time.sleep(30)
            print('-----------------------------------------------------------------')

    if __name__ == '__main__':
        go('Steve')
