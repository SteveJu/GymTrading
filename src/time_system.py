import datetime
import re


class time_system:
    def __init__(self):
        self.today = datetime.date.today()
        self.now = datetime.datetime.now()

    def getFullDateAndTime(self):
        self.today = datetime.date.today()
        self.now = datetime.datetime.now()
        current_time = self.today.strftime('%Y-%m-%d') + ' ' + self.now.strftime('%H:%M:%S')
        return current_time

    def getFullDate(self):
        self.today = datetime.date.today()
        current_time = self.today.strftime('%Y-%m-%d')
        return current_time

    def getFullTime(self):
        self.now = datetime.datetime.now()
        current_time = self.now.strftime('%H:%M:%S')
        return current_time

    def getHour(self):
        self.now = datetime.datetime.now()
        current_time = int(self.now.strftime('%H'))
        return current_time

    def getMin(self):
        self.now = datetime.datetime.now()
        current_time = int(self.now.strftime('%M'))
        return current_time

    def getTimeToExp(self, time: str):
        self.now = datetime.datetime.now()
        time_list = re.split('-|T|:|\+', time)
        time_list = time_list[:-2]
        for t in range(len(time_list)):
            time_list[t] = int(time_list[t])
        exp = datetime.datetime(time_list[0], time_list[1], time_list[2], time_list[3], time_list[4], time_list[5])
        diff = exp - self.now
        delta = datetime.timedelta(days=365)
        return diff / delta
