import time_system as ts
import daily_log_system as dls

import re


class print_system:
    def __init__(self):
        self.ts = ts.time_system()
        self.current_time = self.ts.getFullDateAndTime()
        self.dls = dls.daily_log_system(self.current_time)

    def printCurrTime(self):
        message = "Current Time = " + str(self.current_time)
        print(message)
        self.dls.open_file()
        self.dls.log(message)
        self.dls.close_file()

    def printSection(self):
        message = '=======================Observation========================='
        print(message)
        self.dls.open_file()
        self.dls.log(message)
        self.dls.close_file()

    def printEmpty(self):
        message = '***********************************************************'
        message += '\n'
        message += 'No unusual options for now, will check 30 minutes later.'
        message += '\n'
        message += '***********************************************************'
        print(message)
        self.dls.open_file()
        self.dls.log(message)
        self.dls.close_file()

    def printCurrDepo(self, curr_depo):
        message = "Current Deposit = " + str(curr_depo)
        print(message)
        self.dls.open_file()
        self.dls.log(message)
        self.dls.close_file()

    def printAssets(self, assets):
        self.dls.open_file()
        message = '==========================Asset============================'
        print(message)
        self.dls.log(message)
        if assets == ['None']:
            message = 'NO ASSETS RIGHT NOW.'
            print(message)
            self.dls.log(message)
        else:
            for i in range(len(assets)):
                asset_list = re.split(' ', assets[i])
                message += 'STOCK NAME: ' + str(asset_list[0])
                message += '\n'
                message += 'STRIKE: ' + str(asset_list[1])
                message += '\n'
                message += 'EXPIRATION DATE: ' + str(asset_list[2])
                message += '\n'
                message += 'OPERATION TYPE: ' + str(asset_list[3])
                message += '\n'
                message += 'BOUGHT AT: ' + str(asset_list[4])
                message += '\n'
                message += 'SHARES HOLD: ' + str(asset_list[5])
                message += '\n'
                message += '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^No.' + str(i + 1) + '^^^'
                print(message)
                self.dls.log(message)
        self.dls.close_file()

    def printUnu(self, i, Stock_Name, Expiration_Date, Strike, Opr_Type, Stock_Price, Ask_Price, Bid_Price,
                 Trading_Cost,
                 Cal_Price):
        message = 'STOCK NAME: ' + str(Stock_Name)
        message += '\n'
        message += 'EXPIRATION DATE: ' + str(Expiration_Date)
        message += '\n'
        message += 'STRIKE: ' + str(Strike)
        message += '\n'
        message += 'OPERATION TYPE: ' + str(Opr_Type)
        message += '\n'
        message += 'STOCK PRICE: ' + str(Stock_Price)
        message += '\n'
        message += 'ASK PRICE: ' + str(Ask_Price)
        message += '\n'
        message += 'BID PRICE: ' + str(Bid_Price)
        message += '\n'
        message += 'TRADING COST: ' + str(Trading_Cost)
        message += '\n'
        message += 'CALCULATED PRICE: ' + str(Cal_Price)
        message += '\n'
        message += '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^No.' + str(i + 1) + '^^^'
        print(message)
        self.dls.open_file()
        self.dls.log(message)
        self.dls.close_file()
