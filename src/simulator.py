import collections
import time_system as ts
import re

float_list = ['Current Deposit', 'Strike', 'Price per share', 'Cost', 'Earning By Far', 'Bought At', 'Sell At']
int_list = ['ID', 'Shares']


def readCurrent():
    portfolio = collections.defaultdict()
    with open('logs/portfolio.txt', 'r') as f:
        lines = f.readlines()
    f.close()
    curr = re.split('; |;', lines[-1])
    curr = curr[:-1]
    for item in curr:
        items = re.split(': ', item)
        key = items[0]
        if key in float_list:
            value = float(items[1])
        elif key in int_list:
            value = int(items[1])
        else:
            value = items[1]
        portfolio[key] = value
    return portfolio


def getCurrDepo(portfolio):
    return portfolio['Current Deposit']


def getCurrAsset(portfolio):
    assets = list(filter(None, re.split(']|\[', portfolio['Current Asset'])))
    return assets


def writeOperations(opera: str, stock_name: str, strike: float, exp_date: str, opt_type: str, shares: int,
                    bought_at=None, sell_at=None):
    curr = readCurrent()
    new_id = int(curr['ID']) + 1
    curr_depo = curr['Current Deposit']
    curr_asset = curr['Current Asset']
    curr_earn = curr['Earning By Far']

    time_sys = ts.time_system()
    time = time_sys.getFullDateAndTime()

    cost = 0
    if opera == 'Buy':
        cost = shares * bought_at * 100
    if opera == 'Sell':
        cost = -1 * shares * sell_at * 100
    cost = round(cost, 2)

    operation_message = '\n'
    operation_message += 'ID: ' + f"{new_id:04}" + '; '
    operation_message += 'Operation: ' + opera + '; '
    operation_message += 'Time: ' + time + '; '
    operation_message += 'Stock Name: ' + stock_name + '; '
    operation_message += 'Strike: ' + str(strike) + '; '
    operation_message += 'Expiration Date: ' + exp_date + '; '
    operation_message += 'Type: ' + opt_type + '; '
    operation_message += 'Shares: ' + str(shares) + '; '
    operation_message += 'Bought At: ' + str(bought_at) + '; '
    operation_message += 'Sell At: ' + str(sell_at) + '; '
    operation_message += 'Cost: ' + str(cost) + '; '

    portfolio_message = '\n'
    portfolio_message += 'ID: ' + f"{new_id:04}" + '; '
    portfolio_message += 'Current Deposit: ' + str(curr_depo - cost) + '; '
    portfolio_message += 'Current Asset: '
    asset_item = stock_name + ' ' + str(strike) + ' ' + exp_date + ' ' + opt_type + ' ' + str(bought_at)
    if curr_asset == 'None':
        portfolio_message += '[' + asset_item + ' ' + str(shares) + ']'
    else:
        assets = re.split(']|\[', curr_asset)
        asset_info = collections.defaultdict()
        for asset in assets:
            if len(asset) > 0:
                temp_asset = re.split(' ', asset)
                asset_info[temp_asset[0] + ' ' + temp_asset[1] + ' ' + temp_asset[2] + ' ' + temp_asset[3] +
                           ' ' + temp_asset[4]] = int(temp_asset[5])

        if opera == 'Buy':
            if asset_item in asset_info:
                asset_info[asset_item] += shares
            else:
                asset_info[asset_item] = shares
        elif opera == 'Sell':
            asset_info[asset_item] -= shares
            if asset_info[asset_item] == 0:
                del asset_info[asset_item]
        asset_str = ''
        for k, v in asset_info.items():
            asset_str += '[' + k + ' ' + str(v) + ']'
        if len(asset_str) > 0:
            portfolio_message += asset_str
        else:
            portfolio_message += 'None'
    portfolio_message += '; '
    portfolio_message += 'Earning By Far: ' + str(curr_earn - cost) + '; '

    with open('logs/operations_log.txt', 'a') as f:
        f.write(operation_message)
    f.close()

    with open('logs/portfolio.txt', 'a') as f:
        f.write(portfolio_message)
    f.close()