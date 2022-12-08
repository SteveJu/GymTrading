import datetime


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
