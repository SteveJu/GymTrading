class daily_log_system:
    def __init__(self, current_time):
        self.f = None
        self.file_name = str(current_time).replace(' ', '')
        self.file_name = self.file_name.replace('-', '')
        self.file_name = self.file_name.replace(':', '')
        self.file_name = 'logs/daily/' + self.file_name + '.txt'

    def open_file(self):
        self.f = open(self.file_name, 'a')

    def log(self, message):
        self.f.write(message)
        self.f.write('\n')

    def close_file(self):
        self.f.close()
