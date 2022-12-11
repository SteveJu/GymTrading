import re
import robin_connection as rc
import time_system as ts
import simulator as sim


def ifSell(assets):
    if assets != ['None']:
        for asset in assets:
            asset_list = re.split(' ', asset)
            stock_name = asset_list[0]
            strike = float(asset_list[1])
            exp_date = asset_list[2]
            opr_type = asset_list[3]
            bought_at = round(float(asset_list[4]), 2)
            shares_hold = int(asset_list[5])
            info = rc.see_curr_prices(stock_name, exp_date, strike, opr_type)
            curr_bid_price = round(float(info[1]), 2)
            curr_time_to_exp = info[2]
            t = ts.time_system()
            # Add current bid price / (model price) close to 1; bring profit space in
            if bought_at < curr_bid_price or t.getTimeToExp(curr_time_to_exp) < 0.005:
                # print('SELL')
                sim.writeOperations('Sell', stock_name, strike, exp_date, opr_type, shares_hold, bought_at,
                                    curr_bid_price)


def ifBuy(stock_name, exp_date, strike, opr_type, Ask_Price, Cal_Price, profit_space, assets):
    assets_dict = []
    if assets != ['None']:
        for asset in assets:
            asset_list = re.split(' ', asset)
            asset_id = ' '.join(asset_list[:5])
            assets_dict.append(asset_id)
    item_buy = ' '.join([stock_name, str(strike), exp_date, opr_type, str(Ask_Price)])
    if Ask_Price / Cal_Price <= (1 - profit_space) and item_buy not in assets_dict:
        # print('BUY')
        sim.writeOperations('Buy', stock_name, strike, exp_date, opr_type, 10, Ask_Price, None)
