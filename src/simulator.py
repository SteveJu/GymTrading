import collections


def readCurrent():
    portfolio = collections.defaultdict()
    with open('log.txt', 'r') as f:
        lines = f.readlines()
    curr = lines[-1].split(';')
    curr = curr[:-1]
    for item in curr:
        items = item.split(': ')
        key = items[0]
        try:
            value = float(items[1])
        except:
            value = items[1]
        portfolio[key] = value
    return portfolio


def getCurrAsset(portfolio):
    return portfolio['Total Asset']


def writeToLog(message):
    with open('log.txt', 'w') as f:
        f.write(message)
