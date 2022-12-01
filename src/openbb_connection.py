from openbb_terminal.sdk import openbb
#test

def getUnu(threshold):
    unu_df = openbb.stocks.options.unu()
    unu_df = unu_df[0]
    tickers = []
    exps = []
    strikes = []
    types = []
    for index, row in unu_df.iterrows():
        if row['Vol/OI'] > threshold:
            tickers.append(row['Ticker'])
            exps.append(row['Exp'])
            strikes.append(row['Strike'])
            types.append(row['Type'])
        else:
            break
    return tickers, exps, strikes, types

