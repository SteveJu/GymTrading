import robin_connection as rc
import openbb_connection as oc
import simulator as sim
import time_system as ts
import models as ms
import printing_system as ps
import asset_management as am

import time


class main:
    def __init__(self):
        pass

    if __name__ == '__main__':
        # Set parameters manually
        threshold = 20
        profit_space = 0.3
        interest_rate = 0.04
        lamb = 1.0

        # Open classes
        print_sys = ps.print_system()
        time_sys = ts.time_system()
        steve_rc = rc.robin_connection()

        # Login and initialize
        current_hour = time_sys.getHour()
        steve_rc.robin_login(time_sys.getFullDateAndTime())
        stock_names, exps, strikes, types = [], [], [], []

        # Main loop
        while current_hour < 24:
            current_hour = time_sys.getHour()
            current_min = time_sys.getMin()
            print_sys.printCurrTime()

            curr_info = sim.readCurrent()
            curr_depo = sim.getCurrDepo(curr_info)
            print_sys.printCurrDepo(curr_depo)

            assets = sim.getCurrAsset(curr_info)
            print_sys.printAssets(assets)
            am.ifSell(assets)
            if current_min % 30 == 0 or len(stock_names) == 0:
                stock_names, exps, strikes, types = oc.getUnu(threshold)
            if len(stock_names) == 0 and assets == ['None']:
                print_sys.printEmpty()
                time.sleep(1766)
            elif len(stock_names) == 0:
                print_sys.printAssets(assets)
                am.ifSell(assets)
                print_sys.printEmpty()
            else:
                print_sys.printSection()
                prices = rc.see_a_stock(stock_names)
                for i in range(len(stock_names)):
                    Stock_Name = stock_names[i]
                    Stock_Price = round(float(prices[i]), 2)
                    Expiration_Date = exps[i]
                    Strike = strikes[i]
                    Opr_Type = types[i]
                    Opt_Info = rc.see_an_option(stock_names[i], exps[i], strikes[i], types[i])
                    if not Opt_Info:
                        continue
                    Ask_Price = round(float(Opt_Info[0]), 2)
                    Bid_Price = round(float(Opt_Info[1]), 2)
                    Trading_Cost = round(Ask_Price - Bid_Price, 2)
                    Gamma = float(Opt_Info[2])
                    Implied_Volatility = float(Opt_Info[3])
                    Time_To_Exp = time_sys.getTimeToExp(Opt_Info[4])
                    ifCall = True
                    if Opr_Type == 'Put':
                        ifCall = False
                    m = ms.models(ifCall, Stock_Price, Strike, Time_To_Exp, interest_rate, Implied_Volatility, lamb,
                                  Gamma)
                    Cal_Price = m.JumpDiffusion()
                    print_sys.printUnu(i, Stock_Name, Expiration_Date, Strike, Opr_Type, Stock_Price, Ask_Price,
                                       Bid_Price,
                                       Trading_Cost, Cal_Price)
                    am.ifBuy(Stock_Name, Expiration_Date, Strike, Opr_Type, Ask_Price, Trading_Cost, Cal_Price,
                             profit_space, assets)
            time.sleep(30)
        rc.robin_logout(time_sys.getFullDateAndTime())
