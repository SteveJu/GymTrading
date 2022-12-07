import collections

float_list = ['Current Deposit', 'Strike', 'Price per share', 'Total earning']
int_list = ['Shares']


def readCurrent():
    portfolio = collections.defaultdict()
    with open('logs/portfolio.txt', 'r') as f:
        lines = f.readlines()
    curr = lines[-1].split('; ')
    curr = curr[:-1]
    for item in curr:
        items = item.split(': ')
        key = items[0]
        if key in float_list:
            value = float(items[1])
        elif key in int_list:
            value = int(items[1])
        else:
            value = items[1]
        portfolio[key] = value
    return portfolio


def getCurrAsset(portfolio):
    return portfolio['Current Deposit']


def writeBuy(message):
    with open('logs/operations_log.txt', 'w') as f:
        f.write(message)
