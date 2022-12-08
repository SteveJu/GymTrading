def printSection():
    print('==========================Section==========================')


def printCurrTime(current_time):
    print("Current Time =", current_time)


def printCurrDepo(curr_depo):
    print("Current Time =", curr_depo)


def printEmpty():
    print('*********************************************************')
    print('No unusual options for now, will check 30 minutes later.')
    print('*********************************************************')


def printUnu(i, Stock_Name, Expiration_Date, Strike, Opr_Type, Stock_Price, Ask_Price, Bid_Price, Trading_Cost,
             Cal_Price):
    print('**************************************************No.', i + 1, '***')
    print('STOCK NAME: ', Stock_Name)
    print('EXPIRATION DATE: ', Expiration_Date)
    print('STRIKE: ', Strike)
    print('OPERATION TYPE: ', Opr_Type)
    print('STOCK PRICE: ', Stock_Price)
    print('ASK PRICE: ', Ask_Price)
    print('BID PRICE: ', Bid_Price)
    print('TRADING COST: ', Trading_Cost)
    print('CALCULATED PRICE: ', Cal_Price)
