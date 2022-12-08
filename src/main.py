import robin_connection as rc
import openbb_connection as oc
import simulator as sim
import time_system as ts
import time


class main:
    def __init__(self):
        pass

    if __name__ == '__main__':
        threshold = 20
        steve_rc = rc.robin_connection()

        time_sys = ts.time_system()
        current_hour = time_sys.getHour()

        steve_rc.robin_login(time_sys.getFullDateAndTime())

        try:
            stock_names, exps, strikes, types = oc.getUnu(threshold)
        except:
            stock_names, exps, strikes, types = [], [], [], []

        while current_hour < 24:
            current_hour = time_sys.getHour()
            current_min = time_sys.getMin()
            current_time = time_sys.getFullDateAndTime()
            print("Current Time =", current_time)

            curr_info = sim.readCurrent()
            curr_depo = sim.getCurrAsset(curr_info)
            print('Current Deposit: ', curr_depo)

            if current_min % 30 == 0:
                stock_names, exps, strikes, types = oc.getUnu(threshold)
            if len(stock_names) == 0:
                print('*********************************************************')
                print('No unusual options for now, will check 30 seconds later.')
                print('*********************************************************')
            else:
                prices = steve_rc.see_a_stock(stock_names)
                for i in range(len(stock_names)):
                    print('**************************************************No.', i+1, '***')
                    print(stock_names[i], exps[i], strikes[i], types[i])
                    print('Price now: ', round(float(prices[i]), 2))
                    opt_info = steve_rc.see_an_option(stock_names[i], exps[i], strikes[i], types[i])
                    ask_price = round(float(opt_info[0]), 2)
                    bid_price = round(float(opt_info[1]), 2)
                    print('ask price: ', ask_price)
                    print('bid price: ', bid_price)
                    print('Trading cost: ', round(ask_price - bid_price, 2))
                    print('gamma: ', opt_info[2])
                    print('implied volatility: ', opt_info[3])
                    print('sellout datetime: ', opt_info[4])
                print('==========================Section==========================')
            time.sleep(30)
        steve_rc.robin_logout(time_sys.getFullDateAndTime())
