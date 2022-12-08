import robin_connection as rc
import openbb_connection as oc
import simulator as sim
import time_system as ts
import models as models
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
                    Stock_Price = round(float(prices[i]), 2)
                    Stock_Name = stock_names[i]
                    Expiration_Date = exps[i]
                    Strike = strikes[i]
                    Opt_Type = types[i]
                    Opt_Info = steve_rc.see_an_option(stock_names[i], exps[i], strikes[i], types[i])
                    Ask_Price = round(float(Opt_Info[0]), 2)
                    Bid_Price = round(float(Opt_Info[1]), 2)
                    Trading_Cost = round(Ask_Price - Bid_Price, 2)
                    Gamma = float(Opt_Info[2])
                    Implied_Volatility = float(Opt_Info[3])
                    Time_To_Exp = time_sys.getTimeToExp(Opt_Info[4])
                    ifCall = True
                    if types[i] == 'Put':
                        ifCall = False
                    m = models.models(ifCall, Stock_Price, Strike, Time_To_Exp, 0.04, Implied_Volatility, 1.0, Gamma)
                    Cal_Price = m.JumpDiffusion()
                    print('**************************************************No.', i + 1, '***')
                    print(stock_names[i], exps[i], strikes[i], types[i])
                    print('Price now: ', Stock_Price)
                    print('ask price: ', Ask_Price)
                    print('bid price: ', Bid_Price)
                    print('Trading cost: ', Trading_Cost)
                    print('gamma: ', Gamma)
                    print('implied volatility: ', Implied_Volatility)
                    print('Time to EXP: ', Time_To_Exp)
                    print('Calculated Price: ', Cal_Price)
                print('==========================Section==========================')
            time.sleep(30)
        steve_rc.robin_logout(time_sys.getFullDateAndTime())
